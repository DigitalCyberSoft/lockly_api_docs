The hub's Aliyun IoT link
=========================

.. warning::

   This page describes the **hub's own** connection to Alibaba Cloud IoT. It is
   documented for completeness. **A client/integration must not connect with
   these credentials** — doing so impersonates the hub and knocks it offline,
   breaking the BLE relay. For app-style real-time push and commands, use the
   Lockly device channel instead: :doc:`client_channel`.

Obtaining MQTT details
----------------------

The MQTT details for each Wi-Fi hub can be found in the :http:any:`door_lock` data.

Specifically, the following fields are used:

- ``iotprodkey``: The Wi-Fi hub's IoT device management product key
- ``iotdm``: The Wi-Fi hub's IoT device management name
- ``iotsecret`` The Wi-Fi hub's IoT device management secret
- ``iothost``: The MQTT broker host (``{iodprodkey}.iot-as-mqtt.cn-shanghai.aliyuncs.com`` if unprovided)

Authenticating with the MQTT broker
-----------------------------------

The `Alibaba Cloud IoT Platform documentation <https://www.alibabacloud.com/help/en/iot-platform/latest/establish-mqtt-connections-over-tcp>`_ describes the MQTT credential format.

================= ============== ===============
Alibaba parameter Lockly vaue    Customizable
================= ============== ===============
securemode        ``"2"``        Yes
signmethod        ``"hmacsha1"`` Yes
deviceName        ``iotdm``      No
productKey        ``iotprodkey`` No
deviceSecret      ``iotsecret``  No
================= ============== ===============

The **mqttUsername** is used as the **clientId**.
