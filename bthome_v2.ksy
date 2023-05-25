meta:
  id: bthome_service_data
  title: BTHome service data
  license: MIT
  endian: le
  bit-endian: le
  imports:
    - bthome_v2_unencrypted
doc: |
  BLE advertising in the BTHome v2 format
doc-ref: https://bthome.io/format/
seq:
  - id: device_information
    type: bthome_device_information
  - id: mac_reversed
    if: device_information.mac_included
    size: 6
  - id: measurements
    if: device_information.bthome_version == 2
    type:
      switch-on: device_information.encryption
      cases:
        false: bthome_measurement
        # TODO: implement encrypted measurements
    repeat: eos
types:
  bthome_device_information:
    seq:
      - id: encryption
        type: b1
      - id: mac_included
        type: b1
      - id: trigger_based
        type: b1
      - id: reserved_for_future_use
        type: b2
      - id: bthome_version
        type: b3
