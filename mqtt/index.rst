MQTT API
========

There are **two different MQTT systems** in the Lockly world, and conflating them
is the single biggest trap in the original documentation:

#. **The hub ↔ Alibaba Cloud IoT link.** Each Wi-Fi hub is an Aliyun IoT device
   and connects to Aliyun using the ``iot*`` credentials in the lock data. This
   is the *hub's own* identity. :doc:`authentication` documents it — but see the
   warning there: a client must **not** connect with these credentials.

#. **The app ↔ Lockly broker link** (the "device channel"). This is how the app
   gets real-time push and how newer Matter hubs / Wi-Fi-native locks receive
   commands. It is a **Lockly-operated broker on AWS**, authenticated with your
   account e-mail and login token. :doc:`client_channel` documents it, and
   :doc:`messages` lists the message types.

.. warning::

   ✅/🧩 Do **not** connect a client to Aliyun IoT with the hub's ``iotdm`` /
   ``iotsecret`` / ``iotprodkey`` / ``iothost``. Those are the hub's device
   identity; using them kicks the hub off the broker and breaks the BLE relay.
   The original "Connecting to the MQTT broker" instructions describe this
   hub-identity link; they are kept for reference on :doc:`authentication` but are
   not the path an app or integration uses for push or commands.

.. toctree::
   :caption: General documentation
   :maxdepth: 2

   client_channel
   messages
   authentication
