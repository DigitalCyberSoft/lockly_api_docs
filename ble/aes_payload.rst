AES-128 payload encryption
==========================

The payload inside every BLE frame is encrypted with **AES-128/ECB**. The 16-byte
key is derived per-lock from the lock's master code (``mc``) and device UUID
(``ID``), both from the ``qrylknew`` lock data. (🔎 adapted from
LocklyHA; ✅ exercised there on real hardware.)

.. warning::

   The master code plus the UUID *are* the key to the lock. Anyone holding both
   can forge any command on this page. See :doc:`/methodology`.

Key derivation
--------------

``DataUtils.m86653h``:

.. sourcecode:: python

   def derive_aes_key(master_code: str, uuid: str) -> bytes:
       # expand each decimal digit of mc with a leading "0":
       # "24860092" -> "0204080600000902"
       mc_bytes   = bytes.fromhex("".join("0" + c for c in str(master_code)))  # 8 B
       uuid_bytes = bytes.fromhex(uuid)                                        # 12 B

       key = bytearray(16)
       for i in range(len(str(master_code))):          # 8 for an 8-digit mc
           key[i] = uuid_bytes[i % len(uuid_bytes)] ^ mc_bytes[i]
       for i in range(8, 12):
           key[i] = uuid_bytes[i] ^ mc_bytes[i - 8]
       for i in range(12, 16):
           key[i] = uuid_bytes[i - 12]
       return bytes(key)

**Example** — ``mc = "24860092"``, ``uuid = "2d0023003030471333363838"`` →
key ``2f042b0630304e113132303e2d002300``.

Master-code field encoding
---------------------------

The master code is *also* embedded in many command plaintexts, XOR-encoded
(``HexUtils.m86806g``). This is a different transform from the key derivation
above — note it uses the raw digit values, not the ``0``-expanded bytes:

.. sourcecode:: python

   def encrypt_master_code(master_code: str, uuid: str) -> str:
       mc_bytes   = bytes(int(c) for c in str(master_code))   # digit values
       uuid_bytes = bytes.fromhex(uuid)
       enc = bytes(mc_bytes[i] ^ uuid_bytes[i % len(uuid_bytes)]
                   for i in range(len(mc_bytes)))
       return enc.hex().upper()                                # 16 hex chars for 8-digit mc

This appears in command plaintexts as ``<mc_len> <enc_mc>`` where ``mc_len`` is
the byte length of ``enc_mc`` (``08`` for an 8-digit code).

The nonce
---------

Commands that change lock state (unlock, lock, …) include an 8-byte **nonce**
that the lock supplies in its status response (bytes 19–26 of the decrypted
status payload) and expects echoed in the next command. The app caches it per
UUID (``ble_aes_random_numbers_...``). On hardware without
``isSupportTimestamp()`` it is this cached value, **not** a timestamp. Practically:
query status first, keep the nonce, use it in the state-changing command.
