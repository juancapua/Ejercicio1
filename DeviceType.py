from enum import Enum

class DeviceType(str, Enum):
    ANDROID = 1
    IOS = 2
    TV = 3
    DESKTOP = 4
    