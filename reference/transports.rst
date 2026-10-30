Transports: how a command reaches the lock
==========================================

A BLE frame (:doc:`/ble/frame_format`) can reach a lock three ways. The app
chooses one per command in ``CmdManager.R(...)`` based on flags on the lock's
``BluetoothBean``. 🔎 traced from app 3.3.4. Understanding this explains most
"works in the app but my call fails" puzzles.

Selection logic
---------------

Simplified from ``CmdManager.R`` (non-"force-BLE" path):

#. **MQTT device channel** — if ``isSupportMqttConnect()`` (lock is bound to a
   Matter/PGH260 hub, or is Wi-Fi-native, or LTE). The frame is published as
   ``lockCommandRequest`` (:doc:`/mqtt/client_channel`). If the lock also supports
   both BLE and remote, the app may race BLE and MQTT.
#. **Hub relay** — else if ``isRemoteControl()`` (bound to a classic PGH200/220
   hub). The frame goes through :http:post:`senddata` (``HubBleBuilder``).
#. **Direct BLE** — else, over a GATT connection to the lock's MAC.

So which transports a lock offers depends on its hub generation:

.. list-table::
   :header-rows: 1
   :widths: 26 24 50

   * - Hub / lock
     - Transport
     - Notes
   * - PGH200 / PGH220 (Secure LINK)
     - ``senddata`` relay
     - **Not** on the MQTT device channel. The broker answers ``3005 device is
       offline`` for devices behind one.
   * - PGH260 (Matter)
     - MQTT device channel
     - ``senddata`` may return ``cod=930`` here — these locks are not REST-relay
       devices.
   * - Wi-Fi-native (Visage)
     - MQTT device channel
     - No hub; connects on its own.
   * - no hub / no Wi-Fi
     - direct BLE only
     - not reachable from the cloud at all

``BluetoothBean.isMatterHub()`` is simply ``hubId.startsWith("PGH260")``.

.. important::

   Build state-changing commands from a nonce + host password fetched over the
   **same** transport that will carry the command. Mixing transports yields a
   stale nonce and a lock-side rejection (BLE error ``F3``).

``cod`` error codes
-------------------

Returned in the ``cod`` field of REST responses (string or int — always compare
as ``str(cod) == "200"``). ✅/🔎 from LocklyHA and app strings.

======= =======================================================================
``cod``  Meaning
======= =======================================================================
``200``  success
``900``  hub-level system error (for ``cachedstatus``: hub firmware too old)
``901``  no lock found
``909``  server cannot parse request (``para`` missing or not DES3-encrypted)
``910``  ``para`` sent unencrypted
``920``  endpoint rejected the request (seen on ``lockly/syspara``)
``930``  hub/Secure LINK not associated with the lock — **or** the lock has no
         hub (Wi-Fi-native), so the hub-relay ``senddata`` cannot serve it. Use
         the MQTT channel instead.
``931``  Secure LINK already bound to another account
``932``  Secure LINK does not exist
``938``  Secure LINK ID coding-format error
``942``  MQTT timeout — hub received no BLE reply from the lock in time
         (transient; retry is safe)
``943``  hub is offline (the app falls back to direct Bluetooth)
``990``  general system error / poor network
======= =======================================================================

Lock-side rejections are separate: a short unencrypted ACK frame with CmdType
``0C`` and an error nibble ``F1``–``FF`` (``FF`` = wrong password, ``F3`` = stale
nonce). A ``cod=200`` says nothing about these — always parse the ACK.
