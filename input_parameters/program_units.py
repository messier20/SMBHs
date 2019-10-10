import math

import input_parameters.physics_constants as C

unit_length = 3.086e21
unit_mass = 5e9 * 1.989e33
#
unit_velocity = math.sqrt(C.GRAVITATIONAL * unit_mass / unit_length)  # unitvel = sqrt(gg*unitmass/unitlength)

# unittime = unitlength/unitvel
# unitsurfden = unitmass/unitlength^2.
# unitenergy = unitmass*unitvel^2
# unitdensity = unitmass/unitlength^3.
#
unit_kpc = unit_length / 3.086e21
# unityear = unittime/3.15d7
unit_sunmass = unit_mass / 1.989e33

bulge_scale = 1 / unit_kpc  # ;scale radius of bulge in kpc
disc_scale = 3 / unit_kpc  # ;scale length of disc in kpc
