The Lockly device channel (app ↔ broker)
========================================

This is the MQTT link the **app** uses — for real-time state push, and as a
*second command transport* independent of ``senddata``. It is how newer
Matter hubs (PGH260) and Wi-Fi-native locks are driven, and it is the reason some
accounts get ``cod=930`` from ``senddata`` while their app works fine.

🔎/✅ Adapted from LocklyHA, which verified lock/unlock over this channel on a
PGD728FN behind a PGH260. See :doc:`/CREDITS`.

Broker and authentication
-------------------------

A **Lockly-operated broker on AWS** (not Aliyun), MQTT over TLS on port 8883. The
host is baked into the app (``PgConfig``), e.g.::

   ssl://mqttuswest02-lb-001-<...>.elb.us-west-2.amazonaws.com:8883

.. list-table::
   :header-rows: 1
   :widths: 22 78

   * - MQTT field
     - Value
   * - ``client_id``
     - a random UUID, generated fresh at startup (chosen by the client, not
       assigned by the server)
   * - ``username``
     - the account e-mail, **lowercased**
   * - ``password``
     - the login JWT (without the ``Bearer`` prefix)

.. warning::

   ✅ The username **must be lowercased** (the app does
   ``name.toLowerCase(Locale.ROOT)``). The REST API is case-insensitive, so a
   mixed-case e-mail logs in and looks healthy everywhere *except* here, where it
   produces a bare ``rc=5`` at CONNECT. The JWT also expires in 24 h; renew it
   before reconnecting (``refresh``). An ``rc=5`` should **not** be
   retried in a tight loop — paho's auto-reconnect will hammer the broker; log in
   again for a fresh token and back off.

Topics
------

.. list-table::
   :header-rows: 1
   :widths: 22 20 58

   * - Topic
     - Direction
     - Notes
   * - ``server``
     - client → broker
     - **publish only.** The app never subscribes; a ``SUBACK 0x80`` on it is
       expected and harmless.
   * - ``client/<id>``
     - broker → client
     - replies and state callbacks. The broker holds a server-side subscription —
       you receive here **without** issuing a SUBSCRIBE.

.. note::

   The long-standing "push is impossible" conclusion was wrong: the mistake was
   subscribing to ``server``. Command replies and the resulting state *do* arrive
   on ``client/<id>``. However, **unsolicited** external changes (keypad, app,
   Matter) arrive as ``deviceStateCallback`` only for a client id registered for
   push via Lockly's Firebase/AIPN service, which needs a real FCM token from a
   genuine app install. So a third-party client gets **command confirmation** but
   not **unsolicited push** of outside changes.

Sending a command
-----------------

Publish to ``server`` (``LockCommandController.sendCommand``):

.. sourcecode:: json

   {
     "header":  {"namespace": "com.lockly", "name": "lockCommandRequest",
                 "requestId": "<uuid>", "timestamp": 1788496170204},
     "payload": {"deviceId": "<lock uuid>", "commandName": "forward",
                 "commandContent": "<base64 of the same BLE frame senddata carries>"}
   }

``commandName`` is ``"forward"`` — the server relays the BLE frame without
interpreting it, exactly as ``senddata`` does. The reply arrives on
``client/<id>`` as ``lockCommandResponse``, or as an ``exception`` with a code
(``3005`` = ``device is offline``: the hub is not on this channel — a PGH220 on
old firmware is not).

.. important::

   Build the command from a nonce and host password fetched over the **same**
   transport. On a ``cod=930`` account ``senddata`` also refuses the status and
   credential queries, and a command built from a stale nonce is rejected by the
   lock (BLE error ``F3``).
