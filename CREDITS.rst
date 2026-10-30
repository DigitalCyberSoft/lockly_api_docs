Credits and licensing
=====================

This project builds on the work of several people. It documents the Lockly APIs
for interoperability and educational purposes. It is **unofficial** and is not
affiliated with, authorised by, or endorsed by Lockly Security Inc. /
PIN GENIE LIMITED.

Upstream sources
----------------

- **hacker1024** — the original
  `Unofficial Lockly API documentation <https://github.com/hacker1024/lockly_api_docs>`_
  (2022). The REST message format, the *anonymous* RSA / *user* 3DES encryption
  split, and the first ``login``, ``qrylknew``, ``asyncSend`` and ``lockly/syspara``
  pages originate here. This repository is a fork of that project.

- **bdmartin** — the
  `endpoint-documentation fork <https://github.com/bdmartin/lockly_api_docs>`_
  (2026), merged into this repository. The read-only endpoint pages
  (``getUserInfoAndDvList``, ``getEkeyList``, ``oac/get``, ``admin/invite/list``,
  ``getFingerprintList``, ``get/deviceConfigInfo``, ``check/isPay``,
  ``user/isbeta``, ``backup/ekeyOrEbadge``, ``lock/cachedstatus/get``) are their
  work, validated against the live API.

- **Forcky — LocklyHA** — the
  `Lockly Home Assistant integration <https://github.com/Forcky/LocklyHA>`_
  (MIT licensed). Its ``docs/api.md`` is the first description of the BLE frame
  format, the AES-128 payload key derivation, the ``senddata`` live path, the
  real MQTT broker, and the ``cod`` error codes, all validated on real hardware
  (PGD628FN + PGH220, and Lockly Visage PGK728WRHK). The :doc:`ble/index` and
  :doc:`mqtt/index` sections adapt and extend that material. LocklyHA is
  copyright its authors under the MIT License; a copy is in
  ``third_party/LocklyHA-LICENSE``.

Additions in this fork
----------------------

New material in this fork — the BLE command index, the feature command pages
(Welcome Mode, Rain Mode, offline access codes, firmware/OTA, enrolment and
others), the corrected MQTT notes, and the full REST endpoint index — was
produced by static analysis of the Lockly Android apps. See
:doc:`methodology` for how, and for the honesty markers used throughout.

Licensing
---------

- New material added in this fork is released under
  **Creative Commons Attribution 4.0 International (CC BY 4.0)** — see
  ``LICENSE``. Reuse freely with attribution.
- Text inherited from hacker1024's repository carries **no licence** (none was
  ever applied upstream); it is reproduced here as a fork for interoperability
  documentation. It is not relicensed.
- Material adapted from LocklyHA remains under the **MIT License** of that
  project (``third_party/LocklyHA-LICENSE``).

Trademarks
----------

"Lockly" and the model names (Visage, Secure, Flex, Vision, …) are trademarks of
their respective owner. They are used here only to identify the hardware being
described.
