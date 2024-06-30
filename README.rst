====================
BTHome Kaitai Struct
====================


    BTHome format description in Kaitai Struct


This is a description of the `BTHome <https://bthome.io/>`_ format for broadcasting sensor data and button presses over Bluetooth Low Energy. The description uses `Kaitai Struct <https://kaitai.io/>`_, a declarative language to describe various binary data structures. As a result, the format description can be compiled into source files of one of 11 supported programming languages to create a BTHome parser: C++/STL, C#, Go, Java, JavaScript, Lua, Nim, Perl, PHP, Python and Ruby.

Format description
==================

The format description in Kaitai Struct is listed in two files:

* `advertising\_data.ksy <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/blob/main/advertising_data.ksy>`_: the raw advertising data, including advertising data elements for flags, local name and service data
* `bthome\_v2.ksy <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/blob/main/bthome_v2.ksy>`_: the service data for BTHome's UUID 0xFCD2

In most applications you should use bthome\_v2.ksy. For example, the files in the `data <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/tree/main/data>`_ directory contain service data that can be decoded with this Kaitai Struct file. The `Python example script <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/blob/main/examples/python/detect_bthome_v2.py>`_ also uses a `Python package <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/tree/main/examples/python/kaitai>`_ generated from this file.

Limitations
===========

The format description currently has the following limitations:

* Only the `BTHome v2 format <https://bthome.io/format/>`_ is supported.
* The `encrypted format <https://bthome.io/encryption/>`_ is supported, but the decryption of the ciphertext should be implemented as extra code. Look at the tests or the Python example code for a way to do this.

Exploring the structure of BTHome data
======================================

You can explore the structure of BTHome service data interactively with `Kaitai Struct Visualizer <https://github.com/kaitai-io/kaitai_struct_visualizer/>`_. For example:

.. code-block:: shell

  ksv data/bthome_packet_id_temperature_humidity_battery.bin bthome_v2.ksy

This looks like this:

.. image:: https://github.com/koenvervloesem/BTHome-Kaitai-Struct/raw/main/ksv-example.png
    :alt: Exploring BTHome service data in Kaitai Struct Visualizer

You can also dump the decoded information from a file with BTHome service data with ``ksdump``, part of Kaitai Struct Visualizer:

.. code-block:: shell

  $ ksdump data/bthome_double_voltage_different_object_id.bin bthome_v2.ksy
  Compilation OK
  ... processing bthome_v2.ksy 0
  ...... loading bthome_service_data.rb
  ...... loading bthome_measurement.rb
  Classes loaded OK, main class = BthomeServiceData
  device_information:
    bthome_version: 2
    encryption: false
    mac_included: false
    reserved_for_future_use: 0
    trigger_based: false
  measurement:
  - data:
      packet_id: 1
  - data:
      power: 0.0
      unit: W
      value:
        high_byte: 0
        low_byte: 0
        middle_byte: 0
        value: 0
  - data:
      unit: V
      value: 2317
      voltage: 231.70000000000002
  - data:
      battery: 51
      unit: "%"
  - data:
      unit: V
      value: 3305
      voltage: 3.305

Compiling the format description into parser code
=================================================

Download the `Kaitai Struct compiler <https://kaitai.io/#download>`_ and then compile the BTHome format specification into a parser of your favorite programming language. As an example, here's how you create a Python parser (which isn't that interesting, because there's already the official `bthome-ble <https://github.com/Bluetooth-Devices/bthome-ble>`_ parser):

.. code-block:: shell

  ksc -t python --python-package . bthome_v2.ksy

If you want to try it out, move the generated Python files to the directory with the Python example:

.. code-block:: shell

  mv *.py examples/python/kaitai

Install the requirements of the example script and run it:

.. code-block:: shell

  pip install -r examples/python/requirements.txt
  python examples/python/detect_bthome_v2.py

This continuously scans for BTHome v2 advertisements and decodes them. If you want to decrypt encrypted BTHome advertisements, add the bindkey with the ``--bindkey`` parameter on the command line.

Testing the format description
==============================

There's a `Python test script <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/blob/main/tests/test_bthome_v2.py>`_ that tests the generated Python parser on some data files with service data. Those data files contain service data from BTHome advertisements used in `bthome-ble's tests <https://github.com/Bluetooth-Devices/bthome-ble/tree/main/tests>`_. First compile the format description into the Python parser code, move the generated Python files to the directory with the Python example, and then install `pytest <https://docs.pytest.org>`_ and run the tests with:

.. code-block:: shell

  pytest

All tests should pass.

Projects using this BTHome format description
=============================================

* `BTHome Bluetooth Binding for openHAB <https://github.com/seime/openhab-bthome?tab=readme-ov-file>`_ (Java)

Learn more about Bluetooth Low Energy development
=================================================

If you want to learn more about Bluetooth Low Energy development, read the book `Develop your own Bluetooth Low Energy Applications for Raspberry Pi, ESP32 and nRF52 with Python, Arduino and Zephyr <https://koen.vervloesem.eu/books/develop-your-own-bluetooth-low-energy-applications/>`_ and the accompanying GitHub repository `koenvervloesem/bluetooth-low-energy-applications <https://github.com/koenvervloesem/bluetooth-low-energy-applications>`_.

License
=======

This project is provided by Koen Vervloesem as open source software with the MIT license. See the `LICENSE <https://github.com/koenvervloesem/BTHome-Kaitai-Struct/blob/main/LICENSE.txt>`_ file for more information.
