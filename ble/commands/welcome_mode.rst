Welcome Mode / stay-unlocked (``9B`` / ``46``)
==============================================

"Welcome Mode" keeps the deadbolt retracted on a schedule — the lock stays
unlocked during a chosen window and re-locks at the end — so a door can be left
open for set hours without the auto-lock throwing it. (Internally the older
single-slot form is "always open mode".) The **lock holds the schedule and runs
it itself**; the cloud (``saveDvWelcomeConfig`` and friends) keeps only
a copy for the app to display, so the schedule survives a loss of internet.

🔎 Traced from app 3.3.4; not yet exercised on hardware. Welcome Mode travels on
the same transport as unlock (hub ``senddata`` / MQTT / direct BLE — see
:doc:`/reference/transports`), so it can be set remotely.

Two implementations, chosen by model
-------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 40 15 45

   * - Gate
     - Command
     - Capacity
   * - ``isSupport8SegmentWelcomeMode()``
     - ``9B``
     - 8 schedule slots (shared with energy-saving)
   * - ``isSupportWelcomeMode()``
     - ``46``
     - single schedule / always-on

- **``9B`` models** include PGK728WRHK (Visage), PGK7SWH(K), PGK728WHK, PGK628WH,
  PGK798HK, PGD628FG25, PGD728FG25, PGD728FNG25, PGD728FN21 (≥1.04.00),
  PGD238T (≥1.01.02), PGD7AWG25, PGD7YWG25, PGD238L (3.04.01–<4.00.00).
- **``46`` models** include PGD829AF/AFN/AFHK/KNF/FNUS/K7F/KHT, PGD678FS,
  PGD228FN, PGI302FC, PGD7S, **PGD728F/FN/FNP (≥1.02.46)**, **PGD628F
  (≥1.02.41)**, PGD628FC (≥1.00.36), PGD6S, … (list continues).

(Markers from ``BluetoothBeanManager.isSupport8SegmentWelcomeMode`` /
``isSupportWelcomeMode``.)

Weekday byte
------------

Both forms encode days as one byte: **bit 0 = Monday … bit 4 = Friday, bit 5 =
Saturday, bit 6 = Sunday, bit 7 = one-time**. So daily = ``0x7F``, weekdays =
``0x1F``, "once" = ``0x80``.

The ``9B`` command (8-slot)
---------------------------

Plaintext fields after the standard ``<mc_len> <enc_mc>`` prefix:

.. sourcecode:: text

   9B  <mc_len>  <enc_mc>  <flag>  <mode>  <configurator?>

- **flag** (``EnergySavingWelcomeModeFlag``): ``01`` set energy-saving, ``02``
  query energy-saving, ``03`` **set welcome**, ``04`` **query welcome**.
- **mode** (``EnergySavingWelcomeMode``): ``00`` normal, ``01`` **custom** (used
  for all welcome ops), ``02`` power-saving, ``03`` ultra power-saving.
- **configurator** (set operations only): ``08`` + 8 × *time-segment* +
  ``syncFlag`` (1 B) + ``toggleState`` (1 B).

  - *time-segment* = ``week(1) startH(1) startM(1) endH(1) endM(1)``; unused slots
    are ``00FFFFFFFF``.
  - ``syncFlag`` 0 = write the log entry, 1 = don't (from
    ``WelcomeModeRequest.getSyncFlag``).

Response (``0A9B``): ``00 flag mode [total(1) total×segment(5) syncFlag toggleState]``.
The app always writes the full 8-slot table (add/update/delete merge client-side
in ``WelcomeModeCmdConfiguratorMapper``).

The ``46`` command (single slot)
--------------------------------

.. sourcecode:: text

   46  <mc_len>  <enc_mc>  <action>  <week>  <start>  <end>

- **action**: ``1`` set, ``2`` query.
- always-on: ``01 7F FFFF FFFF``; the app's "off" placeholder: ``01 00 1111 1212``.
- **start/end**: ``HHmm`` in the lock's time zone, each two decimal digits → one
  hex byte (``DataUtils.a``).

Related single-slot commands:

- **``75`` (AlwaysOpenModeStatus)** — *how* Welcome Mode begins: set ``01 01`` /
  ``01 02``, query ``02 01``. Maps to log events 133 ("keep unlocked after first
  entry") and 134 ("unlocked automatically").
- **``8B`` (WelcomeMode139)** — *temporarily* switch Welcome Mode off. Only
  PGD628FC (≥3.00.42) and PGD628FNC (≥2.00.68). Set ``01 {01=on|02=off}``.

.. note::

   The ``keepUnlockFlag`` / ``unlockStartTime`` / ``unlockEndTime`` fields in the
   ``qrylknew`` lock data are 🧩 likely the cloud mirror of this
   schedule. Not traced end-to-end.
