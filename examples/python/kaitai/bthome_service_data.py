# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO


if parse_version(kaitaistruct.__version__) < parse_version('0.9'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__))

from . import bthome_measurement
class BthomeServiceData(KaitaiStruct):
    """BLE advertising in the BTHome v2 format
    
    .. seealso::
       Source - https://bthome.io/format/
    """
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.device_information = BthomeServiceData.BthomeDeviceInformation(self._io, self, self._root)
        if self.device_information.mac_included:
            self.mac_reversed = self._io.read_bytes(6)

        if self.device_information.bthome_version == 2:
            self.measurements = []
            i = 0
            while not self._io.is_eof():
                _on = self.device_information.encryption
                if _on == False:
                    self.measurements.append(bthome_measurement.BthomeMeasurement(self._io))
                i += 1



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



