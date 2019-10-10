from enum import Enum


class PROFILE_TYPES(Enum):
    ISOTHERMAL = 'Isothermal'
    HERNQUIST = 'Hernquist'
    JAFFE = 'Jaffe'
    NFW = 'NFW'


class DISC_PROFILE(Enum):
    EXPONENTIAL = 'Exponential'
