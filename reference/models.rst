Models, lock types and capabilities
===================================

Lockly behaviour varies by model *and* firmware. Three identifiers matter, and
they are not the same thing. 🔎 from the apps and LocklyHA.

Model code vs. lock type vs. hub
--------------------------------

- **Model code** — e.g. ``PGD728FN``, ``PGK728WRHK``. The prefix hints at the
  family: ``PGD`` deadbolt/latch, ``PGK`` newer Wi-Fi/Visage, ``PGI`` interconnect
  / specialty, ``PGH`` **hub** (PGH200/220 Secure LINK; PGH260 Matter). It is in
  the ``mod`` / ``lockType`` fields of the :http:post:`qrylknew` lock data, and in
  the app as ``isPGxxxx()`` predicates on ``BluetoothBean`` (114 of them).
- **Lock type number** — a small integer the **lock reports itself**, as byte 18
  of the decrypted status payload (:doc:`/ble/commands/status`). It selects the
  BLE frame variant (:doc:`/ble/commands/unlock_lock`). ``qrylknew`` does **not**
  return it; it defaults to ``1`` when unknown — so **query status before building
  commands**.
- **Capability flags** — ``isSupport…()`` methods combining model and firmware
  version (e.g. ``isSupportWelcomeMode()``, ``isSupport82Cmd()``). The per-feature
  pages list the relevant models; the authoritative source is
  ``BluetoothBeanManager`` in the app, and LocklyHA's ``capabilities.py`` ports
  the frame-shaping ones.

Known model → lock-type numbers
-------------------------------

From LocklyHA's ``MODEL_LOCK_TYPES`` and the unlock-variant analysis (✅ for the
hardware-tested ones):

========== =========== ================================================
Lock type  Model        Frame variant (:doc:`/ble/commands/unlock_lock`)
========== =========== ================================================
2          PGD728F      ``22``
4          PGD628F      ``22``
21         PGD628FN     ``22``
22         PGD728FN     ``22``
105        PGK728WRHK   ``52`` (Visage; Wi-Fi-native) ✅
121        PGI301       ``52`` (no timestamp)
124        PGD728FG25   ``52``
125        PGD728FNG25  ``52``
127        PGD628FG25   ``52``
129        PGD728FN21   500-group
========== =========== ================================================

Any model not listed falls back to lock type ``1`` / the ``22`` frame until the
lock reports otherwise.

Capability flags worth knowing
------------------------------

===================================== =================================================
Flag                                   Gates
===================================== =================================================
``isSupport82Cmd()``                   the ``52`` unlock frame (all Wi-Fi-native locks)
``isSupportMqttConnect()``             the MQTT device channel (:doc:`transports`)
``isRemoteControl()``                  classic hub relay via ``senddata``
``isMatterHub()``                      ``hubId.startsWith("PGH260")``
``isSupport8SegmentWelcomeMode()``     8-slot Welcome Mode ``9B`` (:doc:`/ble/commands/welcome_mode`)
``isSupportWelcomeMode()``             single-slot Welcome Mode ``46``
``isSupportRainModeSetting()``         Rain Mode ``56`` (:doc:`/ble/commands/rain_mode`)
``isSupportAutoFirmwareUpdate()``      account-wide auto-OTA (:doc:`/ble/commands/firmware`)
``isSupportTimestamp()``               nonce vs. real timestamp in the unlock frame
===================================== =================================================
