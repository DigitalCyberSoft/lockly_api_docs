Rain Mode (``56``)
==================

Rain Mode switches the keypad (or fingerprint reader) **off when the lock detects
rain**, "to avoid false triggering", and restores it on the next unlock / button
press / doorbell. It is the closest thing Lockly offers to "stop the keypad
reacting to things that aren't a real entry" — useful for a touchscreen lock in a
shared or exposed location. 🔎 traced from app 3.3.4.

Command
-------

.. sourcecode:: text

   56  <mc_len>  <enc_mc>  <action>  <state>

- **action**: ``1`` set, ``2`` query.
- **state**: ``1`` on, ``0`` off (the app sends ``Z2(1, isChecked ? 1 : 0)``).

Response (``0A56``): first byte is the state; ``isOn()`` ⇔ byte == ``1``.

Sent via the normal transport router (``CmdManager``), so it is settable through
a hub or MQTT, not only over Bluetooth.

Availability
------------

Gated by ``isSupportRainModeSetting()``. Models include **PGD728F (≥1.02.69)**,
PGD829AF (≥3.03.27), **PGD628F (≥1.02.45)**, PGD628FN (≥1.02.52), and more; the
Lockly Manager app adds description variants for PGK798HK, PGD899*, PGD898* and
screenless PGD7Y*/PGD7A*.

.. note::

   Both the consumer and Manager apps have this toggle, but the consumer app only
   shows it to the lock owner (``isSupportRainModeSetting() && y5()``); the
   Manager app drops the ``y5()`` permission check, which is 🧩 why it is more
   visible there.
