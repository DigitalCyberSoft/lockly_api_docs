BLE command index
=================

Every lock action travels as an AES-128 encrypted BLE frame whose ``cmd`` byte
(see :doc:`/ble/frame_format`) selects the operation. The table below lists
every command byte observed in the Lockly Android app's ``*Cmd`` classes, with
the purpose derived from each class's name, methods and logging strings.
**Availability is per lock model and firmware** — a byte present here is not
accepted by every lock; see the per-feature pages and :doc:`/reference/models`.

.. note::

   🔎 Code-traced from app bytecode (``com.lockly.smartlock`` 3.3.4, with
   ``com.lockly.smartlock.pro`` 1.4.9 for Manager-only commands). Command bytes
   are the first argument to the frame builder ``HexUtils.c(...)`` /
   ``HexUtils.l(...)`` or the ``0A``-prefixed response marker in
   ``isCommandRight()``. Not individually hardware-tested here.

.. list-table::
   :header-rows: 1
   :widths: 8 34 44 14

   * - Byte
     - Command class
     - Purpose
     - Type
   * - ``0x07``
     - HostUnlockCmd
     - Legacy admin lock/unlock (pre-``0x22`` hardware)
     - set
   * - ``0x07``
     - GuestUnlockCmd
     - Legacy guest lock/unlock
     - set
   * - ``0x08``
     - OTACheckVerCmd
     - OTA: query current firmware version
     - query
   * - ``0x09``
     - QueryLockStatusCmd
     - Query lock/door/battery status (pre-``0x34``)
     - query
   * - ``0x0B``
     - SetAlarmCmd
     - Set tamper-alarm sensitivity level (1–3)
     - set
   * - ``0x0F``
     - DeleteLockCmd
     - Factory-unpair / delete lock
     - set
   * - ``0x10``
     - ResetLockAndReStartCmd
     - Restart / reset the lock
     - set
   * - ``0x11``
     - SetMasterCodeCmd
     - Set the initial master code
     - set
   * - ``0x12``
     - SetAutoLockCmd
     - Set auto-lock timeout (seconds)
     - set
   * - ``0x14``
     - StartSensorCmd
     - Begin fingerprint enrolment
     - set
   * - ``0x14``
     - StartNewMasterCodeCmd
     - Begin new master-code entry
     - set
   * - ``0x15``
     - QuerySensorCmd
     - Query fingerprint list
     - query
   * - ``0x15``
     - TPCCmd
     - Set OMK / third-party-code parameters
     - set
   * - ``0x16``
     - DeleteSensorCmd
     - Delete a fingerprint
     - set
   * - ``0x17``
     - StopSensorCmd
     - Stop fingerprint enrolment
     - set
   * - ``0x19``
     - LockSettingsCmd / LockSettings2Cmd
     - Lock settings: random mode, key tone, alarm, auto-lock, door sensor, etc.
     - set/query
   * - ``0x1B``
     - SetOACCmd
     - Set offline access code (legacy OAC) seeds
     - set
   * - ``0x1E``
     - SetShortOACCmd
     - Set short/4-digit one-time OAC seeds
     - set
   * - ``0x1x``
     - QueryShortOacCmd
     - Query short one-time OAC (OAC/OMK family; exact byte via ``CODE_GET_QUERY_NEW_OAC``)
     - query
   * - ``0x1x``
     - SetOMKCmd / QueryOMKCmd
     - Set/query one-time master key (OMK) seeds (``"1"+type``)
     - set/query
   * - ``0x1x``
     - OtherQueryCmd
     - Query lock analysis/diagnostic counters (``CMD_LOCK_OTHER_QUERY``)
     - query
   * - ``0x20``
     - QueryOACUnlockRecordCmd
     - Query OAC unlock records
     - query
   * - ``0x21``
     - SetSensorAutoLockCmd
     - Set sensor-triggered auto-lock
     - set
   * - ``0x22``
     - NewUnlockCmd
     - **Lock / unlock (current)**
     - set
   * - ``0x30``
     - OTASendDataCmd / DoubleOTASendDataCmd
     - OTA: stream firmware data blocks
     - set
   * - ``0x31``
     - QuerySensorNameCmd
     - Query fingerprint name
     - query
   * - ``0x32``
     - SetDoorSensorStateCmd / CheckDoorSensorStateCmd
     - Set / check wired door-sensor state
     - set/query
   * - ``0x33``
     - SetTimeZoneCmd
     - Set the lock's time zone
     - set
   * - ``0x34``
     - LockStatusAndReportCmd
     - Query lock status + report (current)
     - query
   * - ``0x35``
     - SetLockStateCmd
     - Set lock state
     - set
   * - ``0x36``
     - NotificationTalkCmd
     - Notification / talk channel
     - set
   * - ``0x37``
     - StartPairingLightCmd / EndPairingLightCmd / DeleteLightCmd
     - Enter/quit/delete ambient-light (LED strip) pairing
     - set
   * - ``0x39``
     - DownloadSensorCmd
     - Download fingerprint/sensor template
     - query
   * - ``0x3A``
     - UploadSensorCmd
     - Upload fingerprint/sensor template
     - set
   * - ``0x3B``
     - FingerprintCmd
     - Fingerprint operation
     - set
   * - ``0x3C``
     - NewSensorCmd / TestNewSensorCmd
     - Enrol fingerprint (new flow)
     - set
   * - ``0x3D``
     - ActivationSensorCmd
     - Activate a sensor/credential
     - set
   * - ``0x3E``
     - NewDeleteSensorCmd
     - Delete fingerprint (new flow)
     - set
   * - ``0x3F``
     - LightUpgradeCmd
     - Ambient-light firmware upgrade
     - set
   * - ``0x40``
     - LightSensitivityCmd
     - Set ambient-light sensitivity
     - set
   * - ``0x41``
     - LightTrackingCmd
     - Ambient-light tracking / report
     - set/report
   * - ``0x43``
     - WelcomeModeCmd
     - Scheduled auto-lock / welcome (legacy; ``0x12`` on non-AES locks)
     - set/query
   * - ``0x46``
     - AlwaysOpenModeCmd
     - Welcome / "always open" single schedule
     - set/query
   * - ``0x47``
     - LedStateCmd
     - Set status-LED state
     - set
   * - ``0x48``
     - StartHandleCmd
     - Start-handle / door-handle setting
     - set
   * - ``0x49``
     - SetLockTypeCmd
     - Set lock hardware type
     - set
   * - ``0x4A``
     - StartSensorWithUserNoCmd
     - Begin fingerprint enrolment for a user slot
     - set
   * - ``0x4B``
     - SetHostPwdCmd
     - Set the host (admin) password
     - set
   * - ``0x4B``
     - SetPeriodicPwdCmd
     - Set a recurring (periodic) PIN
     - set
   * - ``0x4B``
     - SetPwdWithUserNoCmd
     - Set a PIN for a user slot (family/staff)
     - set
   * - ``0x4D``
     - DeleteGuestPwdCmd / DeleteWithUserNoCmd
     - Delete a guest / user-slot PIN
     - set
   * - ``0x4F``
     - SetLockModeCmd / MultipleVerification79Cmd
     - Set unlock mode / multi-verification
     - set
   * - ``0x50``
     - QueryUserListCmd
     - Query the user list
     - query
   * - ``0x51``
     - QueryUserDetailCmd
     - Query one user's detail
     - query
   * - ``0x53``
     - SyncUnlockRecordCmd
     - Sync unlock/access records
     - query
   * - ``0x54``
     - SetGuestPwdCmd
     - Set a guest / family PIN
     - set
   * - ``0x56``
     - RainModeCmd
     - Rain mode (disable keypad in rain)
     - set/query
   * - ``0x57``
     - NewSensorWithoutDateCmd
     - Enrol fingerprint (no date window)
     - set
   * - ``0x58``
     - LockMode88Cmd / WorkModeCmd
     - Set lock work mode
     - set
   * - ``0x59``
     - PairSensorCmd
     - Pair a wireless sensor
     - set
   * - ``0x5A``
     - CommunicationIdCmd
     - Communication / client ID
     - set/query
   * - ``0x5C``
     - UpdateFingerprintCodeCmd
     - Update fingerprint's user-slot number
     - set
   * - ``0x5D``
     - DoNotDisturbModeCmd
     - Do Not Disturb mode schedule
     - set/query
   * - ``0x5E``
     - DoorbellSoundSettingCmd
     - Doorbell sound setting
     - set
   * - ``0x60``
     - UserRoomNumberCmd
     - Set per-user room number (rental/hotel)
     - set
   * - ``0x66``
     - FingerprintSpecialModelCmd
     - Fingerprint special-model handling
     - set
   * - ``0x67``
     - DoubleUpgradeCheckCmd
     - OTA: dual-image version check
     - query
   * - ``0x68``
     - PirOpenTimeCmd
     - PIR (motion) open-time setting
     - set
   * - ``0x69``
     - PirToLockCmd
     - PIR-to-lock behaviour
     - set
   * - ``0x6A``
     - PirVideoTimeCmd
     - PIR video recording duration
     - set
   * - ``0x6B``
     - DoubleOTATypeCmd
     - OTA: dual-image type select
     - set
   * - ``0x6C``
     - StartSensor108Cmd
     - Begin fingerprint enrolment (108 flow)
     - set
   * - ``0x6D``
     - QueryMultiSensorCmd
     - Query multiple sensors
     - query
   * - ``0x6F``
     - PirOpenTimeMultipleCmd
     - PIR open-time, multi-period
     - set
   * - ``0x70``
     - QueryMultiPwdCmd
     - Query multiple PINs
     - query
   * - ``0x73``
     - AccessUser115Cmd
     - Access user (115)
     - set
   * - ``0x74``
     - NewUserSensor116Cmd
     - New user sensor (116)
     - set
   * - ``0x75``
     - AlwaysOpenModeStatusCmd
     - Welcome-mode entry method (first-entry vs automatic)
     - set/query
   * - ``0x76``
     - AccessUserDetail118Cmd
     - Access-user detail (118)
     - query
   * - ``0x77``
     - AccessUserSensorList119Cmd
     - Access-user sensor list (119)
     - query
   * - ``0x7A``
     - AccessUser122Cmd
     - Access user (122)
     - set
   * - ``0x7C``
     - Log124Cmd
     - Read access log (124)
     - query
   * - ``0x7D``
     - NewUserSensor125Cmd
     - New access user (125)
     - set
   * - ``0x7E``
     - ImportUser126Cmd
     - Bulk-import users (126)
     - set
   * - ``0x7F``
     - QuerySensorInfoCmd
     - Query RFID/sensor info
     - query
   * - ``0x80``
     - DeleteRfInfoCmd
     - Delete RFID credential
     - set
   * - ``0x83``
     - ReplaceSubAdminCmd
     - Replace sub-admin
     - set
   * - ``0x84``
     - QueryOrSetupUserIdLength132Cmd
     - Query/set user-ID length (132)
     - set/query
   * - ``0x85``
     - EBadgeRandom133Cmd
     - eBadge random challenge (133)
     - query
   * - ``0x86``
     - UnlockEBadge134Cmd
     - Unlock with eBadge (134)
     - set
   * - ``0x89``
     - EbadgeManagerCmd
     - eBadge management
     - set
   * - ``0x8B``
     - WelcomeMode139Cmd
     - Temporarily disable Welcome Mode (139)
     - set/query
   * - ``0x8C``
     - PeripheralModeCmd
     - Peripheral mode
     - set
   * - ``0x8E``
     - MultiUserAuthentication142Cmd / TwoFactorAuthentication142Cmd
     - Two-person / two-factor unlock (142)
     - set/query
   * - ``0x8F``
     - HostageAlarm143Cmd
     - Duress ("hostage") alarm code (143)
     - set
   * - ``0x90``
     - UserSensorList144Cmd
     - User duress-sensor list (144)
     - query
   * - ``0x91``
     - PairSensorInfoCmd
     - Paired-sensor info
     - query
   * - ``0x92``
     - UserSensorActivator146Cmd
     - User-sensor activator (146)
     - set
   * - ``0x93``
     - QueryPwd147Cmd
     - Read credential/password list from lock (147)
     - query
   * - ``0x94``
     - Log148Cmd
     - Read access log (148)
     - query
   * - ``0x95``
     - FaceEnrollmentCmd
     - Face image enrolment (149)
     - set
   * - ``0x97``
     - ScanWifiCmd / ScannerWifi151Cmd
     - Scan Wi-Fi networks (151)
     - query
   * - ``0x98``
     - SetWifiCmd / SetWifi152Cmd
     - Set Wi-Fi credentials (152)
     - set
   * - ``0x99``
     - ConfiguratorWiFi153Cmd
     - Wi-Fi AP configurator (153)
     - set
   * - ``0x9A``
     - PairGatewayCmd
     - Pair gateway/hub
     - set
   * - ``0x9B``
     - EnergySavingWelcomeModeCmd
     - Welcome Mode + energy-saving 8-slot schedule (155)
     - set/query
   * - ``0x9C``
     - AlarmLockCoverCmd
     - Key-cover tamper alarm
     - set
   * - ``0xA0``
     - FaceRecognitionSettingsCmd
     - Face-recognition enable/settings (160)
     - set
   * - ``0xA2``
     - LockLogReportCmd
     - Lock log report (162)
     - query/report
   * - ``0xA3``
     - UserPushSettings163Cmd
     - Per-user push settings (163)
     - set
   * - ``0xA4``
     - ScannerWifi164Cmd
     - Scan Wi-Fi (164)
     - query
   * - ``0xA7``
     - QueryPwd167Cmd
     - Read credential list (167, tenant-access)
     - query
   * - ``0xA8``
     - LockMoreSettingsCmd
     - Extra lock settings (child key, electronic lock)
     - set
   * - ``0xA9``
     - QueryClientIdCmd
     - Query client ID (169) — *Manager app*
     - query
   * - ``0xAA``
     - QueryLteConnectStatusCmd
     - Query LTE connection status (170) — *Manager app*
     - query
   * - ``0xAE``
     - ScanWiFiList174Cmd
     - Scan Wi-Fi list (174)
     - query
   * - ``0xAF``
     - SetDST175Cmd
     - Set daylight-saving time (175) — *Manager app*
     - set
   * - ``0xB6``
     - SetDoorbellModeCmd
     - Set doorbell mode — *Manager app*
     - set
   * - *AT string*
     - ReStartCmd
     - Nordic BLE-module restart (``AT+SRESTART``)
     - set
   * - *const*
     - ResetBLEModuleCmd
     - Reset the Nordic BLE module (``CMD_RESET_BLE_MODULE``)
     - set
   * - *var*
     - QueryPwdCmd
     - Read credential list (``"11"`` or named-query variant)
     - query
   * - *var*
     - PagingLogCmd
     - Paged access-log read (byte set per call)
     - query

Undetermined / notes
--------------------

- **OAC / OMK family** (``QueryShortOacCmd``, ``SetOMKCmd``, ``QueryOMKCmd``):
  the request byte is built from a constant (``CODE_GET_QUERY_NEW_OAC``,
  ``CMD_QUERY_OMK``) or ``"1"+type`` rather than a literal, so the exact byte in
  the ``0x1x`` range was not pinned down. ``SetOACCmd`` = ``0x1B`` and
  ``SetShortOACCmd`` = ``0x1E`` are confirmed.
- **OtherQueryCmd** uses ``CMD_LOCK_OTHER_QUERY`` (literal not resolved in
  ``MessageManage``); it is in the ``0x1x`` diagnostic range.
- **QueryPwdCmd / PagingLogCmd** choose their byte at runtime (``"11"`` /
  per-call), so no single byte applies.
- **ReStartCmd** is an ``AT+``-style Nordic UART string, not an AES frame.
- **UnlockCmd** (Manager app) is a thin state helper, not a frame builder; no
  ``cmd`` byte.
- Helper/base classes excluded: ``Cmd``, ``CmdPack``, ``AbstractSensorCmd``,
  ``GarbageCmd``, ``NordicAtCmd``, ``BaseOTACheckVer``, ``QueryPwdCmdF(Kt)``.
