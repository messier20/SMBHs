import math

from input_parameters import program_constants, galaxy_parameters as galaxy, initial_values as init_val, program_units
from input_parameters import switches
from models.mas_calc import mass_calculation

if __name__ == '__main__':
    print(galaxy.total_masses)
    # KODEL kode visi parametrai ideti i masyvus, bet naudojamas tik vienas variantas.
    # O po to kainaudojamas, kodel priskiriama kintamajam o ne kreipiamasi i tam tikra masyvo elementa pagal loopa

    # start of main loop
    # for k = 0, niter-1 do begin;n_elements(params[*, 0])-1 do begin
    is_main_loop = True
    for k in range(program_constants.ITERATIONS_NUMBER):
        #     # maybe niter-1?
        # total_mass = C.total_mass_x[k] if len(C.total_mass_x[k]) > 1 else C.total_mass_x[0]
        # total_mass = C.total_mass[k]
        # print(total_mass, 'total mass mtot_x')

        disc_mass = galaxy.total_masses[k] * galaxy.bulge_disc_totalmass_fractions[k] * (
                1 - galaxy.bulge_totalmasses[k]) * galaxy.disc_gas_fractions[k]
        # mdisc = mtot * fbt * (1 - bt) * fdg

        cooling_radius = 0.52 * math.sqrt(
            (galaxy.bulge_disc_gas_fractions[k] / 0.16)) * 1.e-5 / galaxy.unit_kpc  # cooling radius in kpc

        while is_main_loop:  # main loop, ends when one of the ending conditions is reached -
            # either number of timesteps, time or outflow radius pass a threshold

            profile = mass_calculation(init_val.radius, init_val.dot_radius, init_val.dotdot_radius,
                                       init_val.delta_radius, init_val.halo_profile, init_val.bulge_profile,
                                       init_val.disc_profile, galaxy.total_masses[k], galaxy.virial_radiuses[k],
                                       galaxy.halo_concentration_parameters[k], program_units.bulge_scale,
                                       program_units.disc_scale, galaxy.bulge_disc_totalmass_fractions[k],
                                       galaxy.halo_gas_fraction, galaxy.bulge_disc_gas_fractions[k],
                                       galaxy.bulge_totalmasses[k])
            print(profile)

            is_main_loop = False
