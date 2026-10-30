REST API encryption
===================

There are two main types of encryption used in the REST API. Both sit *on top of*
the TLS transport — Lockly adds a second application-layer cipher to selected
fields (chiefly ``para``, and the ``key`` field of the account query response).

.. note:: ✅ The keys and procedures on this page still match the current app
   (3.2.9 / 3.3.4). The public/private key pair below was confirmed byte-for-byte
   against the keys embedded in the current build; the RSA and 3DES procedures are
   the same. Worked code for all of this, validated on hardware, is in LocklyHA's
   ``api.py`` (:doc:`/CREDITS`).

Anonymous encryption
--------------------

*Anonymous* encryption is used to encrypt parts of API messages before the user encryption key is available.

Non-padded RSA (RSA-1024, "NoPadding") is used for *anonymous* encryption. The process for both encryption and decryption is as follows:

#. Split the message bytes into chunks (64 bytes for encryption, 128 bytes for decryption).
#. Encrypt or decrypt each chunk individually using the relevant key.
#. Concatenate the encrypted chunk data, and encode the result as base64.

.. note:: 🔎 In practice most *anonymous* payloads (e.g. the ``login`` and
   ``qrylknew`` ``para``) are a single sub-128-byte JSON string, so the "chunking"
   reduces to one block: left-zero-pad the UTF-8 bytes to 128, raw-RSA with the
   public key, base64-encode. Decryption of the server ``key`` field is the same in
   reverse with the private key, then strip leading ``NUL`` bytes. Because it is raw
   RSA with no OAEP/PKCS#1 padding, the plaintext must be shorter than the modulus.

Encryption key
^^^^^^^^^^^^^^

*PEM, X.509 public RSA*

.. sourcecode:: pem

   -----BEGIN PUBLIC KEY-----
   MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCZtiijnvRo5EEI0n2I7shxljMX
   b7mZ/FpjuS98MHGWuYYUrsiJQVgfPn29lmI/MDkhVc7oVTsg5BIyC0TUpZKTgxyF
   DZw08AdWKe9JZvzyGB00AGkRxcem2J64xJJ04o9FW6PDLF0gSvblZAvUdHU1YyfB
   7DgJhikP7lPrFNdGwwIDAQAB
   -----END PUBLIC KEY-----

Decryption key
^^^^^^^^^^^^^^

*PEM, PKCS#8 private RSA*

.. sourcecode:: pem

   -----BEGIN PRIVATE KEY-----
   MIICdQIBADANBgkqhkiG9w0BAQEFAASCAl8wggJbAgEAAoGBAMBZug0p9CRIsZI+
   o3rMj1dlKt7AE52Ql44dSgVvaTVZ3ZWB2vRpvA80cF/QQXVbODgaU3xD0ZTkeGY6
   EP3lQaxLwGbQC1xrfLl4rVJPBt2qk0EtSQt729rOYBzMJSp0r5fPMmVDPogp3neM
   lFhP2xFlkp+yy+hsbkvXmsT9kpZjAgMBAAECgYAy0cIBJlt1lqsrq1b/47nfakA4
   V+EW2RPhnUVoSDYwvUx46rURrDnefolOFzSkL/SbhgEWrMhboT1aLO8+VWrTCF3B
   L2BPK0+G0QGYh8l56qk0dyoJiAz6Qus4OSlypNO01VIZGhNfayYlPjVlrZtDRTZF
   1kPbnUjcUwEKsrHXcQJBAOZbj4zopmYTfB7xFsbyP/K7nMOREjANLilie1Fkl8RZ
   8xSRwdz6s7r1Vx3JuUZbwyyNMG27NO+tZgdvF0u3pskCQQDVwxYUyuF+iIH9Ia2q
   Q1c1Al5fIBBUY8o7BT4tviLpQEjL2lZeJBvlRRzCyiZZISR+KXq8Id4+OKVpix6F
   oC3LAkB9z0niannezAuBFqka9NmKJ38hrEyjo78vaRLyzB67ZWkGNekMWHvqwu3W
   XgLrc1hwL5hghdsOf8R2kOzHNMFJAkA7xh+olMrVbSqcNAyx7b63DgCBrR+j2Xu1
   YVPvyplMjDNO/bDlBkfepqLSPWDXz5K6zLKLZRUWZRSsHMDeMNpdAkB1CAvpgzVt
   /OYbGvUDDK9VFbKtprN0hyFxuaX/pYaQL8hz7l+wkSvAd6lQgNlW5qLfYog06XUe
   xrOFRvMjIhMm
   -----END PRIVATE KEY-----

User encryption
---------------

*User* encryption is used to encrypt parts of API messages after the user encryption key is available.

The Triple Data Encryption Algorithm (3DES) with PKCS#7 padding is used for *user* encryption.

The key used is (potentially) unique to each user.

3DES is used in **ECB mode with PKCS#7 padding**. The 24-byte key is derived from
the account query response (🔎):

.. sourcecode:: python

   # body["key"] is anonymous-RSA-encrypted; decrypt it to a 32-char ASCII string,
   server_key_str = rsa_decrypt_key(body["key"], priv_key)   # 32 ASCII chars
   des3_key       = base64.b64decode(server_key_str)[:24]    # 24-byte 3DES key

   def des3_encrypt(key, plaintext):                 # for the `para` field
       data = plaintext.encode("utf-8")
       pad  = 8 - (len(data) % 8)
       data += bytes([pad]) * pad                    # PKCS#7 to 8-byte boundary
       return base64.b64encode(DES3.new(key, DES3.MODE_ECB).encrypt(data)).decode()

The key is account-scoped and stable across sessions for the same account, so it
can be fetched once and cached.

.. tip:: The *user* encryption key can be obtained using the :doc:`account query API</rest/endpoints/query_account>`.

.. tip:: 3DES is a symmetric cipher. This makes reverse-engineering much of the Lockly app with a packet sniffer possible.

.. warning:: This 3DES key and the lock's master code together grant full control
   of a lock. Treat them like passwords — see :doc:`/methodology`.
