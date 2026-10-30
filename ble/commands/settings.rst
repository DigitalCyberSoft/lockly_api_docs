Lock settings and modes
=======================

Assorted lock configuration commands. 🔎 traced from app 3.3.4; most are
*identified* (byte + purpose) rather than fully decoded — see
:doc:`/reference/command_index` for the complete list. Settings travel on the
normal transport (:doc:`/reference/transports`), so they are generally settable
remotely.

Core settings
-------------

.. list-table::
   :header-rows: 1
   :widths: 40 18 42

   * - Command class
     - Byte
     - Purpose
   * - ``LockSettingsCmd`` / ``LockSettings2Cmd``
     - ``19``
     - bundle of toggles (two sub-commands, see below)
   * - ``LockMoreSettingsCmd``
     - ``A8``
     - child key, electronic lock
   * - ``SetAutoLockCmd``
     - ``12``
     - auto-lock timeout (seconds)
   * - ``SetTimeZoneCmd`` / ``SetDST175Cmd``
     - ``33`` / ``AE``
     - time zone / daylight saving
   * - ``LedStateCmd``
     - ``47``
     - status LED on/off
   * - ``SetAlarmCmd`` / ``AlarmLockCoverCmd``
     - — / ``9C``
     - tamper / key-cover alarm
   * - ``DoNotDisturbModeCmd``
     - ``5D``
     - Do-Not-Disturb schedule (quiet hours)
   * - ``DoorbellSoundSettingCmd``
     - ``5E``
     - doorbell sound
   * - ``SetLockModeCmd`` / ``MultipleVerification79Cmd``
     - ``4F``
     - unlock mode / multi-verification
   * - ``WorkModeCmd`` / ``LockMode88Cmd``
     - ``58``
     - work / lock mode
   * - ``CheckDoorSensorStateCmd`` / ``SetDoorSensorStateCmd``
     - ``32``
     - door-sensor state
   * - ``PeripheralModeCmd``
     - ``8C``
     - peripheral mode
   * - ``SetLockTypeCmd``
     - ``49``
     - lock type
   * - ``ResetLockAndReStartCmd``
     - ``10``
     - factory reset / restart

``0x19`` sub-commands (🔎):

- **sub 1**: Random Mode (shuffled on-screen keypad digits), key-press tone,
  alarm switch, auto-lock switch.
- **sub 2**: slide-to-open, Bluetooth voice, wired door-sensor presence, how the
  door closes, fingerprint-copy tone.
- **``0x0B``** sets the tamper-alarm level (1–3) — this is *not* the keypad
  lockout.

Security / duress
-----------------

- **``HostageAlarm143Cmd`` (``8F``)** — duress (hostage) alarm: a code that
  unlocks and silently raises an alert.
- **``TwoFactorAuthentication142Cmd`` / ``MultiUserAuthentication142Cmd``
  (``8E``)**, with ``4F`` / ``79`` — require two credentials, or two people, to
  open.

Safe Mode (keypad lockout) — read this
---------------------------------------

After too many wrong keypad attempts a lock enters **Safe Mode** (a timed
lockout). 🔎 **Neither the consumer app, Lockly Home, nor Lockly Manager exposes
any setting to disable it or change the attempt threshold or duration, and no
command for it exists in the code.** The threshold is almost certainly fixed in
the lock firmware.

What *is* available:

- Safe Mode is **observable**: it is logged as event ``104`` (enter) / ``105``
  (disable), lock-record open-types ``78``/``79``, and record types ``73``/``74``
  (:doc:`/mqtt/messages`, access-log commands ``7C``/``94``/``A2``). The hub
  ``cachedstatus`` ``sts`` integer defines a ``SECURE_MODE`` bit (``0x20``), 🧩
  though the app never reads it.
- A remote unlock 🧩 very likely still works while in Safe Mode (no error code
  suggests otherwise); whether it also *clears* Safe Mode is ⚠️ untested.
- **Rain Mode** (:doc:`rain_mode`) is the nearest real mitigation if a touch
  keypad is being triggered by weather or passers-by: it disables the keypad on a
  condition rather than locking out on failures.
