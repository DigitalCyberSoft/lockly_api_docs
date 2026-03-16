Feature flags
=============

API endpoints
-------------

.. http:post:: user/isbeta

   Checks whether the user account has beta features enabled.

   :Request encryption: *User*
   :<json string acct: The user's account name.

   :>json boolean isBeta: Whether the user is in the beta program.

   **Example request**

   .. sourcecode:: json

      {
        "acct": "user@example.org"
      }

   **Example response**

   .. sourcecode:: json

      {
        "cod": "200",
        "isBeta": false
      }

.. http:post:: user/isbeta3

   Checks version 3 beta feature flags. Same request format as
   :http:post:`user/isbeta`.

   :Request encryption: *User*
   :<json string acct: The user's account name.

   :>json boolean isBeta: Whether the user has v3 beta features enabled.
