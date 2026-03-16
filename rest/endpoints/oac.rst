One-time access codes
=====================

API endpoints
-------------

.. http:post:: oac/get

   Retrieves one-time access code (OAC) data for a lock.

   OACs enable offline lock access without an internet connection. The server
   returns code arrays in both legacy (``oac``) and new (``oacnew``) formats.
   The client uses these to generate time-limited access codes locally, which
   can be shared with guests and entered on the lock's keypad.

   :Request encryption: *User*
   :<json string acct: The user's account name.
   :<json string dv: The door lock identifier. See also: :http:post:`qrylknew`.

   :>json object oac: Legacy OAC data.
   :>json object oacnew: New OAC data format.

   **Legacy OAC (``oac``) fields**

   Code arrays (``codeA``, ``codeList``) contain indexed objects with
   ``idx`` (position) and ``obj`` (code string) fields.

   :>json list codeA: Array of ``{idx, obj}`` 4-digit code pairs.
   :>json string codeB: 8-digit code parameter.
   :>json string codeC: 3-digit code parameter.
   :>json int codeD: Integer code parameter.
   :>json int codeE: Integer code parameter.
   :>json int codeF: Integer code parameter.
   :>json list codeList: Array of ``{idx, obj}`` 10-digit permutation codes.
   :>json int pairDate: Timestamp (milliseconds since epoch) of lock pairing.
   :>json string pairTimeZone: The lock's time zone offset.

   **New OAC (``oacnew``) fields**

   Uses ``{i, o}`` indexed entries instead of ``{idx, obj}``.

   :>json list listA: Array of ``{i, o}`` 2-digit code entries.
   :>json string codeB: 8-digit code parameter.
   :>json string codeC: 3-digit code parameter.

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
        "oac": {
          "codeA": [
            {"idx": 0, "obj": "0917"},
            {"idx": 1, "obj": "2904"}
          ],
          "codeB": "41251560",
          "codeC": "657",
          "codeD": 8,
          "codeE": 4,
          "codeF": 4,
          "codeList": [
            {"idx": 0, "obj": "5493861072"},
            {"idx": 1, "obj": "5607982134"}
          ],
          "pairDate": 1696643022192,
          "pairTimeZone": "-7:00"
        },
        "oacnew": {
          "listA": [
            {"i": 0, "o": "04"},
            {"i": 1, "o": "25"}
          ],
          "codeB": "41251560",
          "codeC": "657"
        }
      }
