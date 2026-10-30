Methodology and verification markers
====================================

How this was documented
------------------------

The material added in this fork comes from **static analysis of the Lockly
Android applications**, cross-referenced with the upstream projects in
:doc:`CREDITS`. No part of this documentation was produced by attacking Lockly's
servers or other people's locks.

Apps examined (downloaded from a public APK mirror, signatures checked against
the vendor's own signing certificate where applicable):

- ``com.lockly.smartlock`` (**LOCKLY**) 3.3.4 — the current consumer app, and
  2.9.0 for historical comparison.
- ``com.lockly.smartlock.home`` (**Lockly Home**) 1.6.2.
- ``com.lockly.smartlock.pro`` (**Lockly Manager**, the installer / property
  app) 1.4.9.

Tools: ``jadx`` for Java decompilation, ``apktool`` for resources, grep/manual
reading. BLE frame and endpoint behaviour was corroborated against LocklyHA,
which validated the core paths on real hardware.

.. warning::

   Nothing here was sent to a real lock as part of writing this fork, unless a
   page says otherwise. Hardware-validated facts are those LocklyHA confirmed;
   they are marked as such. Everything else is *read from the app's code* — a
   faithful description of what the app does, not proof that a reimplementation
   will be accepted by a given lock's firmware.

Verification markers
--------------------

Each non-trivial claim carries one of these:

.. list-table::
   :header-rows: 1
   :widths: 12 88

   * - Marker
     - Meaning
   * - ✅ **Verified**
     - Confirmed on real hardware (by LocklyHA, or noted inline). Safe to rely on.
   * - 🔎 **Code-traced**
     - Read directly from app bytecode: the field layout, command byte, or
       endpoint body is what the app builds. Not yet exercised on a lock.
   * - 🧩 **Inferred**
     - A reasonable deduction from names, log strings or surrounding code, not
       pinned to a specific line. Treat as a lead, not fact.
   * - ⚠️ **Unknown**
     - Named but not understood. Listed so the gap is visible.

Where a command or endpoint is only *identified* (its name and byte are known
but its payload has not been traced), it appears in the index tables with a
🧩 or ⚠️ marker rather than getting a detailed page it cannot yet support.

Scope of model coverage
------------------------

Command availability is gated per lock model and firmware inside
``BluetoothBeanManager`` and the ``isSupport…`` methods of ``BluetoothBean``.
Where known, the supported models are listed on each feature page. Absence of a
model from a list means "not seen in the code path read", not "confirmed
unsupported".

Responsible use
---------------

This documentation is for owners and integrators working with **their own**
locks and accounts, and for building interoperable software such as a
Home Assistant integration or a command-line tool. Credentials, master codes,
and the derived keys documented here grant full control of a lock; protect them
accordingly.
