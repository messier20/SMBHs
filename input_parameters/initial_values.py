from input_parameters.program_units import unit_kpc, unit_velocity
import input_parameters.parameters as params

version = 4.0
model_type = ['mb20', 'mb30', 'mb40', 'mb50', 'mb60', 'mb70', 'mb80', 'mb90', 'mb100','mb200', 'mb300']

# TODO maybe add prefix init_ for all values
dot_radius = 0
radius = 0.001 / unit_kpc  # arrr[k, 0] = 0.001 / C.unit_kpc
var = 100000.00000
dot_radius = var / unit_velocity
dotdot_radius = 0
delta_radius = 0

# TODO remove values here, use .value where the implementation is if needed
halo_profile = params.PROFILE_TYPES.NFW.value
bulge_profile = params.PROFILE_TYPES.ISOTHERMAL.value
disc_profile = params.DISC_PROFILE.EXPONENTIAL.value

fade = params.FADE.NONE.value
driving_force = params.DRIVING_FORCE.ENERGY_DRIVING
integration_method = params.INTEGRATION_METHOD.SIMPLE_INTEGRATION.value

eta_drive = 0.05                     #;coupling efficiency between luminosity or momentum and driving power/force
