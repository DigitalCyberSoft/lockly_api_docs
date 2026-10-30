Firmware updates (OTA)
======================

How the apps update lock, hub and camera firmware. 🔎 traced from app 3.3.4 /
Home 1.6.2; not exercised. The important split for a computer-based client is
**who downloads the firmware**: the device itself (cloud-driven, scriptable
remotely) or the phone (streamed over Bluetooth, needs a radio near the lock).

Wi-Fi-native locks (incl. Visage PGK728WRHK)
--------------------------------------------

Cloud/self-download — scriptable remotely:

- **Check**: ``fwver/msh/new`` with ``{acct, did, model}`` (3DES) returns
  a separate ``downloadUrl`` + version + MD5 + CRC per component (ble, front,
  back, screen, hub).
- **Update**: an MQTT ``firmwareUpgradeRequest`` with ``type = MULTIPLE``, the
  ``downloadUrl`` and per-file ``args``. The lock downloads the files itself and
  reports ``firmwareUpgradeProgress`` / ``firmwareUpgradeFailure``. (Version
  numbers are encoded by removing the dots, prefixing/padding, and parsing as
  hex.)
- **Exception**: the Bluetooth chip's own firmware uses **SUOTA** (the standard
  Dialog/Renesas profile, GATT service ``0xFEF5``) and must be streamed from a
  device in Bluetooth range.

Classic locks (likely the Touch models)
----------------------------------------

Phone-streamed over Bluetooth — **not** relayed through the hub:

- **Check**: ``lockly/syspara`` (``para = "firmware_ver"``, plus
  ``mod``, ``ref``, ``did``) or ``fwver/new``.
- **Transfer**: Lockly BLE commands ``08``/``2F`` (announce version) and ``0E``
  (send data), in 500-byte blocks written 20 bytes at a time, each block ACKed,
  up to 3 resends (``OTASendDataCmd`` / ``DoubleOTASendDataCmd``, byte ``30``;
  ``LightUpgradeCmd`` ``3F`` for the LED ring). The string
  ``ble_mode_not_ota`` reflects that some OTA is blocked when connected over BLE.
- There is no hub-relay routing for these commands, so the app cannot push these
  updates through a hub.

Hubs
----

Cloud-driven:

- **PGH200 / PGH220**: ``otaver`` to check, then
  ``ota`` ``{acct, hubid, hubver, mdna}`` (3DES). The hub updates itself.
- **PGH260 (Matter)**: MQTT ``firmwareUpgradeRequest`` with ``type = HUB_WIFI``.

Automatic updates — the easy win
---------------------------------

🔎 ``isSupportAutoFirmwareUpdate()`` is true for the **Visage (PGK728WRHK)**,
PGK728WHK, PGK7SWHK and some PGD798/798NV firmware ranges. The setting is
**account-wide** (not per lock):

- ``ota/upgrade/automatic/setting/create`` or
  ``ota/upgrade/automatic/setting/update`` (3DES) with e.g.
  ``{type: 1, startTime: "00:00:00", endTime: "06:00:00", status: "ON"}``.

🧩 Turning this on once likely keeps the Visage updated with no further app
involvement (except its Bluetooth-chip component). Other endpoints:
``ota/upgrade/check``, ``ota/upgrade/apply``,
``update/dv/fw`` (appears to *report* the installed version, RSA),
``vision/allver`` / ``vision/camgwver`` (camera/Vision).
