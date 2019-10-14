from input_parameters.parameters import DRIVING_FORCE
from input_parameters.program_units import *


class DrivingForceIntegrator:
    def __init__(self):
        pass

    def driving_force_calc(self, driving_force, mg, radius, eta_drive, integration_method):
        if driving_force == DRIVING_FORCE.ENERGY_DRIVING:
            optical_depth = 0.348 / (unit_length ** 2) * unit_mass * mg / (4 * math.pi * (radius ** 2))
            if optical_depth < 1:
                eta_drive = eta_drive * optical_depth
            if eta_drive < 0.05:
                eta_drive = 0.05  # transition to energy-driven wind
            method_name = str(integration_method)
            method = getattr(self, method_name, lambda: 'Invalid')
            return method()
        elif driving_force == DRIVING_FORCE.MOMENTUM_DRIVING:
            print(driving_force)

    def simple_integration(self):
        # rtdot, dotdot_radius, dt, eta_drive, cc, radius
        print('simple')

    def leap_frog_dkd(self):
        pass

    def leap_frog_kdk(self):
        pass
