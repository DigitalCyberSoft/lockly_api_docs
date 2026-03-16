E-key list
==========

API endpoints
-------------

.. http:post:: getEkeyList

   Retrieves access entries (e-keys) assigned to a lock.

   E-keys represent all access methods: permanent users (type ``V``),
   master codes (type ``M``), timed access (type ``T``), and others.
   Each entry may include encrypted temporary passwords (``tempPwd``,
   ``tempPwd2``) and time-window constraints.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json list ekeyList: A list of e-key objects.

   **E-key object fields**

   :>json int mediumId: Unique access entry identifier.
   :>json string deviceId: The door lock identifier.
   :>json string firstName: User's first name.
   :>json string lastName: User's last name.
   :>json string newName: Display name.
   :>json string userAcct: User's account email.
   :>json int userId: User identifier.
   :>json string ekeyType: E-key type (may be empty).
   :>json string password: Access code (for timed/OAC entries).
   :>json int pwdId: Password slot identifier.
   :>json string status: E-key status (``I`` = active/invited).
   :>json string type: Access type — ``V`` (permanent), ``M`` (master), ``T`` (timed).
   :>json string token: Token string associated with the e-key.
   :>json string tempPwd: Encrypted temporary password (user-encrypted).
   :>json string tempPwd2: Secondary encrypted temporary password.
   :>json object startDate: Start of access window (Java Date object with ``time`` in ms).
   :>json object endDate: End of access window (Java Date object with ``time`` in ms).
   :>json int startDateTamps: Start timestamp in milliseconds.
   :>json int endDateTamps: End timestamp in milliseconds.
   :>json object createdDate: Creation timestamp (Java Date object).
   :>json object updatedDate: Last update timestamp (Java Date object, may be null).

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
        "ekeyList": [
          {
            "mediumId": 12345,
            "deviceId": "300030001234567890123456",
            "firstName": "Jane",
            "lastName": "Smith",
            "newName": "Jane Smith",
            "userAcct": "jane@example.com",
            "userId": 100,
            "ekeyType": "",
            "password": "",
            "pwdId": 0,
            "status": "I",
            "type": "V",
            "token": "ABC123XY",
            "role": "",
            "imageUrl": "",
            "isAddType": "Y",
            "tempPwd": "...",
            "tempPwd2": "...",
            "ref": "",
            "startDate": null,
            "endDate": null,
            "startDateTamps": 0,
            "endDateTamps": 0,
            "startTimes": 0,
            "endTimes": 0,
            "createdDate": {
              "time": 1748486840000,
              "date": 29,
              "day": 4,
              "hours": 2,
              "minutes": 47,
              "month": 4,
              "seconds": 20,
              "timezoneOffset": 0,
              "year": 125
            },
            "updatedDate": null
          }
        ]
      }
