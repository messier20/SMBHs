from input_parameters.arrays import *
from input_parameters.galaxy_parameters import *
from input_parameters.initial_values import *
from input_parameters.program_constants import *
from input_parameters.switches import *
from abstractions.DrivingForceIntegrator import DrivingForceIntegrator
from models.mass_calc import mass_calculation
from abstractions.FadeTypeSwitcher import FadeTypeSwitcher
from plots.plotting_LumAGN_relation import plotting_LumAGN_relation
from plots.plotting_R_relation import plotting_R_relation
import time

from plots.plotting_histogram import plotting_histogram


def ending(is_main_loop):
    start_time = time.time()
    is_main_loop = False
    print('Iteration number ', k, ' finished')
    return is_main_loop



if __name__ == '__main__':
    start_time = time.time()

    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()

    for k in range(ITERATIONS_NUM):
        is_main_loop = True
        index = 0

        smbh_mass = smbh_mass_init

        radius_arr[k, 0] = radius
        dot_radius_arr[k, 0] = dot_radius
        dotdot_radius_arr[k, 0] = dotdot_radius
        delta_radius_arr[k, 0] = delta_radius

        disc_mass = total_masses[k] * bulge_disc_totalmass_fractions[k] * (1 - bulge_totalmasses[k]) * disc_gas_fractions[k]

        cooling_radius = 0.52 * math.sqrt(
            (bulge_disc_gas_fractions[k] / 0.16)) * 1.e-5 / unit_kpc  # cooling radius in kpc

        while is_main_loop:  # main loop, ends when one of the ending conditions is reached -
            # either number of timesteps, time or outflow radius pass a threshold
            
            (mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2) = \
                mass_calculation(radius_arr[k, index], dot_radius_arr[k, index], dotdot_radius_arr[k, index],
                                 delta_radius_arr[k, index], halo_profile, bulge_profile,
                                 disc_profile, total_masses[k], virial_radiuses[k], halo_concentration_parameters[k],
                                 bulge_scale, disc_scale, bulge_disc_totalmass_fractions[k],
                                 halo_gas_fraction, bulge_disc_gas_fractions[k], bulge_totalmasses[k])

            mass_out_arr[k, index] = mg
            total_mass_arr[k, index] = mg + mp
            dot_mass_arr[k, index] = mdg

            # ;this sets the timestep with 'Courant' criterion 0.1. In fact, this is
            # ;a little sloppy, since we should set the timestep after calculating
            # ;the expected acceleration, but since r, rdot, rddot, rtdot do not
            # ;change very significantly between timesteps, this is fine

            dot_t1 = (radius_arr[k, index] + 1.e-8) / (radius_arr[k, index] + 1.e-8)
            dot_t2 = (dot_radius_arr[k, index] + 1.e-8) / (dotdot_radius_arr[k, index] + 1.e-8)
            dot_t3 = (dotdot_radius_arr[k, index] + 1.e-8) / (dot_rt_arr[k, index] + 1.e-8)

            dt = 0.1 * min(abs(dot_t1), abs(dot_t2), abs(dot_t3))
            if dt > DT_MAX / 100. * (10. * time_arr[k, index] + 1.):
                dt = DT_MAX / 100. * (10. * time_arr[k, index] + 1.)
            if dt < DT_MIN:
                dt = DT_MIN
            dot_time_arr[k, index + 1] = dt
            time_arr[k, index + 1] = time_arr[k, index] + dt

            # ;AGN luminosity, first in terms of Eddington factor
            if repeating_equation:
                time_eff = time_arr[k, index] % quasar_dts[k]
            else:
                time_eff = time_arr[k, index]

            luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(fade, time_eff, quasar_duration)
            luminosity_edd = 1.3e38 * (smbh_mass * unit_mass / 1.989e33) * unit_time / unit_energy  # ;eddington luminosity for the current SMBH mass
            luminosity = luminosity_coef * luminosity_edd
            luminosity_AGN_arr[k, index + 1] = luminosity  # ;actual luminosity

            # ;grow the SMBH
            if smbh_grows:
                smbh_mass = smbh_mass * math.exp(luminosity_coef * dt / salpeter_timescale)  # ;new BH mass


            # ;SMBH growth and luminosity calculation ends

            (radius_arr, dot_radius_arr, dotdot_radius) = \
                Integrator.driving_force_calc(driving_force, mg, radius_arr[k, index], eta_drive, integration_method, luminosity, mdg,
                                              dot_radius_arr[k, index], dotdot_radius_arr[k, index], mp, mdp, mddg, dot_rt_arr, radius_arr,
                                              dot_radius_arr, dotdot_radius_arr, k, index, dt)

            # TODO do I need to implement clearing oscillations
            # if clear_oscillations:

            # TODO implement this correctly
            # pressure_contact_arr[k, index] = 4. / 3. * (dot_radius ** 2) * rhogas2 * (
            #         1. - 1. / (5. * ((dot_radius / sigma) ** 2)))
            # pressure_outer_arr[k, index] = (mg * dotdot_radius + mdg * dot_radius + mg * (mp + mg / 2.) / (
            #         radius ** 2)) / (4 * math.pi * (radius ** 2))
            # print(dot_radius, ' maybe wrong dot radius')

            # pres[k, i] = 4. / 3. * rd ^ 2. * rhogas2 * (1. - 1. / (5. * (rd / sigma) ^ 2.))  # ;pressure at the outer shock
            # p2 = (mg * rdd + mdg * rd + mg * (mp + mg / 2.) / r ^ 2.) / (4 *!pi * r ^ 2.)  # ;pressure at the contact discontinuity
            # pres2[k, i] = p2

            index += 1
            if index >= len(radius_arr[0,]) - 1:
                print(' timesteps')
                is_main_loop = ending(is_main_loop)

            if time_arr[k, index] >= TIME_MAX:
                print('time')
                is_main_loop = ending(is_main_loop)

            if radius_arr[k, index] >= RADIUS_MAX:
                print('radiusmax')
                is_main_loop = ending(is_main_loop)

    radius_arr = radius_arr * unit_kpc
    dot_radius_arr = dot_radius_arr * unit_velocity/1.e5
    time_arr = time_arr * unit_year
    # pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
    # pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
    dot_mass_arr = dot_mass_arr * unit_sunmass / unit_year
    mass_out_arr = mass_out_arr * unit_sunmass
    total_mass_arr = total_mass_arr * unit_sunmass


    exec_time = time.time()
    print("exec time --- %s seconds ---" % (time.time() - start_time))
    # print(np.where(dot_radius_arr > 1000))

    # plotting_R_relation(time_arr, radius_arr, mass_out_arr, dot_mass_arr)
    # plotting_LumAGN_relation(luminosity_AGN_arr, dot_radius_arr, dot_mass_arr)
    plotting_histogram(dot_radius_arr, dot_mass_arr, time_arr)

    print("plot time --- %s seconds ---" % (time.time() - exec_time))


