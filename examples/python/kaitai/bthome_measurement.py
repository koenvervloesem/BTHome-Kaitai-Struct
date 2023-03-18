# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class BthomeMeasurement(KaitaiStruct):
    """Unencrypted BLE advertising in the BTHome v2 format
    
    .. seealso::
       Source - https://bthome.io/format/
    """

    class BthomeObjectId(Enum):
        misc_packet_id = 0
        sensor_battery = 1
        sensor_temperature_0_01 = 2
        sensor_humidity_0_01 = 3
        sensor_pressure_0_01 = 4
        sensor_illuminance_0_01 = 5
        sensor_mass_kg_0_01 = 6
        sensor_mass_lb_0_01 = 7
        sensor_dewpoint_0_01 = 8
        sensor_count = 9
        sensor_energy_0_001 = 10
        sensor_power_0_01 = 11
        sensor_voltage_0_001 = 12
        sensor_pm2_5 = 13
        sensor_pm10 = 14
        binary_generic_boolean = 15
        binary_power = 16
        binary_opening = 17
        sensor_co2 = 18
        sensor_tvoc = 19
        sensor_moisture_0_01 = 20
        binary_battery = 21
        binary_battery_charging = 22
        binary_carbon_monoxide = 23
        binary_cold = 24
        binary_connectivity = 25
        binary_door = 26
        binary_garage_door = 27
        binary_gas = 28
        binary_heat = 29
        binary_light = 30
        binary_lock = 31
        binary_moisture = 32
        binary_motion = 33
        binary_moving = 34
        binary_occupancy = 35
        binary_plug = 36
        binary_presence = 37
        binary_problem = 38
        binary_running = 39
        binary_safety = 40
        binary_smoke = 41
        binary_sound = 42
        binary_tamper = 43
        binary_vibration = 44
        binary_window = 45
        sensor_humidity = 46
        sensor_moisture = 47
        event_button = 58
        event_dimmer = 60
        sensor_count_uint16 = 61
        sensor_count_uint32 = 62
        sensor_rotation_0_1 = 63
        sensor_distance_mm = 64
        sensor_distance_m_0_1 = 65
        sensor_duration_0_001 = 66
        sensor_current_0_001 = 67
        sensor_speed_0_01 = 68
        sensor_temperature_0_1 = 69
        sensor_uv_index_0_1 = 70
        sensor_volume_0_1 = 71
        sensor_volume = 72
        sensor_volume_flow_rate_0_001 = 73
        sensor_voltage_0_1 = 74
        sensor_gas = 75
        sensor_gas_uint32 = 76
        sensor_energy_0_001_uint32 = 77
        sensor_volume_0_001 = 78

    class ButtonEventType(Enum):
        none = 0
        press = 1
        double_press = 2
        triple_press = 3
        long_press = 4
        long_double_press = 5
        long_triple_press = 6

    class DimmerEventType(Enum):
        none = 0
        rotate_left = 1
        rotate_right = 2
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.object_id = KaitaiStream.resolve_enum(BthomeMeasurement.BthomeObjectId, self._io.read_u1())
        _on = self.object_id
        if _on == BthomeMeasurement.BthomeObjectId.sensor_mass_lb_0_01:
            self.data = BthomeMeasurement.BthomeSensorMassLb001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_moving:
            self.data = BthomeMeasurement.BthomeBinaryMoving(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_moisture:
            self.data = BthomeMeasurement.BthomeBinaryMoisture(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_humidity_0_01:
            self.data = BthomeMeasurement.BthomeSensorHumidity001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_distance_mm:
            self.data = BthomeMeasurement.BthomeSensorDistanceMm(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_uv_index_0_1:
            self.data = BthomeMeasurement.BthomeSensorUvIndex01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_moisture_0_01:
            self.data = BthomeMeasurement.BthomeSensorMoisture001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_gas:
            self.data = BthomeMeasurement.BthomeSensorGas(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_motion:
            self.data = BthomeMeasurement.BthomeBinaryMotion(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_energy_0_001:
            self.data = BthomeMeasurement.BthomeSensorEnergy0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_temperature_0_01:
            self.data = BthomeMeasurement.BthomeSensorTemperature001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_opening:
            self.data = BthomeMeasurement.BthomeBinaryOpening(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_dewpoint_0_01:
            self.data = BthomeMeasurement.BthomeSensorDewpoint001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_smoke:
            self.data = BthomeMeasurement.BthomeBinarySmoke(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_co2:
            self.data = BthomeMeasurement.BthomeSensorCo2(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_sound:
            self.data = BthomeMeasurement.BthomeBinarySound(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.misc_packet_id:
            self.data = BthomeMeasurement.BthomeMiscPacketId(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_volume_flow_rate_0_001:
            self.data = BthomeMeasurement.BthomeSensorVolumeFlowRate0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_volume_0_001:
            self.data = BthomeMeasurement.BthomeSensorVolume0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_occupancy:
            self.data = BthomeMeasurement.BthomeBinaryOccupancy(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_door:
            self.data = BthomeMeasurement.BthomeBinaryDoor(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_volume:
            self.data = BthomeMeasurement.BthomeSensorVolume(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_generic_boolean:
            self.data = BthomeMeasurement.BthomeBinaryGenericBoolean(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_power_0_01:
            self.data = BthomeMeasurement.BthomeSensorPower001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_light:
            self.data = BthomeMeasurement.BthomeBinaryLight(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_window:
            self.data = BthomeMeasurement.BthomeBinaryWindow(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_count_uint32:
            self.data = BthomeMeasurement.BthomeSensorCountUint32(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_current_0_001:
            self.data = BthomeMeasurement.BthomeSensorCurrent0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_mass_kg_0_01:
            self.data = BthomeMeasurement.BthomeSensorMassKg001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_presence:
            self.data = BthomeMeasurement.BthomeBinaryPresence(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_gas:
            self.data = BthomeMeasurement.BthomeBinaryGas(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_garage_door:
            self.data = BthomeMeasurement.BthomeBinaryGarageDoor(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_connectivity:
            self.data = BthomeMeasurement.BthomeBinaryConnectivity(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_problem:
            self.data = BthomeMeasurement.BthomeBinaryProblem(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_distance_m_0_1:
            self.data = BthomeMeasurement.BthomeSensorDistanceM01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_running:
            self.data = BthomeMeasurement.BthomeBinaryRunning(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.event_button:
            self.data = BthomeMeasurement.BthomeEventButton(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_tamper:
            self.data = BthomeMeasurement.BthomeBinaryTamper(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_voltage_0_001:
            self.data = BthomeMeasurement.BthomeSensorVoltage0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_plug:
            self.data = BthomeMeasurement.BthomeBinaryPlug(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_battery_charging:
            self.data = BthomeMeasurement.BthomeBinaryBatteryCharging(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_tvoc:
            self.data = BthomeMeasurement.BthomeSensorTvoc(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_duration_0_001:
            self.data = BthomeMeasurement.BthomeSensorDuration0001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_lock:
            self.data = BthomeMeasurement.BthomeBinaryLock(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_battery:
            self.data = BthomeMeasurement.BthomeSensorBattery(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_cold:
            self.data = BthomeMeasurement.BthomeBinaryCold(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_pressure_0_01:
            self.data = BthomeMeasurement.BthomeSensorPressure001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_volume_0_1:
            self.data = BthomeMeasurement.BthomeSensorVolume01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_voltage_0_1:
            self.data = BthomeMeasurement.BthomeSensorVoltage01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_illuminance_0_01:
            self.data = BthomeMeasurement.BthomeSensorIlluminance001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_temperature_0_1:
            self.data = BthomeMeasurement.BthomeSensorTemperature01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_battery:
            self.data = BthomeMeasurement.BthomeBinaryBattery(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_count_uint16:
            self.data = BthomeMeasurement.BthomeSensorCountUint16(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_gas_uint32:
            self.data = BthomeMeasurement.BthomeSensorGasUint32(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_power:
            self.data = BthomeMeasurement.BthomeBinaryPower(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_count:
            self.data = BthomeMeasurement.BthomeSensorCount(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_humidity:
            self.data = BthomeMeasurement.BthomeSensorHumidity(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_carbon_monoxide:
            self.data = BthomeMeasurement.BthomeBinaryCarbonMonoxide(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_heat:
            self.data = BthomeMeasurement.BthomeBinaryHeat(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_pm10:
            self.data = BthomeMeasurement.BthomeSensorPm10(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_rotation_0_1:
            self.data = BthomeMeasurement.BthomeSensorRotation01(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_speed_0_01:
            self.data = BthomeMeasurement.BthomeSensorSpeed001(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.event_dimmer:
            self.data = BthomeMeasurement.BthomeEventDimmer(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_energy_0_001_uint32:
            self.data = BthomeMeasurement.BthomeSensorEnergy0001Uint32(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_safety:
            self.data = BthomeMeasurement.BthomeBinarySafety(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.binary_vibration:
            self.data = BthomeMeasurement.BthomeBinaryVibration(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_pm2_5:
            self.data = BthomeMeasurement.BthomeSensorPm25(self._io, self, self._root)
        elif _on == BthomeMeasurement.BthomeObjectId.sensor_moisture:
            self.data = BthomeMeasurement.BthomeSensorMoisture(self._io, self, self._root)
        else:
            self.data = BthomeMeasurement.BthomeUnknown(self._io, self, self._root)

    class BthomeSensorEnergy0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def energy(self):
            if hasattr(self, '_m_energy'):
                return self._m_energy if hasattr(self, '_m_energy') else None

            self._m_energy = (self.value.value * 0.001)
            return self._m_energy if hasattr(self, '_m_energy') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"kWh"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorCountUint32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u4le()


    class BthomeSensorBattery(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.battery = self._io.read_u1()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"%"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorCo2(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.co2 = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"ppm"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorVoltage0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def voltage(self):
            if hasattr(self, '_m_voltage'):
                return self._m_voltage if hasattr(self, '_m_voltage') else None

            self._m_voltage = (self.value * 0.001)
            return self._m_voltage if hasattr(self, '_m_voltage') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"V"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryWindow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.window = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorCurrent0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def current(self):
            if hasattr(self, '_m_current'):
                return self._m_current if hasattr(self, '_m_current') else None

            self._m_current = (self.value * 0.001)
            return self._m_current if hasattr(self, '_m_current') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"A"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorVolume01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def volume(self):
            if hasattr(self, '_m_volume'):
                return self._m_volume if hasattr(self, '_m_volume') else None

            self._m_volume = (self.value * 0.1)
            return self._m_volume if hasattr(self, '_m_volume') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"L"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryConnectivity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.connectivity = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorPm10(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pm10 = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\265g/m\263"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinarySound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sound = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeEventDimmer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.event = KaitaiStream.resolve_enum(BthomeMeasurement.DimmerEventType, self._io.read_u1())
            if  ((self.event == BthomeMeasurement.DimmerEventType.rotate_left) or (self.event == BthomeMeasurement.DimmerEventType.rotate_right)) :
                self.steps = self._io.read_u1()



    class BthomeSensorGasUint32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def gas(self):
            if hasattr(self, '_m_gas'):
                return self._m_gas if hasattr(self, '_m_gas') else None

            self._m_gas = (self.value * 0.001)
            return self._m_gas if hasattr(self, '_m_gas') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"m\263"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorPm25(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pm2_5 = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\265g/m\263"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorVolume(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.volume = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"mL"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryMoving(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.moving = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeMiscPacketId(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.packet_id = self._io.read_u1()


    class BthomeSensorTemperature01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s2le()

        @property
        def temperature(self):
            if hasattr(self, '_m_temperature'):
                return self._m_temperature if hasattr(self, '_m_temperature') else None

            self._m_temperature = (self.value * 0.1)
            return self._m_temperature if hasattr(self, '_m_temperature') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\260C"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryVibration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vibration = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryBattery(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.battery = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryPower(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.power = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorEnergy0001Uint32(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def energy(self):
            if hasattr(self, '_m_energy'):
                return self._m_energy if hasattr(self, '_m_energy') else None

            self._m_energy = (self.value * 0.001)
            return self._m_energy if hasattr(self, '_m_energy') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"kWh"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryOpening(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.opening = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorPressure001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def pressure(self):
            if hasattr(self, '_m_pressure'):
                return self._m_pressure if hasattr(self, '_m_pressure') else None

            self._m_pressure = (self.value.value * 0.01)
            return self._m_pressure if hasattr(self, '_m_pressure') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"hPa"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeEventButton(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.event = KaitaiStream.resolve_enum(BthomeMeasurement.ButtonEventType, self._io.read_u1())


    class BthomeSensorCountUint16(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u2le()


    class BthomeUnknown(KaitaiStruct):
        """Data with unknown object ID are parsed as a byte array until the end."""
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown = self._io.read_bytes_full()


    class BthomeSensorTvoc(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tvoc = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\265g/m\263"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorDistanceMm(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.distance = self._io.read_u2le()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"mm"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryPresence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.presence = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryMoisture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.moisture = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorGas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def gas(self):
            if hasattr(self, '_m_gas'):
                return self._m_gas if hasattr(self, '_m_gas') else None

            self._m_gas = (self.value.value * 0.001)
            return self._m_gas if hasattr(self, '_m_gas') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"m\263"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorIlluminance001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def illuminance(self):
            if hasattr(self, '_m_illuminance'):
                return self._m_illuminance if hasattr(self, '_m_illuminance') else None

            self._m_illuminance = (self.value.value * 0.01)
            return self._m_illuminance if hasattr(self, '_m_illuminance') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"lux"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorMassLb001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def mass(self):
            if hasattr(self, '_m_mass'):
                return self._m_mass if hasattr(self, '_m_mass') else None

            self._m_mass = (self.value * 0.01)
            return self._m_mass if hasattr(self, '_m_mass') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"lb"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorTemperature001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s2le()

        @property
        def temperature(self):
            if hasattr(self, '_m_temperature'):
                return self._m_temperature if hasattr(self, '_m_temperature') else None

            self._m_temperature = (self.value * 0.01)
            return self._m_temperature if hasattr(self, '_m_temperature') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\260C"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryCold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cold = BthomeMeasurement.Bool8(self._io, self, self._root)


    class Bool8(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.int_value = self._io.read_u1()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = (True if (self.int_value & 1) == 1 else False)
            return self._m_value if hasattr(self, '_m_value') else None


    class BthomeBinaryHeat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.heat = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryDoor(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.door = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryLock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.lock = BthomeMeasurement.Bool8(self._io, self, self._root)


    class U3(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.low_byte = self._io.read_u1()
            self.middle_byte = self._io.read_u1()
            self.high_byte = self._io.read_u1()

        @property
        def value(self):
            if hasattr(self, '_m_value'):
                return self._m_value if hasattr(self, '_m_value') else None

            self._m_value = ((self.low_byte | (self.middle_byte << 8)) | (self.high_byte << 16))
            return self._m_value if hasattr(self, '_m_value') else None


    class BthomeBinaryGarageDoor(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.garage_door = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorMassKg001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def mass(self):
            if hasattr(self, '_m_mass'):
                return self._m_mass if hasattr(self, '_m_mass') else None

            self._m_mass = (self.value * 0.01)
            return self._m_mass if hasattr(self, '_m_mass') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"kg"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorSpeed001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def speed(self):
            if hasattr(self, '_m_speed'):
                return self._m_speed if hasattr(self, '_m_speed') else None

            self._m_speed = (self.value * 0.01)
            return self._m_speed if hasattr(self, '_m_speed') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"m/s"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorDewpoint001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s2le()

        @property
        def dew_point(self):
            if hasattr(self, '_m_dew_point'):
                return self._m_dew_point if hasattr(self, '_m_dew_point') else None

            self._m_dew_point = (self.value * 0.01)
            return self._m_dew_point if hasattr(self, '_m_dew_point') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\260C"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryOccupancy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.occupancy = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorCount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u1()


    class BthomeSensorMoisture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.moisture = self._io.read_u1()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"%"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryRunning(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.running = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryPlug(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.plug = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorPower001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def power(self):
            if hasattr(self, '_m_power'):
                return self._m_power if hasattr(self, '_m_power') else None

            self._m_power = (self.value.value * 0.01)
            return self._m_power if hasattr(self, '_m_power') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"W"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryMotion(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.motion = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryTamper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tamper = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryBatteryCharging(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.battery_charging = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorVolume0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def volume(self):
            if hasattr(self, '_m_volume'):
                return self._m_volume if hasattr(self, '_m_volume') else None

            self._m_volume = (self.value * 0.001)
            return self._m_volume if hasattr(self, '_m_volume') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"L"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorDistanceM01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s2le()

        @property
        def distance(self):
            if hasattr(self, '_m_distance'):
                return self._m_distance if hasattr(self, '_m_distance') else None

            self._m_distance = (self.value * 0.1)
            return self._m_distance if hasattr(self, '_m_distance') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"m"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorHumidity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.humidity = self._io.read_u1()

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"%"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryCarbonMonoxide(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.carbon_monoxide = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinaryLight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.light = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeBinarySafety(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.safety = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorHumidity001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def humidity(self):
            if hasattr(self, '_m_humidity'):
                return self._m_humidity if hasattr(self, '_m_humidity') else None

            self._m_humidity = (self.value * 0.01)
            return self._m_humidity if hasattr(self, '_m_humidity') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"%"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorMoisture001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def moisture(self):
            if hasattr(self, '_m_moisture'):
                return self._m_moisture if hasattr(self, '_m_moisture') else None

            self._m_moisture = (self.value * 0.01)
            return self._m_moisture if hasattr(self, '_m_moisture') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"%"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorVolumeFlowRate0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def volume_flow_rate(self):
            if hasattr(self, '_m_volume_flow_rate'):
                return self._m_volume_flow_rate if hasattr(self, '_m_volume_flow_rate') else None

            self._m_volume_flow_rate = (self.value * 0.001)
            return self._m_volume_flow_rate if hasattr(self, '_m_volume_flow_rate') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"m\263/hr"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinarySmoke(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.smoke = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorUvIndex01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u1()

        @property
        def uv_index(self):
            if hasattr(self, '_m_uv_index'):
                return self._m_uv_index if hasattr(self, '_m_uv_index') else None

            self._m_uv_index = (self.value * 0.1)
            return self._m_uv_index if hasattr(self, '_m_uv_index') else None


    class BthomeBinaryProblem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.problem = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorVoltage01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def voltage(self):
            if hasattr(self, '_m_voltage'):
                return self._m_voltage if hasattr(self, '_m_voltage') else None

            self._m_voltage = (self.value * 0.1)
            return self._m_voltage if hasattr(self, '_m_voltage') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"V"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeSensorRotation01(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_s2le()

        @property
        def rotation(self):
            if hasattr(self, '_m_rotation'):
                return self._m_rotation if hasattr(self, '_m_rotation') else None

            self._m_rotation = (self.value * 0.1)
            return self._m_rotation if hasattr(self, '_m_rotation') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"\260"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryGas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.gas = BthomeMeasurement.Bool8(self._io, self, self._root)


    class BthomeSensorDuration0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeMeasurement.U3(self._io, self, self._root)

        @property
        def duration(self):
            if hasattr(self, '_m_duration'):
                return self._m_duration if hasattr(self, '_m_duration') else None

            self._m_duration = (self.value.value * 0.001)
            return self._m_duration if hasattr(self, '_m_duration') else None

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit if hasattr(self, '_m_unit') else None

            self._m_unit = u"s"
            return self._m_unit if hasattr(self, '_m_unit') else None


    class BthomeBinaryGenericBoolean(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.generic_boolean = BthomeMeasurement.Bool8(self._io, self, self._root)



