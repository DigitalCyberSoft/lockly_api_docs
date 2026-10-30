Access codes: PINs, OAC and OMK
===============================

Lockly has several kinds of keypad credential. They split into **online** codes
(created in the cloud and pushed to the lock) and **offline access codes (OAC)**
(generated on the phone from seeds, usable with no connection to the lock at
all). 🔎 traced from app 3.3.4 unless marked.

PIN credentials (online)
------------------------

Set/delete a code in a slot, optionally time-limited. These push fine over a hub
or MQTT (verified remotely for timed/recurring/resident codes — see
:doc:`enrolment`).

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Command class
     - Byte
     - Purpose
   * - ``SetHostPwdCmd`` / ``SetPwdWithUserNoCmd``
     - ``4B``
     - set host / per-user PIN
   * - ``SetPeriodicPwdCmd``
     - ``4B``
     - set a recurring time-limited PIN
   * - ``SetGuestPwdCmd``
     - ``54``
     - set a guest PIN
   * - ``DeleteGuestPwdCmd`` / ``DeleteWithUserNoCmd``
     - ``4D``
     - delete a PIN (guest / by user no.)
   * - ``QueryUserListCmd``
     - ``50``
     - list users / slots
   * - ``QueryUserDetailCmd``
     - ``51``
     - per-user detail
   * - ``QueryMultiPwdCmd``
     - ``70``
     - query multiple PIN slots
   * - ``QueryPwd147Cmd``
     - ``93``
     - read a credential (incl. host slot 0)
   * - ``QueryOrSetupUserIdLength132Cmd``
     - ``84``
     - get / set user-ID length

Cloud side: ``acu/save``, ``crdntl/pw/add``,
``crdntl/pw/update``, ``crdntl/pwList/active``, ``acu/delete``.

Offline Access Codes (OAC)
--------------------------

OAC lets a guest enter a **time-limited or one-time code** that the lock accepts
with no network link — the lock and the app share a secret seed set, and both
derive the same rolling codes independently.

- **Seeds** come from the cloud once, via ``oac/get`` (legacy ``oac``
  object and newer ``oacnew`` object; fields ``codeA``/``codeB``/``codeC``,
  ``codeList``, ``pairDate``, ``listA`` …). See the :doc:`endpoint page
  </rest/endpoints/oac>`.
- **Generation is local**, in ``OACManager`` / ``OacUtil``. 🔎 It is digit
  arithmetic over the seed arrays — modular digit addition, a configurable
  check-digit algorithm, and index tables (``getEncodeList``, ``arrayX/Y``,
  ``randomNumbersA/B/C``). The full algorithm is in ``OACManager.java`` (~1100
  lines) and has **not** been fully reproduced here; it is the natural next
  target for a standalone implementation because it needs no lock contact.
- **On-lock sync** uses BLE ``SetOACCmd`` (``1B``), ``SetShortOACCmd`` and
  ``QueryShortOacCmd``; ``QueryOACUnlockRecordCmd`` (``20``) reads OAC usage back.

.. note::

   🧩 For an owner who wants to hand out codes to staff/contractors without the
   lock being reachable, OAC is the most promising path — but it is only
   *identified* here, not a finished spec.

OMK (one-time master key)
-------------------------

``SetOMKCmd`` / ``QueryOMKCmd`` (``15``) and ``TPCCmd`` manage a one-time master
key used during pairing / recovery. ⚠️ Not traced in detail.
