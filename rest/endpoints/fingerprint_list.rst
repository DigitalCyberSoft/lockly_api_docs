Fingerprint list
================

API endpoints
-------------

.. http:post:: getFingerprintList

   Retrieves the list of users associated with fingerprint access on a lock.

   The response contains a user-encrypted ``usrarr`` field (the same
   user array format used in the :http:any:`door lock <door_lock>` object).
   It must be decrypted with the user encryption key before parsing.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json user-encrypted base64 usrarr: Encrypted user array (same format as ``door_lock.usrarr``).

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
        "usrarr": "T2VieHV2YzdFZVQ0bUtTRTk3ZEcyQT09"
      }

   **Decrypted ``usrarr`` example**

   After decrypting with the user key, the array matches the ``usrarr``
   format in the :http:any:`door lock <door_lock>` object:

   .. sourcecode:: json

      [
        {
          "dutype": "F",
          "pid": 1,
          "fn": "John",
          "ekeyType": "",
          "ln": "Doe",
          "subadm": "N",
          "oacpriv": "N",
          "fpId": "fp001"
        }
      ]
