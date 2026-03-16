Device configuration
====================

API endpoints
-------------

.. http:post:: get/deviceConfigInfo

   Retrieves the camera and detection configuration for a lock.

   Applicable to Vision models and locks with camera capabilities.
   Returns detection scheduling (up to 4 time periods), detection distance,
   audio detection, recording duration, and HD settings.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json string deviceId: The door lock identifier.
   :>json object decfg: Detection configuration object.

   **Detection configuration (``decfg``) fields**

   The primary detection period is defined by the fields without a numeric
   suffix. Up to three additional periods can be configured (suffix ``1``
   through ``3``). The ``detectionPeriodWeek`` field is a 7-bit bitmask
   (0–127) where each bit represents a day of the week.

   :>json int detectionPeriodBeginHour: Start hour (0–23).
   :>json int detectionPeriodBeginMinute: Start minute (0–59).
   :>json int detectionPeriodEndHour: End hour (0–24).
   :>json int detectionPeriodEndMinute: End minute (0–59).
   :>json int detectionPeriodWeek: Day-of-week bitmask (127 = every day).
   :>json int detectionAudio: Audio detection enabled (0 = off, 1 = on).
   :>json int detectionDistance: Detection distance level (e.g. 2).
   :>json int recordDuration: Recording duration in seconds per event.
   :>json int switchHd: HD video enabled (0 = off, 1 = on).

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
        "deviceId": "300030001234567890123456",
        "decfg": {
          "detectionPeriodBeginHour": 0,
          "detectionPeriodBeginMinute": 0,
          "detectionPeriodEndHour": 24,
          "detectionPeriodEndMinute": 0,
          "detectionPeriodWeek": 127,
          "detectionPeriodBeginHour1": 0,
          "detectionPeriodBeginMinute1": 0,
          "detectionPeriodEndHour1": 0,
          "detectionPeriodEndMinute1": 0,
          "detectionPeriodWeek1": 0,
          "detectionPeriodBeginHour2": 0,
          "detectionPeriodBeginMinute2": 0,
          "detectionPeriodEndHour2": 0,
          "detectionPeriodEndMinute2": 0,
          "detectionPeriodWeek2": 0,
          "detectionPeriodBeginHour3": 0,
          "detectionPeriodBeginMinute3": 0,
          "detectionPeriodEndHour3": 0,
          "detectionPeriodEndMinute3": 0,
          "detectionPeriodWeek3": 0,
          "detectionAudio": 0,
          "detectionDistance": 2,
          "recordDuration": 15,
          "switchHd": 1
        }
      }
