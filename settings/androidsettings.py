from biicode.common.settings.smart_serial import smart_serialize, smart_deserialize
from biicode.common.exception import ConfigurationFileError
from biicode.common.settings.loader import yaml_dumps
import os


class AndroidSettings(object):
    """
        Attributes
        ----------
            abi: Android ABI
                EX: "armeabi-v7a" or "x86" for emulator.
            api_level: Android Native Api Level
                EX: 18
            sdk: SDK path
            ndk: NDK path
            ant: ANT tool execute ant

        ABI possible values
        -------------------

        "armeabi" - matches to the NDK ABI with the same name.
        "armeabi-v7a" - matches to the NDK ABI with the same name.
           See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
        "armeabi-v7a with NEON" - same as armeabi-v7a, but
            sets NEON as floating-point unit
        "armeabi-v7a with VFPV3" - same as armeabi-v7a, but
            sets VFPV3 as floating-point unit (has 32 registers instead of 16).
        "armeabi-v6 with VFP" - tuned for ARMv6 processors having VFP.
        "arm64-v8a" - matches to the NDK ABI with the same name.
           See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
        "x86" - matches to the NDK ABI with the same name.
            See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
        "x86_64" - matches to the NDK ABI with the same name.
            See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
        "mips" - matches to the NDK ABI with the same name.
            See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
        "mips64" - matches to the NDK ABI with the same name.
            See ${ANDROID_NDK}/docs/CPU-ARCH-ABIS.html for the documentation.
    """

    smart_serial = {'abi': ('abi', None, None),
                    'api_level': ('api_level', None, None),
                    'sdk': ('sdk', None, None),
                    'ndk': ('ndk', None, None),
                    'ant': ('ant', None, None)
                    }

    def __init__(self):
        self.abi = None
        self.api_level = None
        self.sdk = None
        self.ndk = None
        self.ant = None

    def __nonzero__(self):
        if self.abi or self.api_level or self.sdk or self.ndk or self.ant:
            return True
        return False

    def __eq__(self, other):
        return self.abi == other.abi and \
            self.api_level == other.api_level and self.sdk == other.sdk and \
            self.sdk == other.sdk and self.version == other.version and \
            self.ndk == other.ndk and \
            self.ant == other.ant

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return yaml_dumps(self)

    def serialize(self):
        serial = smart_serialize(self)
        return serial

    @classmethod
    def deserialize(cls, data):
        try:
            d = smart_deserialize(cls, data)
        except ValueError as error:
            raise ConfigurationFileError("Error parsing settings.bii %s %s" % (os.linesep, error))
        return d

    serialize_dict = serialize
    deserialize_dict = deserialize
