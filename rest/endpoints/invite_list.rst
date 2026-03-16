Shared access list
==================

API endpoints
-------------

.. http:post:: admin/invite/list

   Retrieves shared access entries for a lock.

   Returns a list of users who have been granted shared access to the
   lock by the admin. The response key is ``sharedList``.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json list sharedList: A list of shared access objects.

   **Shared access object fields**

   :>json int mediumId: Unique shared access identifier.
   :>json string deviceId: The door lock identifier.
   :>json string firstName: User's first name.
   :>json string lastName: User's last name.
   :>json string userAcct: User's account email.
   :>json int userId: User identifier.
   :>json string status: Access status (e.g. ``A`` = active).
   :>json string type: Access type.
   :>json string role: Permission role (e.g. ``USER``).

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
        "sharedList": []
      }
