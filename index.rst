Unofficial Lockly API documentation
===================================

Welcome to the Unofficial Lockly API documentation!

This is an ongoing effort to document the various `Lockly <https://lockly.com.au>`_ APIs, with the goal of
enabling the development of projects such as:

- An alternative, cross-platform app capable of using both Wi-Fi and Bluetooth to
  communicate with locks
- A `Home Assistant <https://www.home-assistant.io>`_ integration
- Command-line tooling for owners who want to script their own locks

.. note::

   This is a community fork that greatly expands the original. It now covers the
   Bluetooth command layer and the MQTT device channel in addition to the REST
   API, and adds an index of every lock command and REST endpoint seen in the
   apps. Please read :doc:`methodology` first — every claim carries a marker
   showing whether it is hardware-verified, traced from app code, or inferred.

   **Unofficial and unaffiliated.** Not endorsed by Lockly. See :doc:`CREDITS`.

.. toctree::
   :caption: Start here
   :maxdepth: 1

   methodology
   CREDITS

.. toctree::
   :caption: APIs
   :maxdepth: 2

   rest/index
   ble/index
   mqtt/index

.. toctree::
   :caption: Reference
   :maxdepth: 1

   reference/transports
   reference/command_index
   reference/endpoint_index
   reference/models
