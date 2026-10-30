Bluetooth (BLE) command layer
=============================

Every action a Lockly lock performs — unlock, lock, status, adding a code,
changing a setting — is ultimately a **BLE command frame** sent to the lock.
What differs is only the *transport* that carries the frame:

- directly, over a Bluetooth GATT connection from a phone;
- relayed by a Wi-Fi hub through the ``senddata`` REST endpoint;
- or over the MQTT device channel (newer Matter hubs and Wi-Fi-native locks).

The frame itself is identical across transports (one flag byte aside). This
section documents that frame: its structure, the AES-128 payload encryption, the
CRC, and the individual commands. :doc:`/reference/transports` explains how the
app chooses a transport, and :doc:`/reference/command_index` lists every command
byte seen in the app.

.. note::

   Most of this section is adapted, with thanks, from the hardware-validated
   notes in **LocklyHA** (MIT — see :doc:`/CREDITS`). Core commands (status,
   unlock) are ✅ verified there on real hardware; feature commands documented
   here are 🔎 traced from the app unless stated otherwise. Read
   :doc:`/methodology` for what the markers mean.

.. toctree::
   :maxdepth: 1

   frame_format
   aes_payload
   crc
   commands/status
   commands/unlock_lock
   commands/welcome_mode
   commands/rain_mode
   commands/access_codes
   commands/enrolment
   commands/settings
   commands/firmware
