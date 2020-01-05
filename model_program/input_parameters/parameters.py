from enum import Enum


class PROFILE_TYPES(Enum):
    ISOTHERMAL = 'Isothermal'
    HERNQUIST = 'Hernquist'
    JAFFE = 'Jaffe'
    NFW = 'NFW'


class DISC_PROFILE(Enum):
    EXPONENTIAL = 'Exponential'


class FADE(Enum):
    NONE = 'none'
    EXPONENTIAL = 'exponential'
    POWER_LAW = 'power_law'
    KING = 'king'


class DRIVING_FORCE(Enum):
    ENERGY_DRIVING = 'energy_driving'
    MOMENTUM_DRIVING = 'momentum_driving'


class INTEGRATION_METHOD(Enum):
    SIMPLE_INTEGRATION = 'simple_integration'
    LEAP_FROG_DKD = 'leap_frog_dkd'
    LEAP_FROG_KDK = 'leap_frog_dkd'
