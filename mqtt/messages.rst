Device-channel message types
=============================

Messages on the device channel are JSON objects identified by ``header.name``.
🔎/✅ from LocklyHA and app tracing.

Incoming (broker → ``client/<id>``)
-----------------------------------

================================= ====================================================
``header.name``                    Meaning
================================= ====================================================
``deviceStateCallback``            lock / door state changed (see below)
``lockCommandResponse``            reply to a ``lockCommandRequest``
``lockEventLogQueryResponse``      access-log event, delivered in real time
``firmwareUpgradeProgress``        OTA progress (see :doc:`/ble/commands/firmware`)
``firmwareUpgradeFailure``         OTA failed
``deviceInfoResponse``             radio diagnostics reply (PGH260): BLE RSSI, Wi-Fi, fw
``bindHubAndLockResponse`` /
``unbindHubAndLockResponse``       hub ↔ lock binding results
``hubCommandResponse``             reply to a ``hubCommandRequest``
``exception``                      error, with a code (e.g. ``3005`` device offline)
================================= ====================================================

Outgoing (client → ``server``)
------------------------------

================================= ====================================================
``header.name``                    Meaning
================================= ====================================================
``lockCommandRequest``             relay a BLE frame to a lock (``commandName:"forward"``)
``hubCommandRequest``              command to a hub
``firmwareUpgradeRequest``         start an OTA (``type``: ``MULTIPLE`` lock, ``HUB_WIFI`` hub)
``lockEventLogQueryRequest``       request access-log events
``deviceInfoRequest``              request radio diagnostics (PGH260 only)
``bindHubAndLockRequest`` /
``unbindHubAndLockRequest``        bind / unbind a lock to a hub
================================= ====================================================

``deviceStateCallback`` format
------------------------------

.. sourcecode:: json

   {
     "header": {"name": "deviceStateCallback"},
     "items": [
       {
         "deviceId": "2d0023003030471333363838",
         "states": [
           {"statusKey": "LOCKED_STATUS", "statusValue": "0"},
           {"statusKey": "MAGNET",        "statusValue": "0"}
         ]
       }
     ]
   }

============================ ==========================================
``statusKey``                 ``statusValue``
============================ ==========================================
``LOCKED_STATUS``             ``"0"`` unlocked, ``"1"`` locked
``MAGNET``                    ``"0"`` door closed, ``"1"`` door open
============================ ==========================================

.. note::

   🧩 Safe Mode enter/exit surfaces through the access log (events ``104`` /
   ``105``), which can be delivered here as ``lockEventLogQueryResponse`` — the
   basis for *detecting* a keypad lockout remotely even though it cannot be
   configured (:doc:`/ble/commands/settings`).
