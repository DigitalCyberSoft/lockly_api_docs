Unlock and lock (``22`` / ``52``)
=================================

Unlock and lock are the same command with a different *action* byte. ✅ Verified
on hardware by LocklyHA (PGD628FN + PGH220 hub; PGK728WRHK Visage over MQTT).
This is the single most useful command and also the one with the most model
variation, so read :doc:`status` first — the lock reports its *type* there, and
the type selects the frame layout.

.. tip::

   The whole sequence: **query status** (:doc:`status`) → keep the 8-byte nonce →
   build the unlock/lock frame with that nonce → send it → **parse the ACK**
   (``cod=200`` alone does not mean the lock acted).

The ``22`` frame (most locks)
-----------------------------

``NewUnlockCmd.getData`` concatenates an ordered argument list. Two rules bite:
a one-character argument is left-padded to two (``"2"`` → ``02``), and an *empty*
argument is skipped entirely (it disappears, it does not become ``00``).

.. sourcecode:: text

   22  <mc_len>  <enc_mc>  <unlock_type>  <pwd>  <pwd_id>  <action>  <str3>  <nonce>

=============== ================================================= =============================
Field            Value                                             Notes
=============== ================================================= =============================
``22``           command code                                      ``52`` on Wi-Fi-native, below
``mc_len``       ``08``                                            decimal byte length of ``enc_mc``
``enc_mc``       XOR-encoded master code                           :doc:`../aes_payload`
``unlock_type``  ``02`` host/admin, ``03`` long-term/staff
``pwd``          lock admin password ``hc``, digit-expanded        ``"980798"`` → ``090800070908``
``pwd_id``       **``00`` for a host**                             see warning
``action``       ``01`` unlock, ``02`` lock
``str3``         **``01`` via hub, ``00`` direct BLE**             see warning
``nonce``        8-byte value from the last status response        omitted if never queried
=============== ================================================= =============================

Zero-pad to the AES block boundary, encrypt, wrap (:doc:`../frame_format`).

.. warning::

   Two fields were the long-standing cause of "unlock silently fails behind a
   ``cod=200``" (both had to be right at once):

   - **``str3``** is ``01`` for any hub-relayed (``senddata`` / MQTT) command. The
     app's default of ``00`` makes the lock NACK.
   - **``pwd_id``** for a host is slot ``00`` — the slot the host credential
     actually occupies. Sending ``01`` makes the lock compare the wrong
     credential and reject with BLE error ``FF`` (wrong password).

Lock vs unlock
--------------

``NewLockCmd`` calls ``NewUnlockCmd.getDataForHub(bean, password, "2")`` — the
identical frame with ``action = 02``. The ``senddata`` ``directive``
field (``"unlock"`` / ``"lock"``) is a hint to the hub; the action byte is
authoritative.

The ``52`` frame (Wi-Fi-native locks — incl. Visage)
----------------------------------------------------

``isSupport82Cmd()`` is true for every Wi-Fi-native model (PGK728WRHK Visage,
PGD728FG25, …). These **never** use the ``22`` layout. ✅ Confirmed on two
PGK728WRHK (firmware 1.14.31 and 3.00.24).

.. sourcecode:: text

   52  <mc_len>  <enc_mc>  <unlock_type>  <pwd>  <user_id>  <action>  <str3>  <epoch_ms>

Three fields differ from ``22``, and because two of them change the frame length
they must all be correct together:

- **``user_id``** replaces ``pwd_id``: **two bytes, little-endian**
  (``{i%256, i/256}``). For the lock's **owner** this is ``0`` (``0000``).
- **``epoch_ms``**: **eight bytes, little-endian**, the phone's own
  ``System.currentTimeMillis()`` — not the packed time, not the stored nonce
  (these locks have ``isSupportTimestamp() == true``, so the lock's nonce is not
  replayed).
- **type byte low nibble** is ``B`` for a host (``isHost() ? 11 : isLongTerm() ?
  13 : 12``), not ``5``.

500-group locks (e.g. PGD728FN21, type 129) use ``22`` with an extra ``02`` after
the command code and a two-byte slot via ``getCmdLenString()``.

Lock type → variant
--------------------

The lock reports its type as byte 18 of the status payload (``qrylknew`` does not
return it; it defaults to 1 when absent). Known values:

===== =============== =========
Type   Model           Variant
===== =============== =========
4      PGD628F         ``22``
21     PGD628FN        ``22``
121    PGI301          ``52`` (no timestamp)
124    PGD728FG25      ``52``
125    PGD728FNG25     ``52``
127    PGD628FG25      ``52``
129    PGD728FN21      500-group
105    PGK728WRHK      ``52`` (Visage; from LocklyHA capabilities)
===== =============== =========

LocklyHA's ``capabilities.py`` has the full ported model/type sets.
