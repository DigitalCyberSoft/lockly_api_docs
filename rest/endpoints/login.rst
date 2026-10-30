Login
=====

API endpoints
-------------

.. http:post:: login

   Authenticates user credentials and provides a bearer token in the
   ``Authorization`` response **header**.

   :Request encryption: *Anonymous*
   :<json string acct: The user's account name (e-mail).
   :<json string pw: The user's password, hashed with SHA-256 (lowercase hex).

   :>header Authorization: ``Bearer <jwt>`` — the token for subsequent requests.

   .. note::

      ✅ The field inside the RSA-encrypted ``para`` is ``pw``, **not**
      ``password`` as the original 2.3.7 docs stated (confirmed against the
      current app and LocklyHA). ``login`` does not carry the common body;
      ``para`` is ``RSA_encrypt({"acct": email, "pw": sha256hex(password)})``.

   .. note::

      🔎 The JWT is returned in the HTTP **Authorization response header**, not in
      the JSON body (the body is just ``{"cod": "200"}``). Any authenticated
      response also carries a refreshed header, which the app's
      ``TokenRenewInterceptor`` stores. Token lifetime is 24 h
      (``exp - iat = 86400``); on expiry the server returns a non-200 ``cod`` (and
      the app also treats HTTP 401/403 as expiry). Re-call :http:post:`login`, or
      use :http:post:`refresh`.

   **Example request** (contents of ``para`` before RSA encryption)

   .. sourcecode:: json

      {
        "acct": "user@example.org",
        "pw": "766ef939879dc062af1cfe7bfc46f1af99a40a3926f185aee4b0801e34697c70"
      }

   **Example response**

   .. sourcecode:: text

      HTTP/1.1 200 OK
      Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

      {"cod": "200"}

.. http:post:: refresh

   Exchanges a still-valid (or recently expired) token for a fresh one. 🔎

   :Request encryption: *None* (common body only, no ``para``)
   :<header Authorization: ``Bearer <old_jwt>``
   :>header Authorization: ``Bearer <new_jwt>`` (same mechanism as ``login``)

   The app hits this transparently via its token interceptor, but simply
   re-calling :http:post:`login` on any non-200 ``cod`` also works.
