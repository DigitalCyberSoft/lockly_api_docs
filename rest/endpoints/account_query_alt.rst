Account query (alternative)
===========================

API endpoints
-------------

.. http:post:: getUserInfoAndDvList

   A lighter alternative to :http:post:`qrylknew` that returns the same
   core data: locks, user encryption key, and account info.

   The response format is identical to :http:post:`qrylknew` — encrypted
   door lock objects in ``dl``, anonymous-encrypted user key in ``key``.

   :Request encryption: *Anonymous*
   :<json string acct: The user's account name.

   :>json string fn: The user's first name.
   :>json string ln: The user's last name.
   :>json list of user-encrypted base64 of door lock object dl: A list of the user's :http:any:`door lock <door_lock>` s.
   :>json anonymous-encrypted base64 key: The user's 3DES encryption key.

   **Example request**

   .. sourcecode:: json

      {
        "acct": "user@example.org"
      }

   **Example response**

   .. sourcecode:: json

      {
        "cod": "200",
        "fn": "John",
        "ln": "Doe",
        "dl": [
          "ZW5jcnlwdGVkX2Rvb3JfbG9ja19kYXRhX2Jhc2U2NA=="
        ],
        "key": "ZW5jcnlwdGVkX3VzZXJfa2V5X2Jhc2U2NA==",
        "uuid": "2a47c50c658c44a0bc123082d9bb3673",
        "zone": "61",
        "pr": []
      }
