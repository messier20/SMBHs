from input_parameters.program_units import unit_kpc, unit_velocity
import input_parameters.parameters as params

radius = 0.001 / unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
dot_radius = 1.e5 / unit_velocity
dotdot_radius = 0
delta_radius = 0

halo_profile = params.PROFILE_TYPES.NFW.value
bulge_profile = params.PROFILE_TYPES.ISOTHERMAL.value
disc_profile = params.DISC_PROFILE.EXPONENTIAL.value
