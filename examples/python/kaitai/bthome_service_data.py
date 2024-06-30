# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if getattr(kaitaistruct, 'API_VERSION', (0, 9)) < (0, 9):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

class BthomeServiceData(KaitaiStruct):
    """BLE advertising in the BTHome v2 format
    
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
        sensor_water = 79
        sensor_timestamp = 80
        sensor_acceleration = 81
        sensor_gyroscope = 82
        sensor_text = 83
        sensor_raw = 84

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
        self.device_information = BthomeServiceData.BthomeDeviceInformation(self._io, self, self._root)
        if self.device_information.mac_included:
            self.mac_reversed = self._io.read_bytes(6)

        if  ((self.device_information.bthome_version == 2) and (self.device_information.encryption == False)) :
            self.measurement = []
            i = 0
            while not self._io.is_eof():
                self.measurement.append(BthomeServiceData.BthomeMeasurement(self._io, self, self._root))
                i += 1


        if  ((self.device_information.bthome_version == 2) and (self.device_information.encryption == True)) :
            self.ciphertext = self._io.read_bytes((((self._io.size() - self._io.pos()) - 4) - 4))

        if  ((self.device_information.bthome_version == 2) and (self.device_information.encryption == True)) :
            self.counter = self._io.read_u4be()

        if  ((self.device_information.bthome_version == 2) and (self.device_information.encryption == True)) :
            self.mic = self._io.read_u4be()


    class BthomeSensorEnergy0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def energy(self):
            if hasattr(self, '_m_energy'):
                return self._m_energy

            self._m_energy = (self.value.value * 0.001)
            return getattr(self, '_m_energy', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"kWh"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"%"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"ppm"
            return getattr(self, '_m_unit', None)


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
                return self._m_voltage

            self._m_voltage = (self.value * 0.001)
            return getattr(self, '_m_voltage', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"V"
            return getattr(self, '_m_unit', None)


    class BthomeDeviceInformation(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.encryption = self._io.read_bits_int_le(1) != 0
            self.mac_included = self._io.read_bits_int_le(1) != 0
            self.trigger_based = self._io.read_bits_int_le(1) != 0
            self.reserved_for_future_use = self._io.read_bits_int_le(2)
            self.bthome_version = self._io.read_bits_int_le(3)


    class BthomeBinaryWindow(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.window = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_current

            self._m_current = (self.value * 0.001)
            return getattr(self, '_m_current', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"A"
            return getattr(self, '_m_unit', None)


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
                return self._m_volume

            self._m_volume = (self.value * 0.1)
            return getattr(self, '_m_volume', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"L"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryConnectivity(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.connectivity = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_unit

            self._m_unit = u"\265g/m\263"
            return getattr(self, '_m_unit', None)


    class BthomeBinarySound(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.sound = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorAcceleration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def acceleration(self):
            if hasattr(self, '_m_acceleration'):
                return self._m_acceleration

            self._m_acceleration = (self.value * 0.001)
            return getattr(self, '_m_acceleration', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m/s\262"
            return getattr(self, '_m_unit', None)


    class BthomeEventDimmer(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.event = KaitaiStream.resolve_enum(BthomeServiceData.DimmerEventType, self._io.read_u1())
            if  ((self.event == BthomeServiceData.DimmerEventType.rotate_left) or (self.event == BthomeServiceData.DimmerEventType.rotate_right)) :
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
                return self._m_gas

            self._m_gas = (self.value * 0.001)
            return getattr(self, '_m_gas', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m\263"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"\265g/m\263"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"mL"
            return getattr(self, '_m_unit', None)


    class BthomeSensorTimestamp(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()


    class BthomeBinaryMoving(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.moving = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_temperature

            self._m_temperature = (self.value * 0.1)
            return getattr(self, '_m_temperature', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"\260C"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryVibration(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.vibration = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryBattery(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.battery = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryPower(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.power = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_energy

            self._m_energy = (self.value * 0.001)
            return getattr(self, '_m_energy', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"kWh"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryOpening(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.opening = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorPressure001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def pressure(self):
            if hasattr(self, '_m_pressure'):
                return self._m_pressure

            self._m_pressure = (self.value.value * 0.01)
            return getattr(self, '_m_pressure', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"hPa"
            return getattr(self, '_m_unit', None)


    class BthomeEventButton(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.event = KaitaiStream.resolve_enum(BthomeServiceData.ButtonEventType, self._io.read_u1())


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
                return self._m_unit

            self._m_unit = u"\265g/m\263"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"mm"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryPresence(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.presence = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryMoisture(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.moisture = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorGas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def gas(self):
            if hasattr(self, '_m_gas'):
                return self._m_gas

            self._m_gas = (self.value.value * 0.001)
            return getattr(self, '_m_gas', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m\263"
            return getattr(self, '_m_unit', None)


    class BthomeSensorIlluminance001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def illuminance(self):
            if hasattr(self, '_m_illuminance'):
                return self._m_illuminance

            self._m_illuminance = (self.value.value * 0.01)
            return getattr(self, '_m_illuminance', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"lux"
            return getattr(self, '_m_unit', None)


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
                return self._m_mass

            self._m_mass = (self.value * 0.01)
            return getattr(self, '_m_mass', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"lb"
            return getattr(self, '_m_unit', None)


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
                return self._m_temperature

            self._m_temperature = (self.value * 0.01)
            return getattr(self, '_m_temperature', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"\260C"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryCold(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.cold = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_value

            self._m_value = (True if (self.int_value & 1) == 1 else False)
            return getattr(self, '_m_value', None)


    class BthomeBinaryHeat(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.heat = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryDoor(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.door = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryLock(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.lock = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_value

            self._m_value = ((self.low_byte | (self.middle_byte << 8)) | (self.high_byte << 16))
            return getattr(self, '_m_value', None)


    class BthomeBinaryGarageDoor(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.garage_door = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_mass

            self._m_mass = (self.value * 0.01)
            return getattr(self, '_m_mass', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"kg"
            return getattr(self, '_m_unit', None)


    class BthomeSensorWater(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u4le()

        @property
        def water(self):
            if hasattr(self, '_m_water'):
                return self._m_water

            self._m_water = (self.value * 0.001)
            return getattr(self, '_m_water', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"L"
            return getattr(self, '_m_unit', None)


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
                return self._m_speed

            self._m_speed = (self.value * 0.01)
            return getattr(self, '_m_speed', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m/s"
            return getattr(self, '_m_unit', None)


    class BthomeSensorRaw(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_value = self._io.read_u1()
            self.value = self._io.read_bytes(self.len_value)


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
                return self._m_dew_point

            self._m_dew_point = (self.value * 0.01)
            return getattr(self, '_m_dew_point', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"\260C"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryOccupancy(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.occupancy = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorCount(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.count = self._io.read_u1()


    class BthomeMeasurement(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.object_id = KaitaiStream.resolve_enum(BthomeServiceData.BthomeObjectId, self._io.read_u1())
            _on = self.object_id
            if _on == BthomeServiceData.BthomeObjectId.sensor_mass_lb_0_01:
                self.data = BthomeServiceData.BthomeSensorMassLb001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_moving:
                self.data = BthomeServiceData.BthomeBinaryMoving(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_moisture:
                self.data = BthomeServiceData.BthomeBinaryMoisture(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_humidity_0_01:
                self.data = BthomeServiceData.BthomeSensorHumidity001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_distance_mm:
                self.data = BthomeServiceData.BthomeSensorDistanceMm(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_uv_index_0_1:
                self.data = BthomeServiceData.BthomeSensorUvIndex01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_moisture_0_01:
                self.data = BthomeServiceData.BthomeSensorMoisture001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_gas:
                self.data = BthomeServiceData.BthomeSensorGas(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_motion:
                self.data = BthomeServiceData.BthomeBinaryMotion(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_energy_0_001:
                self.data = BthomeServiceData.BthomeSensorEnergy0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_temperature_0_01:
                self.data = BthomeServiceData.BthomeSensorTemperature001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_opening:
                self.data = BthomeServiceData.BthomeBinaryOpening(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_dewpoint_0_01:
                self.data = BthomeServiceData.BthomeSensorDewpoint001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_smoke:
                self.data = BthomeServiceData.BthomeBinarySmoke(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_co2:
                self.data = BthomeServiceData.BthomeSensorCo2(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_sound:
                self.data = BthomeServiceData.BthomeBinarySound(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.misc_packet_id:
                self.data = BthomeServiceData.BthomeMiscPacketId(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_volume_flow_rate_0_001:
                self.data = BthomeServiceData.BthomeSensorVolumeFlowRate0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_volume_0_001:
                self.data = BthomeServiceData.BthomeSensorVolume0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_occupancy:
                self.data = BthomeServiceData.BthomeBinaryOccupancy(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_door:
                self.data = BthomeServiceData.BthomeBinaryDoor(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_volume:
                self.data = BthomeServiceData.BthomeSensorVolume(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_generic_boolean:
                self.data = BthomeServiceData.BthomeBinaryGenericBoolean(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_power_0_01:
                self.data = BthomeServiceData.BthomeSensorPower001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_light:
                self.data = BthomeServiceData.BthomeBinaryLight(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_window:
                self.data = BthomeServiceData.BthomeBinaryWindow(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_count_uint32:
                self.data = BthomeServiceData.BthomeSensorCountUint32(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_current_0_001:
                self.data = BthomeServiceData.BthomeSensorCurrent0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_mass_kg_0_01:
                self.data = BthomeServiceData.BthomeSensorMassKg001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_presence:
                self.data = BthomeServiceData.BthomeBinaryPresence(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_gas:
                self.data = BthomeServiceData.BthomeBinaryGas(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_garage_door:
                self.data = BthomeServiceData.BthomeBinaryGarageDoor(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_connectivity:
                self.data = BthomeServiceData.BthomeBinaryConnectivity(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_problem:
                self.data = BthomeServiceData.BthomeBinaryProblem(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_raw:
                self.data = BthomeServiceData.BthomeSensorRaw(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_distance_m_0_1:
                self.data = BthomeServiceData.BthomeSensorDistanceM01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_running:
                self.data = BthomeServiceData.BthomeBinaryRunning(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.event_button:
                self.data = BthomeServiceData.BthomeEventButton(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_tamper:
                self.data = BthomeServiceData.BthomeBinaryTamper(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_voltage_0_001:
                self.data = BthomeServiceData.BthomeSensorVoltage0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_timestamp:
                self.data = BthomeServiceData.BthomeSensorTimestamp(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_plug:
                self.data = BthomeServiceData.BthomeBinaryPlug(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_battery_charging:
                self.data = BthomeServiceData.BthomeBinaryBatteryCharging(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_tvoc:
                self.data = BthomeServiceData.BthomeSensorTvoc(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_duration_0_001:
                self.data = BthomeServiceData.BthomeSensorDuration0001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_lock:
                self.data = BthomeServiceData.BthomeBinaryLock(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_battery:
                self.data = BthomeServiceData.BthomeSensorBattery(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_cold:
                self.data = BthomeServiceData.BthomeBinaryCold(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_pressure_0_01:
                self.data = BthomeServiceData.BthomeSensorPressure001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_volume_0_1:
                self.data = BthomeServiceData.BthomeSensorVolume01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_voltage_0_1:
                self.data = BthomeServiceData.BthomeSensorVoltage01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_illuminance_0_01:
                self.data = BthomeServiceData.BthomeSensorIlluminance001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_acceleration:
                self.data = BthomeServiceData.BthomeSensorAcceleration(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_temperature_0_1:
                self.data = BthomeServiceData.BthomeSensorTemperature01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_battery:
                self.data = BthomeServiceData.BthomeBinaryBattery(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_count_uint16:
                self.data = BthomeServiceData.BthomeSensorCountUint16(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_gas_uint32:
                self.data = BthomeServiceData.BthomeSensorGasUint32(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_power:
                self.data = BthomeServiceData.BthomeBinaryPower(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_count:
                self.data = BthomeServiceData.BthomeSensorCount(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_water:
                self.data = BthomeServiceData.BthomeSensorWater(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_humidity:
                self.data = BthomeServiceData.BthomeSensorHumidity(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_carbon_monoxide:
                self.data = BthomeServiceData.BthomeBinaryCarbonMonoxide(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_heat:
                self.data = BthomeServiceData.BthomeBinaryHeat(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_pm10:
                self.data = BthomeServiceData.BthomeSensorPm10(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_rotation_0_1:
                self.data = BthomeServiceData.BthomeSensorRotation01(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_speed_0_01:
                self.data = BthomeServiceData.BthomeSensorSpeed001(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_text:
                self.data = BthomeServiceData.BthomeSensorText(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.event_dimmer:
                self.data = BthomeServiceData.BthomeEventDimmer(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_gyroscope:
                self.data = BthomeServiceData.BthomeSensorGyroscope(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_energy_0_001_uint32:
                self.data = BthomeServiceData.BthomeSensorEnergy0001Uint32(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_safety:
                self.data = BthomeServiceData.BthomeBinarySafety(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.binary_vibration:
                self.data = BthomeServiceData.BthomeBinaryVibration(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_pm2_5:
                self.data = BthomeServiceData.BthomeSensorPm25(self._io, self, self._root)
            elif _on == BthomeServiceData.BthomeObjectId.sensor_moisture:
                self.data = BthomeServiceData.BthomeSensorMoisture(self._io, self, self._root)
            else:
                self.data = BthomeServiceData.BthomeUnknown(self._io, self, self._root)


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
                return self._m_unit

            self._m_unit = u"%"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryRunning(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.running = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryPlug(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.plug = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorPower001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def power(self):
            if hasattr(self, '_m_power'):
                return self._m_power

            self._m_power = (self.value.value * 0.01)
            return getattr(self, '_m_power', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"W"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryMotion(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.motion = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryTamper(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.tamper = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinaryBatteryCharging(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.battery_charging = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_volume

            self._m_volume = (self.value * 0.001)
            return getattr(self, '_m_volume', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"L"
            return getattr(self, '_m_unit', None)


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
                return self._m_distance

            self._m_distance = (self.value * 0.1)
            return getattr(self, '_m_distance', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m"
            return getattr(self, '_m_unit', None)


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
                return self._m_unit

            self._m_unit = u"%"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryCarbonMonoxide(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.carbon_monoxide = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorText(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len_value = self._io.read_u1()
            self.value = (self._io.read_bytes(self.len_value)).decode(u"UTF-8")


    class BthomeBinaryLight(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.light = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeBinarySafety(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.safety = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_humidity

            self._m_humidity = (self.value * 0.01)
            return getattr(self, '_m_humidity', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"%"
            return getattr(self, '_m_unit', None)


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
                return self._m_moisture

            self._m_moisture = (self.value * 0.01)
            return getattr(self, '_m_moisture', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"%"
            return getattr(self, '_m_unit', None)


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
                return self._m_volume_flow_rate

            self._m_volume_flow_rate = (self.value * 0.001)
            return getattr(self, '_m_volume_flow_rate', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"m\263/hr"
            return getattr(self, '_m_unit', None)


    class BthomeBinarySmoke(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.smoke = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_uv_index

            self._m_uv_index = (self.value * 0.1)
            return getattr(self, '_m_uv_index', None)


    class BthomeBinaryProblem(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.problem = BthomeServiceData.Bool8(self._io, self, self._root)


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
                return self._m_voltage

            self._m_voltage = (self.value * 0.1)
            return getattr(self, '_m_voltage', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"V"
            return getattr(self, '_m_unit', None)


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
                return self._m_rotation

            self._m_rotation = (self.value * 0.1)
            return getattr(self, '_m_rotation', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"\260"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryGas(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.gas = BthomeServiceData.Bool8(self._io, self, self._root)


    class BthomeSensorGyroscope(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2le()

        @property
        def gyroscope(self):
            if hasattr(self, '_m_gyroscope'):
                return self._m_gyroscope

            self._m_gyroscope = (self.value * 0.001)
            return getattr(self, '_m_gyroscope', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"\260/s"
            return getattr(self, '_m_unit', None)


    class BthomeSensorDuration0001(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = BthomeServiceData.U3(self._io, self, self._root)

        @property
        def duration(self):
            if hasattr(self, '_m_duration'):
                return self._m_duration

            self._m_duration = (self.value.value * 0.001)
            return getattr(self, '_m_duration', None)

        @property
        def unit(self):
            if hasattr(self, '_m_unit'):
                return self._m_unit

            self._m_unit = u"s"
            return getattr(self, '_m_unit', None)


    class BthomeBinaryGenericBoolean(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.generic_boolean = BthomeServiceData.Bool8(self._io, self, self._root)



