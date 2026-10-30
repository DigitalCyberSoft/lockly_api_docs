Bluetooth communication
=======================

This page documents the REST endpoints that **relay a BLE frame through a Wi-Fi
hub**. The frame carried in the ``cmd`` field is the subject of the entire
:doc:`/ble/index` section — see :doc:`/ble/frame_format` for how to build it, and
:doc:`/reference/transports` for when a hub relay is used versus the MQTT device
channel or a direct Bluetooth connection.

.. note::

   🔎 The app's primary relay endpoint is :http:post:`senddata` (a *synchronous*
   call that returns the lock's ACK frame). ``asyncSend`` is the asynchronous
   variant, documented first historically; its request body is the same but the
   lock's reply arrives via MQTT rather than in the HTTP response. New clients
   should prefer :http:post:`senddata`.

API endpoints
-------------

.. http:post:: senddata

   Relays a BLE frame to the lock through its hub and returns the lock's ACK
   frame synchronously. ✅ (verified by LocklyHA on PGD628FN + PGH220)

   :Request encryption: *User* (3DES ``para``); the ``cmd`` payload is separately AES-encrypted — see :doc:`/ble/aes_payload`.
   :<json string acct: The user's account name.
   :<json string cmd: The BLE frame, as an AES-encrypted hex string.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.
   :<json string mdna: The Wi-Fi hub's IoT device management name (``iotdm``). See also: :http:post:`qrylknew`.
   :<json string directive: Optional hint (``"unlock"`` / ``"lock"``); omit for a plain query.

   :>json string cod: ``"200"`` on relay success. **Note:** this reports only that
     the hub accepted the relay — the *lock's* result is inside the returned ACK
     frame. See the error table in :doc:`/reference/transports` (e.g. ``930`` =
     lock not bound to this hub / Wi-Fi-native lock with no hub; ``942`` = hub got
     no BLE reply in time; ``943`` = hub offline).
   :>json ACK frame: the lock's response frame (parse per :doc:`/ble/frame_format`).

   .. warning::

      ``authSpace/senddata`` is the Lockly Access Portal (workspace) variant of the
      same call.

.. http:post:: asyncSend

   Asynchronous relay. Sends a raw Bluetooth Low Energy packet to the lock via the Wi-Fi hub; the reply is delivered over MQTT rather than in the HTTP response.

   .. tip:: Many of the actions done by the Lockly app over Wi-Fi are implemented through the use of this endpoint.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string cmd: The BLE packet, in a hexadecimal encrypted form.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.
   :<json string mdna: The Wi-Fi hub's IoT device management name. See also: :http:post:`qrylknew`.

   :>json string req_msg_id: The request message ID. Used in MQTT messages.

   **Example request**

   .. sourcecode:: json

      {
        "acct": "user@example.org",
        "cmd": "aa00bb11cc22dd33ee44ff55aa00bb11cc22dd33ee44ff55aa00bb11cc22dd33ee44ff55aa00bb11",
        "directive": "lock",
        "dv": "300030001234567890123456",
        "mdna": "M2T200112233"
      }

   **Example response**

   .. sourcecode:: json

      {
        "cod": "200",
        "req_msg_id": 1590073500295600300
      }
