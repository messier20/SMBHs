from input_parameters.program_units import *

total_mass = 1.e12 / unit_sunmass
total_masses = [total_mass for i in range(0, 5)]  # total virial mass of the galaxy
virial_radius = 200 / unit_kpc
virial_radiuses = [virial_radius for i in range(0, 5)]  # ;virial radius in kpc
bulge_disc_totalmass_fractions = [0.4 for i in range(0, 5)]  # fraction of total mass in the bulge+disc system

halo_gas_fraction = 1.e-3  # gas fraction in the halo
bulge_disc_gas_fractions = [0.05, 0.1, 0.25, 0.5, 1.]  # gas fraction in the bulge+disc

# TODO how to understand bulge-to-total mass
bulge_totalmasses = [0.1 for i in range(0, 5)]  # bulge-to-total mass ratio

disc_gas_fractions = [0.8 for i in range(0, 5)]  # gas fraction in the disc

halo_concentration_parameters = [10 for i in range(0, 5)]  # concentration parameter, only necessary for NFW halos
