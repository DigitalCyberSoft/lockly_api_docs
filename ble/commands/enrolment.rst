User enrolment: fingerprints, RFID, eBadge, face
=================================================

Adding a *person* (as opposed to a bare PIN) to a lock. 🔎 traced from apps
2.9.0 / 3.3.4 / Home 1.6.2. A key historical finding is recorded here because it
surprises integrators.

What can be done remotely
-------------------------

The restriction to Bluetooth is enforced in the **app's screens**, not by the
lock. Every credential command goes through the same transport router
(:doc:`/reference/transports`), which is perfectly capable of relaying enrolment
through a hub or MQTT.

================================ ========================= ==========================
Credential                        Remote (hub/MQTT)?        Notes
================================ ========================= ==========================
PIN codes (timed/recurring/      ✅ yes (pushed remotely)   best remote option today
resident)
Staff PINs                        ⚠️ removed from the app    see below
Fingerprints                      🧩 physically no / code    sensor needs a finger at
                                  path yes                   the lock regardless
RFID cards / eBadge               Bluetooth-only in app      card must be tapped locally
================================ ========================= ==========================

History: staff and Wi-Fi fingerprint enrolment were removed
-----------------------------------------------------------

🔎 Comparing versions:

- **2.9.0** had a Staff UI that called ``addStaffUser`` / ``createStaffLockPw``
  and sent staff PINs over the hub with no forced Bluetooth. It forced Bluetooth
  for fingerprint enrolment only on a couple of camera models; other models
  enrolled fingerprints over the hub.
- **3.3.4** removed the staff screens (the ``addStaffUser`` /
  ``createStaffLockPw`` endpoints still exist but have no callers) and now forces
  Bluetooth for fingerprint enrolment on **any** lock in remote mode.
- **Lockly Home 1.6.2** shows a "Bluetooth required — stand next to the lock"
  dialog.

🧩 Staff management appears to have moved to the Lockly Access Portal
(``authSpace/*`` workspace endpoints). A third-party client could likely still
drive fingerprint enrolment remotely by sending the same frames through
``senddata`` / MQTT, but a person must still touch the sensor.

Enrolment commands
------------------

.. list-table::
   :header-rows: 1
   :widths: 45 20 35

   * - Command class(es)
     - Byte
     - Purpose
   * - ``StartSensorCmd`` / ``StopSensorCmd``
     - ``14`` / ``17``
     - begin / end fingerprint capture
   * - ``QuerySensorCmd`` / ``DeleteSensorCmd``
     - ``15`` / ``16``
     - query / delete fingerprint
   * - ``FingerprintCmd``
     - ``3B``
     - fingerprint operation
   * - ``NewSensorCmd`` / ``NewDeleteSensorCmd``
     - ``3C`` / ``3E``
     - newer fingerprint add / delete
   * - ``StartSensorWithUserNoCmd``
     - ``4A``
     - enrol fingerprint for a user slot
   * - ``UpdateFingerprintCodeCmd``
     - ``5C``
     - update fingerprint→code mapping
   * - ``FaceEnrollmentCmd``
     - ``95``
     - Visage face enrolment
   * - ``FaceRecognitionSettingsCmd``
     - ``A0``
     - face recognition settings
   * - ``DeleteRfInfoCmd``
     - ``80``
     - delete RFID info
   * - ``EBadgeRandom133Cmd`` / ``UnlockEBadge134Cmd``
     - ``85`` / ``86``
     - eBadge challenge / unlock
   * - ``EbadgeManagerCmd``
     - ``89``
     - eBadge management
   * - ``ImportUser126Cmd``
     - ``7E``
     - bulk user import
   * - ``ReplaceSubAdminCmd``
     - ``83``
     - replace the sub-admin
   * - ``UserRoomNumberCmd``
     - ``60``
     - per-user room number (rentals)

Cloud side: ``fingerprint/save``, ``du/save``, ``du/batchUpdateFpCodes``,
``getFingerprintList``, ``crdntl/fpt/add``, ``crdntl/rfid/add``,
``crdntl/ebadge/add``, ``crdntl/face/add``.
