Unofficial Lockly API documentation
===================================

Welcome to the Unofficial Lockly API documentation!

This is an ongoing effort to document the various `Lockly <https://lockly.com.au>`_ APIs, with the goal of
enabling the development of projects such as:

- An alternative, cross-platform app capable of using both Wi-Fi and Bluetooth to
  communicate with locks
- A `Home Assistant <https://www.home-assistant.io>`_ integration
- Command-line tooling for owners who want to script their own locks

This community fork extends the `original project by hacker1024
<https://github.com/hacker1024/lockly_api_docs>`_ with:

- the **Bluetooth command layer** — frame format, AES payload encryption, CRC,
  and per-feature command pages (unlock/lock, status, Welcome Mode, Rain Mode,
  offline access codes, firmware/OTA, enrolment, and more);
- the **MQTT device channel** — corrected broker and authentication notes, topics,
  and message types;
- a complete **index of every BLE command and REST endpoint** observed in the apps;
- endpoint pages merged from `bdmartin's fork
  <https://github.com/bdmartin/lockly_api_docs>`_.

Much of the new protocol detail is adapted, with thanks, from the hardware-validated
notes in `Forcky's LocklyHA <https://github.com/Forcky/LocklyHA>`_ (MIT).

Status markers
--------------

Every non-trivial claim is tagged ✅ verified on hardware, 🔎 traced from app
code, 🧩 inferred, or ⚠️ unknown. See ``methodology.rst``.

Building
--------

.. code-block:: console

   $ pip install -r requirements.txt
   $ make html        # output in _build/html

Licence
-------

New material is **CC BY 4.0** (``LICENSE``). Text inherited from the original
repository carries no licence; material adapted from LocklyHA remains MIT. See
``CREDITS.rst``.

**Unofficial.** Not affiliated with or endorsed by Lockly Security Inc.
