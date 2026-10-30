Query lock status (``1E``)
==========================

Reads the lock's live state: firmware version, lock/door status, battery, and
the 8-byte nonce that every state-changing command must echo (:doc:`../aes_payload`).
(🔎 adapted from LocklyHA; ✅ verified there on hardware.)

.. important::

   A live status query **wakes the lock and it beeps**. For a silent reading, use
   the hub's cached status instead — ``lock/cachedstatus/get`` — which
   returns the hub's last report without touching the lock (needs hub firmware
   build ≥ 422).

Command plaintext
-----------------

.. sourcecode:: text

   1E  <mc_len>  <enc_mc>  <time_hex>  01

================= ======== =================================================
Field             Length   Description
================= ======== =================================================
``1E``            1 B      command code
``mc_len``        1 B      byte length of ``enc_mc`` (``08`` for 8-digit mc)
``enc_mc``        8 B      XOR-encoded master code (:doc:`../aes_payload`)
``time_hex``      6 B      current time ``yyMMddHHmmss``, each pair hex-encoded
``01``            1 B      is_remote = 1 (hub/cloud path)
================= ======== =================================================

17 bytes; zero-pad to 32, AES-128/ECB encrypt, wrap in a command frame
(:doc:`../frame_format`).

Response payload
----------------

Decrypt the 32-byte payload, strip trailing ``00``. Positions are hex-string
character offsets (2 chars = 1 byte):

=============== ======= ========================================================
Hex chars        Bytes   Field
=============== ======= ========================================================
``d[0:8]``       0–3     firmware version (4 bytes)
``d[8:10]``      4       **status byte** (see below)
``d[10:14]``     5–6     wake-up voltage, LE uint16, ``×10 mV``
``d[14:18]``     7–8     start voltage, LE uint16
``d[18:30]``     9–14    time ``yyMMddHHmmss``
``d[30:32]``     15      programming status
``d[32:36]``     16–17   auto-lock delay (s), LE uint16
``d[36:38]``     18      **lock type** (selects the command variant — see
                         :doc:`unlock_lock`)
``d[38:54]``     19–26   8-byte nonce + feature flags
=============== ======= ========================================================

Status byte (``d[8:10]``):

.. list-table::
   :header-rows: 1
   :widths: 8 12 55 25

   * - Bit
     - Mask
     - Meaning when set
     - Confidence
   * - 0
     - ``0x01``
     - door circuit open — door ajar **or** no sensor fitted
     - ✅ verified
   * - 1
     - ``0x02``
     - lock is **unlocked** (open)
     - ✅ verified
   * - 2
     - ``0x04``
     - *unknown* (reads 0 in all samples)
     - ⚠️ untested
   * - 4
     - ``0x10``
     - battery reading invalid
     - 🧩 inferred

.. warning::

   Bit 0 is a **circuit** state, not a sensor-presence flag. An unfitted sensor
   is an open circuit and reads ``1`` just like an open door; only ``0`` is
   unambiguous (it proves a sensor exists and the door is shut). Do **not** carry
   over the bit meanings from the hub ``cachedstatus`` ``sts`` integer
   (``lock/cachedstatus/get``) — that integer uses a *different* layout
   that genuinely has presence bits. LocklyHA documents getting this wrong twice.

.. sourcecode:: python

   status_byte = int(d[8:10], 16)
   is_locked   = not ((status_byte >> 1) & 1)
   wake_mv     = (int(d[10:12], 16) + int(d[12:14], 16) * 256) * 10

Battery (4×AA locks): ``pct = clamp((v - 4.5) / 1.5 * 100, 0, 100)`` where
``v = wake_mv / 1000``. Rechargeable-pack models instead report a percentage
directly in a different byte — see LocklyHA's battery notes.
