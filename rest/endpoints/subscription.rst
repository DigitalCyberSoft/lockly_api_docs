Subscription status
===================

API endpoints
-------------

.. http:post:: check/isPay

   Checks the subscription/payment status for a lock.

   Some Lockly features (e.g. cloud recording, advanced notifications)
   require an active subscription.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json boolean isPay: Whether the lock has an active subscription.
   :>json int paymentType: Payment type identifier.
   :>json string expireDate: Subscription expiration date.

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
        "isPay": true,
        "paymentType": 1,
        "expireDate": "2027-01-01"
      }
