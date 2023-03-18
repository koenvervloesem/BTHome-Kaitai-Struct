"""Tests for Python module generated from BTHome Kaitai Struct files."""
import pytest

from examples.python.kaitai.bthome_service_data import BthomeServiceData
from examples.python.kaitai.bthome_measurement import BthomeMeasurement


@pytest.fixture
def bthome_data(filename):
    """Return BTHome service data from the given file."""
    with open(filename, "rb") as data_file:
        return BthomeServiceData.from_bytes(data_file.read())


@pytest.mark.parametrize("filename", ["data/bthome_wrong_object_id.bin"])
def test_bthome_wrong_object_id(bthome_data):
    """Test BTHome parser for a non-existing Object ID xFE."""
    assert bthome_data.measurements[0].data.unknown == b"\xca\x09"


@pytest.mark.parametrize(
    "filename", ["data/bthome_battery_wrong_object_id_humidity.bin"]
)
def test_bthome_battery_wrong_object_id_humidity(bthome_data):
    """Test BTHome parser for battery, wrong object id and humidity reading.

    Should only return the battery reading, as humidity is after wrong object id.
    """
    assert bthome_data.measurements[0].data.battery == 93
    assert bthome_data.measurements[0].data.unit == "%"
    assert bthome_data.measurements[1].data.unknown == b"\x5d\x09\x03\xb7\x18"


@pytest.mark.parametrize("filename", ["data/bthome_with_mac.bin"])
def test_bthome_with_mac(bthome_data):
    """Test BTHome parser for pressure reading with MAC address in payload."""
    assert bthome_data.mac_reversed == bytes([0xB2, 0x18, 0x8D, 0x38, 0xC1, 0xA4])
    assert round(bthome_data.measurements[0].data.pressure, 2) == 1008.83
    assert bthome_data.measurements[0].data.unit == "hPa"


@pytest.mark.parametrize("filename", ["data/bthome_temperature_humidity.bin"])
def test_bthome_temperature_humidity(bthome_data):
    """Test BTHome parser for temperature humidity reading without encryption."""
    assert round(bthome_data.measurements[0].data.temperature, 2) == 25.06
    assert bthome_data.measurements[0].data.unit == "°C"
    assert round(bthome_data.measurements[1].data.humidity, 2) == 50.55
    assert bthome_data.measurements[1].data.unit == "%"


@pytest.mark.parametrize(
    "filename", ["data/bthome_packet_id_temperature_humidity_battery.bin"]
)
def test_bthome_packet_id_temperature_humidity_battery(bthome_data):
    """Test BTHome parser for packet_id, temperature, humidity and battery reading."""
    assert bthome_data.measurements[0].data.packet_id == 9
    assert bthome_data.measurements[1].data.battery == 93
    assert bthome_data.measurements[1].data.unit == "%"
    assert round(bthome_data.measurements[2].data.temperature, 2) == 23.97
    assert bthome_data.measurements[2].data.unit == "°C"
    assert round(bthome_data.measurements[3].data.humidity, 2) == 63.27
    assert bthome_data.measurements[3].data.unit == "%"


@pytest.mark.parametrize("filename", ["data/bthome_pressure.bin"])
def test_bthome_pressure(bthome_data):
    """Test BTHome parser for pressure reading without encryption."""
    assert round(bthome_data.measurements[0].data.pressure, 2) == 1008.83
    assert bthome_data.measurements[0].data.unit == "hPa"


@pytest.mark.parametrize("filename", ["data/bthome_illuminance.bin"])
def test_bthome_illuminance(bthome_data):
    """Test BTHome parser for illuminance reading without encryption."""
    assert round(bthome_data.measurements[0].data.illuminance, 2) == 13460.67
    assert bthome_data.measurements[0].data.unit == "lux"


@pytest.mark.parametrize("filename", ["data/bthome_mass_kilograms.bin"])
def test_bthome_mass_kilograms(bthome_data):
    """Test BTHome parser for mass reading in kilograms without encryption."""
    assert round(bthome_data.measurements[0].data.mass, 2) == 80.3
    assert bthome_data.measurements[0].data.unit == "kg"


@pytest.mark.parametrize("filename", ["data/bthome_mass_pounds.bin"])
def test_bthome_mass_pounds(bthome_data):
    """Test BTHome parser for mass reading in pounds without encryption."""
    assert round(bthome_data.measurements[0].data.mass, 2) == 74.86
    assert bthome_data.measurements[0].data.unit == "lb"


@pytest.mark.parametrize("filename", ["data/bthome_dew_point.bin"])
def test_bthome_dew_point(bthome_data):
    """Test BTHome parser for dew point reading without encryption."""
    assert round(bthome_data.measurements[0].data.dew_point, 2) == 17.38
    assert bthome_data.measurements[0].data.unit == "°C"


@pytest.mark.parametrize("filename", ["data/bthome_count.bin"])
def test_bthome_count(bthome_data):
    """Test BTHome parser for counter reading without encryption."""
    assert bthome_data.measurements[0].data.count == 96


@pytest.mark.parametrize("filename", ["data/bthome_energy.bin"])
def test_bthome_energy(bthome_data):
    """Test BTHome parser for energy reading without encryption."""
    assert round(bthome_data.measurements[0].data.energy, 3) == 1346.067
    assert bthome_data.measurements[0].data.unit == "kWh"


@pytest.mark.parametrize("filename", ["data/bthome_power.bin"])
def test_bthome_power(bthome_data):
    """Test BTHome parser for power reading without encryption."""
    assert round(bthome_data.measurements[0].data.power, 2) == 69.14
    assert bthome_data.measurements[0].data.unit == "W"


@pytest.mark.parametrize("filename", ["data/bthome_voltage.bin"])
def test_bthome_voltage(bthome_data):
    """Test BTHome parser for voltage reading without encryption."""
    assert round(bthome_data.measurements[0].data.voltage, 3) == 3.074
    assert bthome_data.measurements[0].data.unit == "V"


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor.bin"])
def test_bthome_binary_sensor(bthome_data):
    """Test BTHome parser for binary sensor without device class, without encryption."""
    assert bthome_data.measurements[0].data.generic_boolean.value


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor_power.bin"])
def test_bthome_binary_sensor_power(bthome_data):
    """Test BTHome parser for binary sensor power without encryption."""
    assert bthome_data.measurements[0].data.power.value


@pytest.mark.parametrize("filename", ["data/bthome_binary_sensor_opening.bin"])
def test_bthome_binary_sensor_opening(bthome_data):
    """Test BTHome parser for binary sensor opening without encryption."""
    assert bthome_data.measurements[0].data.opening.value is False


@pytest.mark.parametrize("filename", ["data/bthome_pm.bin"])
def test_bthome_pm(bthome_data):
    """Test BTHome parser for PM2.5 and PM10 reading without encryption."""
    assert bthome_data.measurements[0].data.pm2_5 == 3090
    assert bthome_data.measurements[0].data.unit == "µg/m³"
    assert bthome_data.measurements[1].data.pm10 == 7170
    assert bthome_data.measurements[1].data.unit == "µg/m³"


@pytest.mark.parametrize("filename", ["data/bthome_co2.bin"])
def test_bthome_co2(bthome_data):
    """Test BTHome parser for CO2 reading without encryption."""
    assert bthome_data.measurements[0].data.co2 == 1250
    assert bthome_data.measurements[0].data.unit == "ppm"


@pytest.mark.parametrize("filename", ["data/bthome_voc.bin"])
def test_bthome_voc(bthome_data):
    """Test BTHome parser for VOC reading without encryption."""
    assert bthome_data.measurements[0].data.tvoc == 307
    assert bthome_data.measurements[0].data.unit == "µg/m³"


@pytest.mark.parametrize("filename", ["data/bthome_moisture.bin"])
def test_bthome_moisture(bthome_data):
    """Test BTHome parser for moisture reading from b-parasite sensor."""
    assert round(bthome_data.measurements[0].data.moisture, 2) == 30.74
    assert bthome_data.measurements[0].data.unit == "%"


@pytest.mark.parametrize("filename", ["data/bthome_event_button_long_press.bin"])
def test_bthome_event_button_long_press(bthome_data):
    """Test BTHome parser for an event of a long press on a button without encryption."""
    assert (
        bthome_data.measurements[0].data.event
        == BthomeMeasurement.ButtonEventType.long_press
    )


@pytest.mark.parametrize("filename", ["data/bthome_event_triple_button_device.bin"])
def test_bthome_event_triple_button_device(bthome_data):
    """
    Test BTHome parser for an event of a triple button device where
    the 2nd button is pressed and the 3rd button is triple pressed.
    """
    assert (
        bthome_data.measurements[0].data.event == BthomeMeasurement.ButtonEventType.none
    )
    assert (
        bthome_data.measurements[1].data.event
        == BthomeMeasurement.ButtonEventType.press
    )
    assert (
        bthome_data.measurements[2].data.event
        == BthomeMeasurement.ButtonEventType.triple_press
    )


@pytest.mark.parametrize(
    "filename", ["data/bthome_event_dimmer_rotate_left_3_steps.bin"]
)
def test_bthome_event_dimmer_rotate_left_3_steps(bthome_data):
    """Test BTHome parser for an event rotating a dimmer 3 steps left."""
    assert (
        bthome_data.measurements[0].data.event
        == BthomeMeasurement.DimmerEventType.rotate_left
    )
    assert bthome_data.measurements[0].data.steps == 3


@pytest.mark.parametrize("filename", ["data/bthome_rotation.bin"])
def test_bthome_rotation(bthome_data):
    """Test BTHome parser for rotation."""
    assert round(bthome_data.measurements[0].data.rotation, 1) == 307.4
    assert bthome_data.measurements[0].data.unit == "°"


@pytest.mark.parametrize("filename", ["data/bthome_distance_millimeters.bin"])
def test_bthome_distance_millimeters(bthome_data):
    """Test BTHome parser for distance in millimeters."""
    assert bthome_data.measurements[0].data.distance == 12
    assert bthome_data.measurements[0].data.unit == "mm"


@pytest.mark.parametrize("filename", ["data/bthome_distance_meters.bin"])
def test_bthome_distance_meters(bthome_data):
    """Test BTHome parser for distance in meters."""
    assert round(bthome_data.measurements[0].data.distance, 1) == 7.8
    assert bthome_data.measurements[0].data.unit == "m"


@pytest.mark.parametrize("filename", ["data/bthome_duration.bin"])
def test_bthome_duration(bthome_data):
    """Test BTHome parser for duration in seconds."""
    assert round(bthome_data.measurements[0].data.duration, 3) == 13.39
    assert bthome_data.measurements[0].data.unit == "s"


@pytest.mark.parametrize("filename", ["data/bthome_current.bin"])
def test_bthome_current(bthome_data):
    """Test BTHome parser for current in A."""
    assert round(bthome_data.measurements[0].data.current, 3) == 13.39
    assert bthome_data.measurements[0].data.unit == "A"


@pytest.mark.parametrize("filename", ["data/bthome_speed.bin"])
def test_bthome_speed(bthome_data):
    """Test BTHome parser for speed in m/s."""
    assert round(bthome_data.measurements[0].data.speed, 2) == 133.9
    assert bthome_data.measurements[0].data.unit == "m/s"


@pytest.mark.parametrize("filename", ["data/bthome_temperature_2.bin"])
def test_bthome_temperature_2(bthome_data):
    """Test BTHome parser for temperature with one digit."""
    assert round(bthome_data.measurements[0].data.temperature, 1) == 27.3
    assert bthome_data.measurements[0].data.unit == "°C"


@pytest.mark.parametrize("filename", ["data/bthome_uv_index.bin"])
def test_bthome_uv_index(bthome_data):
    """Test BTHome parser for UV index."""
    assert round(bthome_data.measurements[0].data.uv_index, 1) == 5.0


@pytest.mark.parametrize("filename", ["data/bthome_volume_liters.bin"])
def test_bthome_volume_liters(bthome_data):
    """Test BTHome parser for volume in liters."""
    assert round(bthome_data.measurements[0].data.volume, 1) == 2215.1
    assert bthome_data.measurements[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_volume_milliliters.bin"])
def test_bthome_volume_milliliters(bthome_data):
    """Test BTHome parser for volume in milliliters."""
    assert bthome_data.measurements[0].data.volume == 34780
    assert bthome_data.measurements[0].data.unit == "mL"


@pytest.mark.parametrize("filename", ["data/bthome_volume_flow_rate.bin"])
def test_bthome_volume_flow_rate(bthome_data):
    """Test BTHome parser for volume flow rate in m³ per hour."""
    assert round(bthome_data.measurements[0].data.volume_flow_rate, 3) == 34.780
    assert bthome_data.measurements[0].data.unit == "m³/hr"


@pytest.mark.parametrize("filename", ["data/bthome_voltage_2.bin"])
def test_bthome_voltage_2(bthome_data):
    """Test BTHome parser for voltage reading without encryption."""
    assert round(bthome_data.measurements[0].data.voltage, 1) == 307.4
    assert bthome_data.measurements[0].data.unit == "V"


@pytest.mark.parametrize("filename", ["data/bthome_gas.bin"])
def test_bthome_gas(bthome_data):
    """Test BTHome parser for gas reading without encryption."""
    assert round(bthome_data.measurements[0].data.gas, 3) == 1346.067
    assert bthome_data.measurements[0].data.unit == "m³"


@pytest.mark.parametrize("filename", ["data/bthome_gas_2.bin"])
def test_bthome_gas_2(bthome_data):
    """Test BTHome parser for uint32 gas reading without encryption."""
    assert round(bthome_data.measurements[0].data.gas, 3) == 25821.505
    assert bthome_data.measurements[0].data.unit == "m³"


@pytest.mark.parametrize("filename", ["data/bthome_energy_2.bin"])
def test_bthome_energy_2(bthome_data):
    """Test BTHome parser for uint32 energy reading without encryption."""
    assert round(bthome_data.measurements[0].data.energy, 3) == 344593.17
    assert bthome_data.measurements[0].data.unit == "kWh"


@pytest.mark.parametrize("filename", ["data/bthome_volume_liters_2.bin"])
def test_bthome_volume_liters_2(bthome_data):
    """Test BTHome parser for uint32 volume in liters."""
    assert round(bthome_data.measurements[0].data.volume, 3) == 19551.879
    assert bthome_data.measurements[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_volume_water.bin"])
def test_bthome_volume_water(bthome_data):
    """Test BTHome parser for water in liters."""
    assert round(bthome_data.measurements[0].data.water, 3) == 19551.879
    assert bthome_data.measurements[0].data.unit == "L"


@pytest.mark.parametrize("filename", ["data/bthome_double_temperature.bin"])
def test_bthome_double_temperature(bthome_data):
    """Test BTHome parser for double temperature reading without encryption."""
    assert round(bthome_data.measurements[0].data.temperature, 2) == 25.06
    assert bthome_data.measurements[0].data.unit == "°C"
    assert round(bthome_data.measurements[1].data.temperature, 2) == 25.11
    assert bthome_data.measurements[1].data.unit == "°C"


@pytest.mark.parametrize(
    "filename", ["data/bthome_triple_temperature_double_humidity_battery.bin"]
)
def test_bthome_triple_temperature_double_humidity_battery(bthome_data):
    """
    Test BTHome parser for triple temperature, double humidity and
    single battery reading without encryption.
    """
    assert round(bthome_data.measurements[0].data.temperature, 2) == 25.06
    assert bthome_data.measurements[0].data.unit == "°C"
    assert round(bthome_data.measurements[1].data.temperature, 2) == 25.11
    assert bthome_data.measurements[1].data.unit == "°C"
    assert round(bthome_data.measurements[2].data.temperature, 2) == 22.55
    assert bthome_data.measurements[2].data.unit == "°C"
    assert round(bthome_data.measurements[3].data.humidity, 2) == 63.27
    assert bthome_data.measurements[3].data.unit == "%"
    assert round(bthome_data.measurements[4].data.humidity, 2) == 60.71
    assert bthome_data.measurements[4].data.unit == "%"
    assert bthome_data.measurements[5].data.battery == 93
    assert bthome_data.measurements[5].data.unit == "%"


@pytest.mark.parametrize(
    "filename", ["data/bthome_double_voltage_different_object_id.bin"]
)
def test_bthome_double_voltage_different_object_id(bthome_data):
    """Test BTHome parser for double voltage with different object id."""
    assert bthome_data.measurements[0].data.packet_id == 1
    assert bthome_data.measurements[1].data.power == 0
    assert bthome_data.measurements[1].data.unit == "W"
    assert round(bthome_data.measurements[2].data.voltage, 1) == 231.7
    assert bthome_data.measurements[2].data.unit == "V"
    assert bthome_data.measurements[3].data.battery == 51
    assert bthome_data.measurements[3].data.unit == "%"
    assert round(bthome_data.measurements[4].data.voltage, 3) == 3.305
    assert bthome_data.measurements[4].data.unit == "V"
