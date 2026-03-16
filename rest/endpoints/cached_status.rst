Cached lock status
==================

API endpoints
-------------

.. http:post:: lock/cachedstatus/get

   Retrieves the server-side cached lock status from the Wi-Fi hub's
   last report.

   .. warning:: Only available for locks with a Wi-Fi hub. Vision models
      without a hub will receive error 932.

   The hub periodically reports lock state to the Lockly server. This
   endpoint returns the most recent cached state, including lock status,
   door sensor presence and state, and low battery flag.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json object data: Cached status data.

   **Data object fields**

   :>json string addr: Hub MAC address.
   :>json int sts: Status bitmask (see below).
   :>json int time: Timestamp of the last hub report.

   **Status bitmask (``sts``)**

   .. list-table::
      :header-rows: 1

      * - Bit
        - Mask
        - Meaning
      * - 0
        - ``0x01``
        - Lock status (0 = locked, 1 = unlocked — **inverted**)
      * - 1
        - ``0x02``
        - Has wired door sensor
      * - 2
        - ``0x04``
        - Wired door sensor status (1 = open)
      * - 3
        - ``0x08``
        - Has wireless door sensor
      * - 4
        - ``0x10``
        - Wireless door sensor status (1 = open)
      * - 5
        - ``0x20``
        - Secure mode
      * - 6
        - ``0x40``
        - Secure lock
      * - 7
        - ``0x80``
        - Low battery

   **Example request**

   .. sourcecode:: json

      {
        "acct": "user@example.org",
        "dv": "300030001234567890123456"
      }

   **Example response**

   .. sourcecode:: json

      {
        "cod": "200",
        "data": {
          "addr": "AA:BB:CC:DD:EE:FF",
          "sts": 129,
          "time": 1710500000
        }
      }
