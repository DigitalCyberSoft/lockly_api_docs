Backup e-keys
=============

API endpoints
-------------

.. http:get:: backup/ekeyOrEbadge

   Retrieves backup e-keys and e-badges for a lock.

   Unlike most Lockly endpoints, this uses a GET request with query
   parameters and no encryption.

   :Request encryption: *None*
   :query string acct: The user's account name.
   :query string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json list ekeyList: Backup e-key entries.
   :>json list ebadgeList: Backup e-badge entries.

   **Example request**

   .. sourcecode:: text

      GET /pgsmtlkv2/api/backup/ekeyOrEbadge?acct=user@example.org&dv=300030001234567890123456

   **Example response**

   .. sourcecode:: json

      {
        "cod": "200",
        "ekeyList": [],
        "ebadgeList": []
      }
