from model_program.input_parameters.program_constants import *
# TODO for non arrays parameters add init prefix
from model_program.input_parameters.program_units import *

total_mass = 1.e13 / unit_sunmass
total_masses = [total_mass for i in range(0, ITERATIONS_NUM)]  # total virial mass of the galaxy
virial_radius_1 = 626 * (((total_mass/(10**13))*unit_sunmass)**(1/3)) # old values: 200 / unit_kpc; 138.10558496091766321489 / unit_kpc
virial_radius = virial_radius_1 / unit_kpc
virial_radiuses = [virial_radius for i in range(0, ITERATIONS_NUM)]  # ;virial radius in kpc
bulge_disc_totalmass_fractions = [0.002, 0.003, 0.004, 0.005, 0.006, 0.007, 0.008, 0.009, 0.01, 0.02, 0.03] # fraction of total mass in the bulge+disc system

halo_gas_fraction = 1.e-3  # gas fraction in the halo
bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]  # gas fraction in the bulge+disc

# TODO how to understand bulge-to-total mass
bulge_totalmasses = [1 for i in range(0, ITERATIONS_NUM)]  # bulge-to-total mass ratio

disc_gas_fractions = [0.8 for i in range(0, ITERATIONS_NUM)]  # gas fraction in the disc

halo_concentration_parameters = [10 for i in range(0, ITERATIONS_NUM)]  # concentration parameter, only necessary for NFW halos

# AGN parameters
quasar_dt = 1.e6 / unit_year #time between successive quasar phases
quasar_dts = [quasar_dt for i in range(0, ITERATIONS_NUM)]  # 1.d6/unityear time between successive quasar phases
quasar_duration = 5.e10 / unit_year
quasar_durations = [quasar_duration for i in range(0, ITERATIONS_NUM)]  # ;quasar duration

drop_timescale = 3.e5 / unit_year
alpha_drop = 0.5
eddingtion_ration = 1.  # ;(maximum) Eddington ratio
smbh_mass_init = 1.e8 / unit_sunmass  # ;SMBH mass in Solar masses
smbh_masses = [smbh_mass_init for i in range(0, ITERATIONS_NUM)]
salpeter_timescale = 4.5e8*RADIATIVE_EFFICIENCY_ETA/unit_year        #;SMBH growth timescale at Eddington rate - Salpeter timescale

bulge_masses = [2.e10, 3.e10, 4.e10, 5.e10, 6.e10, 7.e10, 8.e10, 9.e10,  1.e11, 2.e11, 3.e11]
bulge_scales = []
for bulge_mass in bulge_masses:
    # I'm using theoretical formula times 2
    bulge_scales.append((((bulge_mass/1.e11)**0.88)*2.4*2 / unit_kpc))

print(bulge_scales)

disc_scale = 3 / unit_kpc  # ;scale length of disc in kpc