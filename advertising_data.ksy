meta:
  id: advertising_data
  title: Bluetooth advertising data
  license: MIT
  endian: le
  bit-endian: le
  imports:
    - bthome_v2
doc: |
  Advertising and scan response data format
doc-ref: Bluetooth Core Specification Version 5.4 Vol 3, Part C
seq:
  - id: ad_structure
    type: ad_structure
    repeat: eos
enums:
  ad_types:
    0x01: flags
    0x08: shortened_local_name
    0x09: complete_local_name
    0x16: service_data_16_bit_uuid
types:
  ad_structure:
    seq:
      - id: length
        type: u1
      - id: type
        type: u1
        enum: ad_types
      - id: data
        size: length - 1
        type:
          switch-on: type
          cases:
            'ad_types::flags': ad_flags
            'ad_types::shortened_local_name': ad_shortened_local_name
            'ad_types::complete_local_name': ad_complete_local_name
            'ad_types::service_data_16_bit_uuid': ad_service_data_16_bit_uuid
  ad_flags:
    doc-ref: Bluetooth Core Specification Supplement 11, Part 1, Section 1.3
    seq:
      - id: le_limited_discoverable_mode
        type: b1
      - id: le_general_discoverable_mode
        type: b1
      - id: br_edr_not_supported
        type: b1
      - id: simultaneous_le_and_br_edr_to_same_device_capable
        type: b1
      - id: previously_used
        type: b1
  ad_shortened_local_name:
    doc-ref: Bluetooth Core Specification Supplement 11, Part 1, Section 1.2
    seq:
      - id: local_name
        type: str
        encoding: UTF-8
        size-eos: true
  ad_complete_local_name:
    doc-ref: Bluetooth Core Specification Supplement 11, Part 1, Section 1.2
    seq:
      - id: local_name
        type: str
        encoding: UTF-8
        size-eos: true
  ad_service_data_16_bit_uuid:
    doc-ref: Bluetooth Core Specification Supplement 11, Part 1, Section 1.11
    seq:
      - id: uuid
        type: u2
      - id: data
        size-eos: true
        type:
          switch-on: uuid
          cases:
            0xfcd2: bthome_service_data
