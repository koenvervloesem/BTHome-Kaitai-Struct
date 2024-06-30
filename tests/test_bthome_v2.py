"""Tests for Python module generated from BTHome Kaitai Struct files."""
import binascii
from datetime import datetime, timezone
import pytest

from examples.python.kaitai.bthome_service_data import BthomeServiceData

from Cryptodome.Cipher import AES


def decrypt_payload(payload: bytes, mic: bytes, bindkey: bytes, nonce: bytes) -> bytes:
    cipher = AES.new(bindkey, AES.MODE_CCM, nonce=nonce, mac_len=4)
    return cipher.decrypt_and_verify(payload, mic)


@pytest.fixture
def bthome_data(filename):
    """Return BTHome service data from the given file."""
    with open(filename, "rb") as data_file:
        return BthomeServiceData.from_bytes(data_file.read())


@pytest.mark.parametrize("filename", ["data/bthome_wrong_object_id.bin"])
def test_bthome_wrong_object_id(bthome_data):
    """Test BTHome parser for a non-existing Object ID xFE."""
    assert bthome_data.measurement[0].data.unknown == b"\xca\x09"


@pytest.mark.parametrize(
    "filename", ["data/bthome_battery_wrong_object_id_humidity.bin"]
)
def test_bthome_battery_wrong_object_id_humidity(bthome_data):
    """Test BTHome parser for battery, wrong object id and humidity reading.

    Should only return the battery reading, as humidity is after wrong object id.
    """
    assert bthome_data.measurement[0].data.battery == 93
    assert bthome_data.measurement[0].data.unit == "%"
    assert bthome_data.measurement[1].data.unknown == b"\x5d\x09\x03\xb7\x18"


@pytest.mark.parametrize("filename", ["data/bthome_with_mac.bin"])
def test_bthome_with_mac(bthome_data):
    """Test BTHome parser for pressure reading with MAC address in payload."""
    assert bthome_data.mac_reversed == bytes([0xB2, 0x18, 0x8D, 0x38, 0xC1, 0xA4])
    assert round(bthome_data.measurement[0].data.pressure, 2) == 1008.83
    assert bthome_data.measurement[0].data.unit == "hPa"


@pytest.mark.parametrize("filename", ["data/bthome_temperature_humidity.bin"])
def test_bthome_temperature_humidity(bthome_data):
    """Test BTHome parser for temperature humidity reading without encryption."""
    assert round(bthome_data.measurement[0].data.temperature, 2) == 25.06
    assert bthome_data.measurement[0].data.unit == "°C"
    assert round(bthome_data.measurement[1].data.humidity, 2) == 50.55
    assert bthome_data.measurement[1].data.unit == "%"


@pytest.mark.parametrize(
    "filename", ["data/bthome_packet_id_temperature_humidity_battery.bin"]
)
def test_bthome_packet_id_temperature_humidity_battery(bthome_data):
    """Test BTHome parser for packet_id, temperature, humidity and battery reading."""
    assert bthome_data.measurement[0].data.packet_id == 9
    assert bthome_data.measurement[1].data.battery == 93
    assert bthome_data.measurement[1].data.unit == "%"
    assert round(bthome_data.measurement[2].data.temperature, 2) == 23.97
    assert bthome_data.measurement[2].data.unit == "°C"
    assert round(bthome_data.measurement[3].data.humidity, 2) == 63.27
    assert bthome_data.measurement[3].data.unit == "%"


@pytest.mark.parametrize("filename", ["data/bthome_pressure.bin"])
def test_bthome_pressure(bthome_data):
    """Test BTHome parser for pressure reading without encryption."""
    assert round(bthome_data.measurement[0].data.pressure, 2) == 1008.83
    assert bthome_data.measurement[0].data.unit == "hPa"


@pytest.mark.parametrize("filename", ["data/bthome_illuminance.bin"])
def test_bthome_illuminance(bthome_data):
    """Test BTHome parser for illuminance reading without encryption."""
    assert round(bthome_data.measurement[0].data.illuminance, 2) == 13460.67
    assert bthome_data.measurement[0].data.unit == "lux"


@pytest.mark.parametrize("filename", ["data/bthome_mass_kilograms.bin"])
def test_bthome_mass_kilograms(bthome_data):
    """Test BTHome parser for mass reading in kilograms without encryption."""
    assert round(bthome_data.measurement[0].data.mass, 2) == 80.3
    assert bthome_data.measurement[0].data.unit == "kg"


@pytest.mark.parametrize("filename", ["data/bthome_mass_pounds.bin"])
def test_bthome_mass_pounds(bthome_data):
    """Test BTHome parser for mass reading in pounds without encryption."""
    assert round(bthome_data.measurement[0].data.mass, 2) == 74.86
    assert bthome_data.measurement[0].data.unit == "lb"


@pytest.mark.parametrize("filename", ["data/bthome_dew_point.bin"])
def test_bthome_dew_point(bthome_data):
    """Test BTHome parser for dew point reading without encryption."""
    assert round(bthome_data.measurement[0].data.dew_point, 2) == 17.38
    assert bthome_data.measurement[0].data.unit == "°C"


@pytest.mark.parametrize("filename", ["data/bthome_count.bin"])
def test_bthome_count(bthome_data):
    """Test BTHome parser for counter reading without encryption."""
    assert bthome_data.measurement[0].data.count == 96


@pytest.mark.parametrize("filename", ["data/bthome_energy.bin"])
def test_bthome_energy(bthome_data):
    """Test BTHome parser for energy reading without encryption."""
    assert round(bthome_data.measurement[0].data.energy, 3) == 1346.067
    assert bthome_data.measurement[0].data.unit == "kWh"


@pytest.mark.parametrize("filename", ["data/bthome_power.bin"])
def test_bthome_power(bthome_data):
    """Test BTHome parser for power reading without encryption."""
    assert round(bthome_data.measurement[0].data.power, 2) == 69.14
    assert bthome_data.measurement[0].data.unit == "W"


@pytest.mark.parametrize("filename", ["data/bthome_voltage.bin"])
def test_bthome_voltage(bthome_data):
    """Test BTHome parser for voltage reading without encryption."""
    assert round(bthome_data.measurement[0].data.voltage, 3) == 3.074
    assert bthome_data.measurement[0].data.unit == "V"


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor.bin"])
def test_bthome_binary_sensor(bthome_data):
    """Test BTHome parser for binary sensor without device class, without encryption."""
    assert bthome_data.measurement[0].data.generic_boolean.value


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor_power.bin"])
def test_bthome_binary_sensor_power(bthome_data):
    """Test BTHome parser for binary sensor power without encryption."""
    assert bthome_data.measurement[0].data.power.value


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor_opening.bin"])
def test_bthome_binary_sensor_opening(bthome_data):
    """Test BTHome parser for binary sensor opening without encryption."""
    assert bthome_data.measurement[0].data.opening.value is False


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor_window.bin"])
def test_bthome_binary_sensor_window(bthome_data):
    """Test BTHome parser for binary sensor window without encryption."""
    assert bthome_data.measurement[0].data.window.value is True


@pytest.mark.parametrize("filename", ["data/bthome_pm.bin"])
def test_bthome_pm(bthome_data):
    """Test BTHome parser for PM2.5 and PM10 reading without encryption."""
    assert bthome_data.measurement[0].data.pm2_5 == 3090
    assert bthome_data.measurement[0].data.unit == "µg/m³"
    assert bthome_data.measurement[1].data.pm10 == 7170
    assert bthome_data.measurement[1].data.unit == "µg/m³"


@pytest.mark.parametrize("filename", ["data/bthome_co2.bin"])
def test_bthome_co2(bthome_data):
    """Test BTHome parser for CO2 reading without encryption."""
    assert bthome_data.measurement[0].data.co2 == 1250
    assert bthome_data.measurement[0].data.unit == "ppm"


@pytest.mark.parametrize("filename", ["data/bthome_voc.bin"])
def test_bthome_voc(bthome_data):
    """Test BTHome parser for VOC reading without encryption."""
    assert bthome_data.measurement[0].data.tvoc == 307
    assert bthome_data.measurement[0].data.unit == "µg/m³"


@pytest.mark.parametrize("filename", ["data/bthome_moisture.bin"])
def test_bthome_moisture(bthome_data):
    """Test BTHome parser for moisture reading from b-parasite sensor."""
    assert round(bthome_data.measurement[0].data.moisture, 2) == 30.74
    assert bthome_data.measurement[0].data.unit == "%"


@pytest.mark.parametrize("filename", ["data/bthome_event_button_long_press.bin"])
def test_bthome_event_button_long_press(bthome_data):
    """Test BTHome parser for an event of a long press on a button without encryption."""
    assert (
        bthome_data.measurement[0].data.event
        == BthomeServiceData.ButtonEventType.long_press
    )


@pytest.mark.parametrize("filename", ["data/bthome_event_triple_button_device.bin"])
def test_bthome_event_triple_button_device(bthome_data):
    """
    Test BTHome parser for an event of a triple button device where
    the 2nd button is pressed and the 3rd button is triple pressed.
    """
    assert (
        bthome_data.measurement[0].data.event == BthomeServiceData.ButtonEventType.none
    )
    assert (
        bthome_data.measurement[1].data.event == BthomeServiceData.ButtonEventType.press
    )
    assert (
        bthome_data.measurement[2].data.event
        == BthomeServiceData.ButtonEventType.triple_press
    )


@pytest.mark.parametrize("filename", ["data/bthome_event_button_hold_press.bin"])
def test_bthome_event_button_hold_press(bthome_data):
    """Test BTHome parser for an event of a hold press on a button without encryption."""
    assert (
        bthome_data.measurement[0].data.event
        == BthomeServiceData.ButtonEventType.hold_press
    )


@pytest.mark.parametrize(
    "filename", ["data/bthome_event_dimmer_rotate_left_3_steps.bin"]
)
def test_bthome_event_dimmer_rotate_left_3_steps(bthome_data):
    """Test BTHome parser for an event rotating a dimmer 3 steps left."""
    assert (
        bthome_data.measurement[0].data.event
        == BthomeServiceData.DimmerEventType.rotate_left
    )
    assert bthome_data.measurement[0].data.steps == 3


@pytest.mark.parametrize(
    "filename", ["data/bthome_event_dimmer_none.bin"]
)
def test_bthome_event_dimmer_none(bthome_data):
    """Test BTHome parser for an event None for a dimmer."""
    assert (
        bthome_data.measurement[0].data.event
        == BthomeServiceData.DimmerEventType.none
    )
    assert bthome_data.measurement[0].data.steps == 0


@pytest.mark.parametrize("filename", ["data/bthome_rotation.bin"])
def test_bthome_rotation(bthome_data):
    """Test BTHome parser for rotation."""
    assert round(bthome_data.measurement[0].data.rotation, 1) == 307.4
    assert bthome_data.measurement[0].data.unit == "°"


@pytest.mark.parametrize("filename", ["data/bthome_distance_millimeters.bin"])
def test_bthome_distance_millimeters(bthome_data):
    """Test BTHome parser for distance in millimeters."""
    assert bthome_data.measurement[0].data.distance == 12
    assert bthome_data.measurement[0].data.unit == "mm"


@pytest.mark.parametrize("filename", ["data/bthome_distance_meters.bin"])
def test_bthome_distance_meters(bthome_data):
    """Test BTHome parser for distance in meters."""
    assert round(bthome_data.measurement[0].data.distance, 1) == 7.8
    assert bthome_data.measurement[0].data.unit == "m"


@pytest.mark.parametrize("filename", ["data/bthome_duration.bin"])
def test_bthome_duration(bthome_data):
    """Test BTHome parser for duration in seconds."""
    assert round(bthome_data.measurement[0].data.duration, 3) == 13.39
    assert bthome_data.measurement[0].data.unit == "s"


@pytest.mark.parametrize("filename", ["data/bthome_current.bin"])
def test_bthome_current(bthome_data):
    """Test BTHome parser for current in A."""
    assert round(bthome_data.measurement[0].data.current, 3) == 13.39
    assert bthome_data.measurement[0].data.unit == "A"


@pytest.mark.parametrize("filename", ["data/bthome_speed.bin"])
def test_bthome_speed(bthome_data):
    """Test BTHome parser for speed in m/s."""
    assert round(bthome_data.measurement[0].data.speed, 2) == 133.9
    assert bthome_data.measurement[0].data.unit == "m/s"


@pytest.mark.parametrize("filename", ["data/bthome_temperature_2.bin"])
def test_bthome_temperature_2(bthome_data):
    """Test BTHome parser for temperature with one digit."""
    assert round(bthome_data.measurement[0].data.temperature, 1) == 27.3
    assert bthome_data.measurement[0].data.unit == "°C"


@pytest.mark.parametrize("filename", ["data/bthome_uv_index.bin"])
def test_bthome_uv_index(bthome_data):
    """Test BTHome parser for UV index."""
    assert round(bthome_data.measurement[0].data.uv_index, 1) == 5.0


@pytest.mark.parametrize("filename", ["data/bthome_volume_liters.bin"])
def test_bthome_volume_liters(bthome_data):
    """Test BTHome parser for volume in liters."""
    assert round(bthome_data.measurement[0].data.volume, 1) == 2215.1
    assert bthome_data.measurement[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_volume_milliliters.bin"])
def test_bthome_volume_milliliters(bthome_data):
    """Test BTHome parser for volume in milliliters."""
    assert bthome_data.measurement[0].data.volume == 34780
    assert bthome_data.measurement[0].data.unit == "mL"


@pytest.mark.parametrize("filename", ["data/bthome_volume_flow_rate.bin"])
def test_bthome_volume_flow_rate(bthome_data):
    """Test BTHome parser for volume flow rate in m³ per hour."""
    assert round(bthome_data.measurement[0].data.volume_flow_rate, 3) == 34.780
    assert bthome_data.measurement[0].data.unit == "m³/hr"


@pytest.mark.parametrize("filename", ["data/bthome_voltage_2.bin"])
def test_bthome_voltage_2(bthome_data):
    """Test BTHome parser for voltage reading without encryption."""
    assert round(bthome_data.measurement[0].data.voltage, 1) == 307.4
    assert bthome_data.measurement[0].data.unit == "V"


@pytest.mark.parametrize("filename", ["data/bthome_gas.bin"])
def test_bthome_gas(bthome_data):
    """Test BTHome parser for gas reading without encryption."""
    assert round(bthome_data.measurement[0].data.gas, 3) == 1346.067
    assert bthome_data.measurement[0].data.unit == "m³"


@pytest.mark.parametrize("filename", ["data/bthome_gas_2.bin"])
def test_bthome_gas_2(bthome_data):
    """Test BTHome parser for uint32 gas reading without encryption."""
    assert round(bthome_data.measurement[0].data.gas, 3) == 25821.505
    assert bthome_data.measurement[0].data.unit == "m³"


@pytest.mark.parametrize("filename", ["data/bthome_energy_2.bin"])
def test_bthome_energy_2(bthome_data):
    """Test BTHome parser for uint32 energy reading without encryption."""
    assert round(bthome_data.measurement[0].data.energy, 3) == 344593.17
    assert bthome_data.measurement[0].data.unit == "kWh"


@pytest.mark.parametrize("filename", ["data/bthome_volume_liters_2.bin"])
def test_bthome_volume_liters_2(bthome_data):
    """Test BTHome parser for uint32 volume in liters."""
    assert round(bthome_data.measurement[0].data.volume, 3) == 19551.879
    assert bthome_data.measurement[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_volume_water.bin"])
def test_bthome_volume_water(bthome_data):
    """Test BTHome parser for water in liters."""
    assert round(bthome_data.measurement[0].data.water, 3) == 19551.879
    assert bthome_data.measurement[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_timestamp.bin"])
def test_bthome_timestamp(bthome_data):
    """Test BTHome parser for Unix timestamp."""
    timestamp = bthome_data.measurement[0].data.value
    assert (
        datetime(2023, 5, 14, 19, 41, 17, tzinfo=timezone.utc).timestamp() == timestamp
    )


@pytest.mark.parametrize("filename", ["data/bthome_acceleration.bin"])
def test_bthome_acceleration(bthome_data):
    """Test BTHome parser for acceleration in m/s²."""
    assert round(bthome_data.measurement[0].data.acceleration, 3) == 22.151
    assert bthome_data.measurement[0].data.unit == "m/s²"


@pytest.mark.parametrize("filename", ["data/bthome_gyroscope.bin"])
def test_bthome_gyroscope(bthome_data):
    """Test BTHome parser for gyroscope in °/s."""
    assert round(bthome_data.measurement[0].data.gyroscope, 3) == 22.151
    assert bthome_data.measurement[0].data.unit == "°/s"


@pytest.mark.parametrize("filename", ["data/bthome_text.bin"])
def test_bthome_text(bthome_data):
    """Test BTHome parser for text."""
    assert bthome_data.measurement[0].data.value == "Hello World!"


@pytest.mark.parametrize("filename", ["data/bthome_raw.bin"])
def test_bthome_raw(bthome_data):
    """Test BTHome parser for raw data."""
    assert bthome_data.measurement[0].data.value == b"\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64\x21"


@pytest.mark.parametrize("filename", ["data/bthome_volume_storage.bin"])
def test_bthome_volume_storage(bthome_data):
    """Test BTHome parser for volume storage in liters."""
    assert round(bthome_data.measurement[0].data.volume_storage, 3) == 19551.879
    assert bthome_data.measurement[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_device_type_id.bin"])
def test_bthome_device_type_id(bthome_data):
    """Test BTHome parser for device type ID."""
    assert bthome_data.measurement[0].data.device_type_id == 1


@pytest.mark.parametrize("filename", ["data/bthome_device_fw_version_uint32.bin"])
def test_bthome_device_fw_version_uint32(bthome_data):
    """Test BTHome parser for device firmware version (4 bytes)."""
    assert bthome_data.measurement[0].data.fw_version_major == 4
    assert bthome_data.measurement[0].data.fw_version_minor == 2
    assert bthome_data.measurement[0].data.fw_version_patch == 1
    assert bthome_data.measurement[0].data.fw_version_build == 0


@pytest.mark.parametrize("filename", ["data/bthome_device_fw_version_uint24.bin"])
def test_bthome_device_fw_version_uint24(bthome_data):
    """Test BTHome parser for device firmware version (3 bytes)."""
    assert bthome_data.measurement[0].data.fw_version_major == 6
    assert bthome_data.measurement[0].data.fw_version_minor == 1
    assert bthome_data.measurement[0].data.fw_version_patch == 0


@pytest.mark.parametrize("filename", ["data/bthome_double_temperature.bin"])
def test_bthome_double_temperature(bthome_data):
    """Test BTHome parser for double temperature reading without encryption."""
    assert round(bthome_data.measurement[0].data.temperature, 2) == 25.06
    assert bthome_data.measurement[0].data.unit == "°C"
    assert round(bthome_data.measurement[1].data.temperature, 2) == 25.11
    assert bthome_data.measurement[1].data.unit == "°C"


@pytest.mark.parametrize(
    "filename", ["data/bthome_triple_temperature_double_humidity_battery.bin"]
)
def test_bthome_triple_temperature_double_humidity_battery(bthome_data):
    """
    Test BTHome parser for triple temperature, double humidity and
    single battery reading without encryption.
    """
    assert round(bthome_data.measurement[0].data.temperature, 2) == 25.06
    assert bthome_data.measurement[0].data.unit == "°C"
    assert round(bthome_data.measurement[1].data.temperature, 2) == 25.11
    assert bthome_data.measurement[1].data.unit == "°C"
    assert round(bthome_data.measurement[2].data.temperature, 2) == 22.55
    assert bthome_data.measurement[2].data.unit == "°C"
    assert round(bthome_data.measurement[3].data.humidity, 2) == 63.27
    assert bthome_data.measurement[3].data.unit == "%"
    assert round(bthome_data.measurement[4].data.humidity, 2) == 60.71
    assert bthome_data.measurement[4].data.unit == "%"
    assert bthome_data.measurement[5].data.battery == 93
    assert bthome_data.measurement[5].data.unit == "%"


@pytest.mark.parametrize(
    "filename", ["data/bthome_double_voltage_different_object_id.bin"]
)
def test_bthome_double_voltage_different_object_id(bthome_data):
    """Test BTHome parser for double voltage with different object id."""
    assert bthome_data.measurement[0].data.packet_id == 1
    assert bthome_data.measurement[1].data.power == 0
    assert bthome_data.measurement[1].data.unit == "W"
    assert round(bthome_data.measurement[2].data.voltage, 1) == 231.7
    assert bthome_data.measurement[2].data.unit == "V"
    assert bthome_data.measurement[3].data.battery == 51
    assert bthome_data.measurement[3].data.unit == "%"
    assert round(bthome_data.measurement[4].data.voltage, 3) == 3.305
    assert bthome_data.measurement[4].data.unit == "V"


@pytest.mark.parametrize("filename", ["data/bthome_shelly_button.bin"])
def test_bthome_shelly_button(bthome_data):
    """Test BTHome parser for Shelly button."""
    assert bthome_data.measurement[0].data.packet_id == 82
    assert bthome_data.measurement[1].data.battery == 100
    assert bthome_data.measurement[1].data.unit == "%"
    assert (
        bthome_data.measurement[2].data.event == BthomeServiceData.ButtonEventType.press
    )


@pytest.mark.parametrize("filename", ["data/bthome_shelly_button_encrypted.bin"])
def test_bthome_shelly_button_encrypted(bthome_data):
    """Test BTHome parser for Shelly button with encryption."""
    ciphertext = bthome_data.ciphertext
    counter = binascii.b2a_hex(bthome_data.counter.to_bytes(4, "big")).decode("utf-8")
    mic = bthome_data.mic.to_bytes(4, "big")
    address = "bc026ec3ba95"
    uuid16 = "d2fc"
    device_information = "45"
    bindkey = binascii.unhexlify("a0bcc8ba8aa8bb1a8e98d89eadbf13db")
    nonce = binascii.unhexlify("".join([address, uuid16, device_information, counter]))
    decrypted_data = decrypt_payload(ciphertext, mic, bindkey, nonce)
    bthome_service_data = bytearray([0x44])
    bthome_service_data.extend(decrypted_data)
    bthome_service_data = BthomeServiceData.from_bytes(bthome_service_data)

    assert bthome_service_data.measurement[0].data.packet_id == 9
    assert bthome_service_data.measurement[1].data.battery == 100
    assert bthome_service_data.measurement[1].data.unit == "%"
    assert (
        bthome_service_data.measurement[2].data.event
        == BthomeServiceData.ButtonEventType.press
    )


@pytest.mark.parametrize("filename", ["data/bthome_temperature_humidity_encrypted.bin"])
def test_bthome_temperature_humidity_encrypted(bthome_data):
    """Test BTHome parser for temperature humidity reading with encryption."""
    ciphertext = bthome_data.ciphertext
    counter = binascii.b2a_hex(bthome_data.counter.to_bytes(4, "big")).decode("utf-8")
    mic = bthome_data.mic.to_bytes(4, "big")
    address = "5448e68f80a5"
    uuid16 = "d2fc"
    device_information = "41"
    bindkey = binascii.unhexlify("231d39c1d7cc1ab1aee224cd096db932")
    nonce = binascii.unhexlify("".join([address, uuid16, device_information, counter]))
    decrypted_data = decrypt_payload(ciphertext, mic, bindkey, nonce)
    bthome_service_data = bytearray([0x40])
    bthome_service_data.extend(decrypted_data)
    bthome_service_data = BthomeServiceData.from_bytes(bthome_service_data)

    assert round(bthome_service_data.measurement[0].data.temperature, 2) == 25.06
    assert bthome_service_data.measurement[0].data.unit == "°C"
    assert round(bthome_service_data.measurement[1].data.humidity, 2) == 50.55
    assert bthome_service_data.measurement[1].data.unit == "%"
