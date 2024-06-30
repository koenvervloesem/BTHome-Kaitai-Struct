meta:
  id: bthome_service_data
  title: BTHome service data
  license: MIT
  endian: le
  bit-endian: le
doc: |
  BLE advertising in the BTHome v2 format
doc-ref: https://bthome.io/format/
seq:
  - id: device_information
    type: bthome_device_information
  - id: mac_reversed
    if: device_information.mac_included
    size: 6
  - id: measurement
    if: device_information.bthome_version == 2 and device_information.encryption == false
    type: bthome_measurement
    repeat: eos
  - id: ciphertext
    if: device_information.bthome_version == 2 and device_information.encryption == true
    size: _io.size - _io.pos - counter._sizeof - mic._sizeof
  - id: counter
    if: device_information.bthome_version == 2 and device_information.encryption == true
    type: u4be
  - id: mic
    if: device_information.bthome_version == 2 and device_information.encryption == true
    type: u4be
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
  bthome_measurement:
    seq:
      - id: object_id
        type: u1
        enum: bthome_object_id
      - id: data
        type:
          switch-on: object_id
          cases:
            'bthome_object_id::misc_packet_id': bthome_misc_packet_id
            'bthome_object_id::sensor_battery': bthome_sensor_battery
            'bthome_object_id::sensor_temperature_0_01': bthome_sensor_temperature_0_01
            'bthome_object_id::sensor_humidity_0_01': bthome_sensor_humidity_0_01
            'bthome_object_id::sensor_pressure_0_01': bthome_sensor_pressure_0_01
            'bthome_object_id::sensor_illuminance_0_01': bthome_sensor_illuminance_0_01
            'bthome_object_id::sensor_mass_kg_0_01': bthome_sensor_mass_kg_0_01
            'bthome_object_id::sensor_mass_lb_0_01': bthome_sensor_mass_lb_0_01
            'bthome_object_id::sensor_dewpoint_0_01': bthome_sensor_dewpoint_0_01
            'bthome_object_id::sensor_count': bthome_sensor_count
            'bthome_object_id::sensor_energy_0_001': bthome_sensor_energy_0_001
            'bthome_object_id::sensor_power_0_01': bthome_sensor_power_0_01
            'bthome_object_id::sensor_voltage_0_001': bthome_sensor_voltage_0_001
            'bthome_object_id::sensor_pm2_5': bthome_sensor_pm2_5
            'bthome_object_id::sensor_pm10': bthome_sensor_pm10
            'bthome_object_id::binary_generic_boolean': bthome_binary_generic_boolean
            'bthome_object_id::binary_power': bthome_binary_power
            'bthome_object_id::binary_opening': bthome_binary_opening
            'bthome_object_id::sensor_co2': bthome_sensor_co2
            'bthome_object_id::sensor_tvoc': bthome_sensor_tvoc
            'bthome_object_id::sensor_moisture_0_01': bthome_sensor_moisture_0_01
            'bthome_object_id::binary_battery': bthome_binary_battery
            'bthome_object_id::binary_battery_charging': bthome_binary_battery_charging
            'bthome_object_id::binary_carbon_monoxide': bthome_binary_carbon_monoxide
            'bthome_object_id::binary_cold': bthome_binary_cold
            'bthome_object_id::binary_connectivity': bthome_binary_connectivity
            'bthome_object_id::binary_door': bthome_binary_door
            'bthome_object_id::binary_garage_door': bthome_binary_garage_door
            'bthome_object_id::binary_gas': bthome_binary_gas
            'bthome_object_id::binary_heat': bthome_binary_heat
            'bthome_object_id::binary_light': bthome_binary_light
            'bthome_object_id::binary_lock': bthome_binary_lock
            'bthome_object_id::binary_moisture': bthome_binary_moisture
            'bthome_object_id::binary_motion': bthome_binary_motion
            'bthome_object_id::binary_moving': bthome_binary_moving
            'bthome_object_id::binary_occupancy': bthome_binary_occupancy
            'bthome_object_id::binary_plug': bthome_binary_plug
            'bthome_object_id::binary_presence': bthome_binary_presence
            'bthome_object_id::binary_problem': bthome_binary_problem
            'bthome_object_id::binary_running': bthome_binary_running
            'bthome_object_id::binary_safety': bthome_binary_safety
            'bthome_object_id::binary_smoke': bthome_binary_smoke
            'bthome_object_id::binary_sound': bthome_binary_sound
            'bthome_object_id::binary_tamper': bthome_binary_tamper
            'bthome_object_id::binary_vibration': bthome_binary_vibration
            'bthome_object_id::binary_window': bthome_binary_window
            'bthome_object_id::sensor_humidity': bthome_sensor_humidity
            'bthome_object_id::sensor_moisture': bthome_sensor_moisture
            'bthome_object_id::event_button': bthome_event_button
            'bthome_object_id::event_dimmer': bthome_event_dimmer
            'bthome_object_id::sensor_count_uint16': bthome_sensor_count_uint16
            'bthome_object_id::sensor_count_uint32': bthome_sensor_count_uint32
            'bthome_object_id::sensor_rotation_0_1': bthome_sensor_rotation_0_1
            'bthome_object_id::sensor_distance_mm': bthome_sensor_distance_mm
            'bthome_object_id::sensor_distance_m_0_1': bthome_sensor_distance_m_0_1
            'bthome_object_id::sensor_duration_0_001': bthome_sensor_duration_0_001
            'bthome_object_id::sensor_current_0_001': bthome_sensor_current_0_001
            'bthome_object_id::sensor_speed_0_01': bthome_sensor_speed_0_01
            'bthome_object_id::sensor_temperature_0_1': bthome_sensor_temperature_0_1
            'bthome_object_id::sensor_uv_index_0_1': bthome_sensor_uv_index_0_1
            'bthome_object_id::sensor_volume_0_1': bthome_sensor_volume_0_1
            'bthome_object_id::sensor_volume': bthome_sensor_volume
            'bthome_object_id::sensor_volume_flow_rate_0_001': bthome_sensor_volume_flow_rate_0_001
            'bthome_object_id::sensor_voltage_0_1': bthome_sensor_voltage_0_1
            'bthome_object_id::sensor_gas': bthome_sensor_gas
            'bthome_object_id::sensor_gas_uint32': bthome_sensor_gas_uint32
            'bthome_object_id::sensor_energy_0_001_uint32': bthome_sensor_energy_0_001_uint32
            'bthome_object_id::sensor_volume_0_001': bthome_sensor_volume_0_001
            'bthome_object_id::sensor_water': bthome_sensor_water
            'bthome_object_id::sensor_timestamp': bthome_sensor_timestamp
            'bthome_object_id::sensor_acceleration': bthome_sensor_acceleration
            'bthome_object_id::sensor_gyroscope': bthome_sensor_gyroscope
            'bthome_object_id::sensor_text': bthome_sensor_text
            'bthome_object_id::sensor_raw': bthome_sensor_raw
            'bthome_object_id::sensor_volume_storage': bthome_sensor_volume_storage
            'bthome_object_id::device_type': bthome_device_type
            'bthome_object_id::device_fw_version_uint32': bthome_device_fw_version_uint32
            'bthome_object_id::device_fw_version_uint24': bthome_device_fw_version_uint24
            _: bthome_unknown
  bool8:
    seq:
      - id: int_value
        type: u1
    instances:
      value:
        value: 'int_value & 0x01 == 0x01 ? true : false'
  u3:
    seq:
      - id: low_byte
        type: u1
      - id: middle_byte
        type: u1
      - id: high_byte
        type: u1
    instances:
      value:
        value: 'low_byte | (middle_byte << 8) | (high_byte << 16)'
  bthome_misc_packet_id:
    seq:
      - id: packet_id
        type: u1
  bthome_sensor_battery:
    seq:
      - id: battery
        type: u1
    instances:
      unit:
        value: '"%"'
  bthome_sensor_temperature_0_01:
    seq:
      - id: value
        type: s2
    instances:
      temperature:
        value: value * 0.01
      unit:
        value: '"\u00B0C"'
  bthome_sensor_humidity_0_01:
    seq:
      - id: value
        type: u2
    instances:
      humidity:
        value: value * 0.01
      unit:
        value: '"%"'
  bthome_sensor_pressure_0_01:
    seq:
      - id: value
        type: u3
    instances:
      pressure:
        value: value.value * 0.01
      unit:
        value: '"hPa"'
  bthome_sensor_illuminance_0_01:
    seq:
      - id: value
        type: u3
    instances:
      illuminance:
        value: value.value * 0.01
      unit:
        value: '"lux"'
  bthome_sensor_mass_kg_0_01:
    seq:
      - id: value
        type: u2
    instances:
      mass:
        value: value * 0.01
      unit:
        value: '"kg"'
  bthome_sensor_mass_lb_0_01:
    seq:
      - id: value
        type: u2
    instances:
      mass:
        value: value * 0.01
      unit:
        value: '"lb"'
  bthome_sensor_dewpoint_0_01:
    seq:
      - id: value
        type: s2
    instances:
      dew_point:
        value: value * 0.01
      unit:
        value: '"\u00B0C"'
  bthome_sensor_count:
    seq:
      - id: count
        type: u1
  bthome_sensor_energy_0_001:
    seq:
      - id: value
        type: u3
    instances:
      energy:
        value: value.value * 0.001
      unit:
        value: '"kWh"'
  bthome_sensor_power_0_01:
    seq:
      - id: value
        type: u3
    instances:
      power:
        value: value.value * 0.01
      unit:
        value: '"W"'
  bthome_sensor_voltage_0_001:
    seq:
      - id: value
        type: u2
    instances:
      voltage:
        value: value * 0.001
      unit:
        value: '"V"'
  bthome_sensor_pm2_5:
    seq:
      - id: pm2_5
        type: u2
    instances:
      unit:
        value: '"\u00B5g/m\u00B3"'
  bthome_sensor_pm10:
    seq:
      - id: pm10
        type: u2
    instances:
      unit:
        value: '"\u00B5g/m\u00B3"'
  bthome_binary_generic_boolean:
    seq:
      - id: generic_boolean
        type: bool8
  bthome_binary_power:
    seq:
      - id: power
        type: bool8
  bthome_binary_opening:
    seq:
      - id: opening
        type: bool8
  bthome_sensor_co2:
    seq:
      - id: co2
        type: u2
    instances:
      unit:
        value: '"ppm"'
  bthome_sensor_tvoc:
    seq:
      - id: tvoc
        type: u2
    instances:
      unit:
        value: '"\u00B5g/m\u00B3"'
  bthome_sensor_moisture_0_01:
    seq:
      - id: value
        type: u2
    instances:
      moisture:
        value: value * 0.01
      unit:
        value: '"%"'
  bthome_binary_battery:
    seq:
      - id: battery
        type: bool8
  bthome_binary_battery_charging:
    seq:
      - id: battery_charging
        type: bool8
  bthome_binary_carbon_monoxide:
    seq:
      - id: carbon_monoxide
        type: bool8
  bthome_binary_cold:
    seq:
      - id: cold
        type: bool8
  bthome_binary_connectivity:
    seq:
      - id: connectivity
        type: bool8
  bthome_binary_door:
    seq:
      - id: door
        type: bool8
  bthome_binary_garage_door:
    seq:
      - id: garage_door
        type: bool8
  bthome_binary_gas:
    seq:
      - id: gas
        type: bool8
  bthome_binary_heat:
    seq:
      - id: heat
        type: bool8
  bthome_binary_light:
    seq:
      - id: light
        type: bool8
  bthome_binary_lock:
    seq:
      - id: lock
        type: bool8
  bthome_binary_moisture:
    seq:
      - id: moisture
        type: bool8
  bthome_binary_motion:
    seq:
      - id: motion
        type: bool8
  bthome_binary_moving:
    seq:
      - id: moving
        type: bool8
  bthome_binary_occupancy:
    seq:
      - id: occupancy
        type: bool8
  bthome_binary_plug:
    seq:
      - id: plug
        type: bool8
  bthome_binary_presence:
    seq:
      - id: presence
        type: bool8
  bthome_binary_problem:
    seq:
      - id: problem
        type: bool8
  bthome_binary_running:
    seq:
      - id: running
        type: bool8
  bthome_binary_safety:
    seq:
      - id: safety
        type: bool8
  bthome_binary_smoke:
    seq:
      - id: smoke
        type: bool8
  bthome_binary_sound:
    seq:
      - id: sound
        type: bool8
  bthome_binary_tamper:
    seq:
      - id: tamper
        type: bool8
  bthome_binary_vibration:
    seq:
      - id: vibration
        type: bool8
  bthome_binary_window:
    seq:
      - id: window
        type: bool8
  bthome_sensor_humidity:
    seq:
      - id: humidity
        type: u1
    instances:
      unit:
        value: '"%"'
  bthome_sensor_moisture:
    seq:
      - id: moisture
        type: u1
    instances:
      unit:
        value: '"%"'
  bthome_event_button:
    seq:
      - id: event
        type: u1
        enum: button_event_type
  bthome_event_dimmer:
    seq:
      - id: event
        type: u1
        enum: dimmer_event_type
      - id: steps
        type: u1
  bthome_sensor_count_uint16:
    seq:
      - id: count
        type: u2
  bthome_sensor_count_uint32:
    seq:
      - id: count
        type: u4
  bthome_sensor_rotation_0_1:
    seq:
      - id: value
        type: s2
    instances:
      rotation:
        value: value * 0.1
      unit:
        value: '"\u00B0"'
  bthome_sensor_distance_mm:
    seq:
      - id: distance
        type: u2
    instances:
      unit:
        value: '"mm"'
  bthome_sensor_distance_m_0_1:
    seq:
      - id: value
        type: s2
    instances:
      distance:
        value: value * 0.1
      unit:
        value: '"m"'
  bthome_sensor_duration_0_001:
    seq:
      - id: value
        type: u3
    instances:
      duration:
        value: value.value * 0.001
      unit:
        value: '"s"'
  bthome_sensor_current_0_001:
    seq:
      - id: value
        type: u2
    instances:
      current:
        value: value * 0.001
      unit:
        value: '"A"'
  bthome_sensor_speed_0_01:
    seq:
      - id: value
        type: u2
    instances:
      speed:
        value: value * 0.01
      unit:
        value: '"m/s"'
  bthome_sensor_temperature_0_1:
    seq:
      - id: value
        type: s2
    instances:
      temperature:
        value: value * 0.1
      unit:
        value: '"\u00B0C"'
  bthome_sensor_uv_index_0_1:
    seq:
      - id: value
        type: u1
    instances:
      uv_index:
        value: value * 0.1
  bthome_sensor_volume_0_1:
    seq:
      - id: value
        type: u2
    instances:
      volume:
        value: value * 0.1
      unit:
        value: '"L"'
  bthome_sensor_volume:
    seq:
      - id: volume
        type: u2
    instances:
      unit:
        value: '"mL"'
  bthome_sensor_volume_flow_rate_0_001:
    seq:
      - id: value
        type: u2
    instances:
      volume_flow_rate:
        value: value * 0.001
      unit:
        value: '"m\u00B3/hr"'
  bthome_sensor_voltage_0_1:
    seq:
      - id: value
        type: u2
    instances:
      voltage:
        value: value * 0.1
      unit:
        value: '"V"'
  bthome_sensor_gas:
    seq:
      - id: value
        type: u3
    instances:
      gas:
        value: value.value * 0.001
      unit:
        value: '"m³"'
  bthome_sensor_gas_uint32:
    seq:
      - id: value
        type: u4
    instances:
      gas:
        value: value * 0.001
      unit:
        value: '"m³"'
  bthome_sensor_energy_0_001_uint32:
    seq:
      - id: value
        type: u4
    instances:
      energy:
        value: value * 0.001
      unit:
        value: '"kWh"'
  bthome_sensor_volume_0_001:
    seq:
      - id: value
        type: u4
    instances:
      volume:
        value: value * 0.001
      unit:
        value: '"L"'
  bthome_sensor_water:
    seq:
      - id: value
        type: u4
    instances:
      water:
        value: value * 0.001
      unit:
        value: '"L"'
  bthome_sensor_timestamp:
    seq:
      - id: value
        type: u4
  bthome_sensor_acceleration:
    seq:
      - id: value
        type: u2
    instances:
      acceleration:
        value: value * 0.001
      unit:
        value: '"m/s\u00B2"'
  bthome_sensor_gyroscope:
    seq:
      - id: value
        type: u2
    instances:
      gyroscope:
        value: value * 0.001
      unit:
        value: '"\u00B0/s"'
  bthome_sensor_text:
    seq:
      - id: len_value
        type: u1
      - id: value
        type: str
        size: len_value
        encoding: UTF-8
  bthome_sensor_raw:
    seq:
      - id: len_value
        type: u1
      - id: value
        size: len_value
  bthome_sensor_volume_storage:
    seq:
      - id: value
        type: u4
    instances:
      volume_storage:
        value: value * 0.001
      unit:
        value: '"L"'
  bthome_device_type:
    seq:
      - id: device_type_id
        type: u2
  bthome_device_fw_version_uint32:
    seq:
      - id: fw_version_build
        type: u1
      - id: fw_version_patch
        type: u1
      - id: fw_version_minor
        type: u1
      - id: fw_version_major
        type: u1
  bthome_device_fw_version_uint24:
    seq:
      - id: fw_version_patch
        type: u1
      - id: fw_version_minor
        type: u1
      - id: fw_version_major
        type: u1
  bthome_unknown:
    doc: Data with unknown object ID are parsed as a byte array until the end
    seq:
      - id: unknown
        size-eos: true
enums:
  bthome_object_id:
    0x00: misc_packet_id
    0x01: sensor_battery
    0x02: sensor_temperature_0_01
    0x03: sensor_humidity_0_01
    0x04: sensor_pressure_0_01
    0x05: sensor_illuminance_0_01
    0x06: sensor_mass_kg_0_01
    0x07: sensor_mass_lb_0_01
    0x08: sensor_dewpoint_0_01
    0x09: sensor_count
    0x0A: sensor_energy_0_001
    0x0B: sensor_power_0_01
    0x0C: sensor_voltage_0_001
    0x0D: sensor_pm2_5
    0x0E: sensor_pm10
    0x0F: binary_generic_boolean
    0x10: binary_power
    0x11: binary_opening
    0x12: sensor_co2
    0x13: sensor_tvoc
    0x14: sensor_moisture_0_01
    0x15: binary_battery
    0x16: binary_battery_charging
    0x17: binary_carbon_monoxide
    0x18: binary_cold
    0x19: binary_connectivity
    0x1A: binary_door
    0x1B: binary_garage_door
    0x1C: binary_gas
    0x1D: binary_heat
    0x1E: binary_light
    0x1F: binary_lock
    0x20: binary_moisture
    0x21: binary_motion
    0x22: binary_moving
    0x23: binary_occupancy
    0x24: binary_plug
    0x25: binary_presence
    0x26: binary_problem
    0x27: binary_running
    0x28: binary_safety
    0x29: binary_smoke
    0x2A: binary_sound
    0x2B: binary_tamper
    0x2C: binary_vibration
    0x2D: binary_window
    0x2E: sensor_humidity
    0x2F: sensor_moisture
    0x3A: event_button
    0x3C: event_dimmer
    0x3D: sensor_count_uint16
    0x3E: sensor_count_uint32
    0x3F: sensor_rotation_0_1
    0x40: sensor_distance_mm
    0x41: sensor_distance_m_0_1
    0x42: sensor_duration_0_001
    0x43: sensor_current_0_001
    0x44: sensor_speed_0_01
    0x45: sensor_temperature_0_1
    0x46: sensor_uv_index_0_1
    0x47: sensor_volume_0_1
    0x48: sensor_volume
    0x49: sensor_volume_flow_rate_0_001
    0x4A: sensor_voltage_0_1
    0x4B: sensor_gas
    0x4C: sensor_gas_uint32
    0x4D: sensor_energy_0_001_uint32
    0x4E: sensor_volume_0_001
    0x4F: sensor_water
    0x50: sensor_timestamp
    0x51: sensor_acceleration
    0x52: sensor_gyroscope
    0x53: sensor_text
    0x54: sensor_raw
    0x55: sensor_volume_storage
    0xF0: device_type
    0xF1: device_fw_version_uint32
    0xF2: device_fw_version_uint24
  button_event_type:
    0x00: none
    0x01: press
    0x02: double_press
    0x03: triple_press
    0x04: long_press
    0x05: long_double_press
    0x06: long_triple_press
    0x80: hold_press
  dimmer_event_type:
    0x00: none
    0x01: rotate_left
    0x02: rotate_right
