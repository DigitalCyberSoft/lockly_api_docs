BLE frame format
================

BLE commands and responses travel as hex strings — inside the ``cmd`` / ACK
fields of ``senddata`` when relayed by a hub, inside the MQTT
``lockCommandRequest`` payload, or written directly to the lock's GATT
characteristic over Bluetooth. The frame is the same in every case.

There are two layouts: the outgoing **command** frame and the incoming
**response** frame. (🔎 adapted from LocklyHA, ✅ core commands verified there.)

Command frame (host → lock)
---------------------------

.. sourcecode:: text

   ┌──────────────┬──────────────┬────────────────────┬───────────┬─────────┐
   │ Magic (4 B)  │ Length (2 B) │ AES payload (N B)  │ Type (1 B)│ CRC (1B)│
   │ A1 B2 C3 D4  │ LE uint16    │ 16 or 32 bytes     │ see below │ CRC-8   │
   └──────────────┴──────────────┴────────────────────┴───────────┴─────────┘

- **Magic**: constant ``A1 B2 C3 D4``.
- **Length**: little-endian ``uint16`` = total frame length = ``N + 8``.
- **AES payload**: the command, AES-128/ECB encrypted (:doc:`aes_payload`), a
  multiple of 16 bytes.
- **Type byte**: ``(zero_pad_count << 4) | encrypt_type``.

  - ``encrypt_type = 5`` for AES-128/ECB (all hub / Wi-Fi commands).
  - ``zero_pad_count`` = number of ``\x00`` bytes appended to the plaintext to
    reach the AES block boundary.
- **CRC**: Lockly's non-standard CRC-8 (:doc:`crc`), over every byte of the frame
  **except** the CRC byte itself.

Response frame (lock → host)
----------------------------

.. sourcecode:: text

   ┌──────────────┬──────────────┬────────────────┬────────────────────┬─────────┐
   │ Magic (4 B)  │ Length (2 B) │ CmdType (2 B)  │ AES payload (32 B) │ CRC (1B)│
   │ A1 B2 C3 D4  │ LE uint16    │ e.g. 0A 1E     │ two AES blocks     │ CRC-8   │
   └──────────────┴──────────────┴────────────────┴────────────────────┴─────────┘

The response inserts a 2-byte **CmdType** between Length and the payload, and has
**no** Type byte before the CRC. CmdType is ``0A`` followed by the command byte
that is being answered — e.g. ``0A1E`` answers a status query (``1E``), ``0A22``
answers unlock/lock (``22``), ``0A9B`` answers a Welcome Mode command (``9B``).

Extracting the payload (hex-string positions, 2 chars = 1 byte):

.. sourcecode:: python

   payload_hex = ack_hex[16:-2]   # drop magic(8) + length(4) + cmdtype(4), and CRC(2)
   payload     = bytes.fromhex(payload_hex)        # 16 or 32 bytes
   plaintext   = AES.new(aes_key, AES.MODE_ECB).decrypt(payload).rstrip(b"\x00")

The first plaintext byte of most responses is a status byte: ``00`` = success.
Lock-side **rejections** come back as a short unencrypted frame with CmdType
``0C`` and an error nibble (``F1``–``FF``; ``FF`` = wrong password). A ``cod=200``
from the cloud only means the hub relayed the frame — it says nothing about
whether the lock accepted it, so always parse the ACK.
