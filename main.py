from input_parameters.arrays import *
from input_parameters.galaxy_parameters import *
from input_parameters.initial_values import *
from input_parameters.program_constants import *
from input_parameters.switches import *
from abstractions.DrivingForceIntegrator import DrivingForceIntegrator
from models.mass_calc import mass_calculation
from abstractions.FadeTypeSwitcher import FadeTypeSwitcher
from plots.plotting_LumAGN_relation import plotting_LumAGN_relation
from plots.plotting_r_relation import plotting_r_relation
from plots.plotting_time_relation import plotting_time_relation
import time
import pandas as pd
import os

from plots.plotting_histogram import plotting_histogram


def ending(is_main_loop):
    is_main_loop = False
    print('Iteration number ', k, ' finished')
    return is_main_loop


if __name__ == '__main__':
    np.seterr(divide='ignore', invalid='ignore')
    start_time = time.time()

    params_path = 'C:/Users/Monika/PycharmProjects/SMBHs/results/output_values/'
    values_version_folder = 'v' + str(version) + '/'
    try:
        os.mkdir(params_path + values_version_folder)
    except:
        pass

    params_output_name = values_version_folder +'fbt_v2'

    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()

    for out_index in range(len(bulge_disc_totalmass_fractions)):
        loop_time = time.time()

        (radius_arr, dot_radius_arr, dotdot_radius_arr, delta_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, \
        dot_rt_arr, time_arr, dot_time_arr, luminosity_AGN_arr, pressure_contact_arr, pressure_outer_arr, bulge_mass_arr) =init_zero_arrays()

        bulge_disc_totalmass_fraction = bulge_disc_totalmass_fractions[out_index]
        bulge_scale = bulge_scales[out_index]
        for k in range(ITERATIONS_NUM):
            is_main_loop = True
            index = 0

            smbh_mass = smbh_mass_init

            radius_arr[k, 0] = radius
            dot_radius_arr[k, 0] = dot_radius
            dotdot_radius_arr[k, 0] = dotdot_radius
            delta_radius_arr[k, 0] = delta_radius

            #mhalo = mtot*(1-fbt)
            # mbulge = mtot * fbt * bt
            mass_halo = total_masses[k] * (1 - bulge_disc_totalmass_fraction)
            mass_bulge = total_masses[k] * bulge_disc_totalmass_fraction * bulge_totalmasses[k]
            disc_mass = total_masses[k] * bulge_disc_totalmass_fraction * (1 - bulge_totalmasses[k]) * \
                        disc_gas_fractions[k]

            cooling_radius = 0.52 * math.sqrt(
                (bulge_disc_gas_fractions[k] / 0.16)) * 1.e-5 / unit_kpc  # cooling radius in kpc

            while is_main_loop:  # main loop, ends when one of the ending conditions is reached -
                # either number of timesteps, time or outflow radius pass a threshold

                (mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2, mb) = \
                    mass_calculation(radius_arr[k, index], dot_radius_arr[k, index], dotdot_radius_arr[k, index],
                                     delta_radius_arr[k, index], halo_profile, bulge_profile,
                                     disc_profile, total_masses[k], virial_radiuses[k],
                                     halo_concentration_parameters[k],
                                     bulge_scale, disc_scale, bulge_disc_totalmass_fraction,
                                     halo_gas_fraction, bulge_disc_gas_fractions[k], bulge_totalmasses[k])

                mass_out_arr[k, index] = mg
                total_mass_arr[k, index] = mg + mp
                dot_mass_arr[k, index] = mdg
                bulge_mass_arr[k, index] = mb

                # ;this sets the timestep with 'Courant' criterion 0.1. In fact, this is
                # ;a little sloppy, since we should set the timestep after calculating
                # ;the expected acceleration, but since r, rdot, rddot, rtdot do not
                # ;change very significantly between timesteps, this is fine

                dot_t1 = (radius_arr[k, index] + 1.e-8) / (dot_radius_arr[k, index] + 1.e-8)
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
                luminosity_edd = 1.3e38 * (
                            smbh_mass * unit_mass / 1.989e33) * unit_time / unit_energy  # ;eddington luminosity for the current SMBH mass
                luminosity = luminosity_coef * luminosity_edd
                luminosity_AGN_arr[k, index + 1] = luminosity  # ;actual luminosity

                # ;grow the SMBH
                if smbh_grows:
                    smbh_mass = smbh_mass * math.exp(luminosity_coef * dt / salpeter_timescale)  # ;new BH mass

                # ;SMBH growth and luminosity calculation ends

                (radius_arr, dot_radius_arr, dotdot_radius, dot_rt_arr) = \
                    Integrator.driving_force_calc(driving_force, mg, radius_arr[k, index], eta_drive,
                                                  integration_method, luminosity, mdg,
                                                  dot_radius_arr[k, index], dotdot_radius_arr[k, index], mp, mdp, mddg,
                                                  dot_rt_arr, radius_arr,
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

        observed_time_arr = (radius_arr / dot_radius_arr) * unit_year
        radius_arr = radius_arr * unit_kpc
        dot_radius_arr = dot_radius_arr * unit_velocity/1.e5
        time_arr = time_arr * unit_year
        # pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
        # pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
        dot_mass_arr = dot_mass_arr * unit_sunmass / unit_year
        mass_out_arr = mass_out_arr * unit_sunmass
        total_mass_arr = total_mass_arr * unit_sunmass

        # mine
        bulge_mass_arr = bulge_mass_arr * unit_sunmass
        # observed_time_arr = radius_arr / (dot_radius_arr * 1.02269032 * (10**(-9)))

        radius_more_than_20_arr = np.where(radius_arr > 0.02, radius_arr, np.nan)
        dot_radius_reduced_arr = np.where(radius_arr > 0.02, dot_radius_arr, np.nan)
        # dot_radius_reduced_arr.shape = dot_radius_arr.shape
        time_reduced_arr = np.where(radius_arr > 0.02, time_arr, np.nan)
        dot_mass_reduced_arr = np.where(radius_arr > 0.02, dot_mass_arr, np.nan)
        mass_out_reduced_arr = np.where(radius_arr > 0.02, mass_out_arr, np.nan)
        total_mass_reduced_arr = np.where(radius_arr > 0.02, total_mass_arr, np.nan)
        luminosity_AGN_reduced_arr = np.where(radius_arr > 0.02, luminosity_AGN_arr, np.nan)
        observed_time_reduced_arr = np.where(radius_arr > 0.02, observed_time_arr, np.nan)



        # TODO maybe switch order
        # df = pd.DataFrame(np.array(radius_arr).transpose())
        radius_df = pd.DataFrame(np.array(radius_arr).transpose())
        radius_df.to_csv(str(params_path) + params_output_name + 'radius' + model_type[out_index] + '.csv')

        dot_radius_df = pd.DataFrame(np.array(dot_radius_arr).transpose())
        dot_radius_df.to_csv(str(params_path) + params_output_name + 'dot_Radius' + model_type[out_index] + '.csv')

        time_df = pd.DataFrame(np.array(time_arr).transpose())
        time_df.to_csv(str(params_path) + params_output_name + 'time' + model_type[out_index] + '.csv')

        dot_mass_df = pd.DataFrame(np.array(dot_mass_arr).transpose())
        dot_mass_df.to_csv(str(params_path) + params_output_name + 'dot_mass' + model_type[out_index] + '.csv')

        tot_mass_df = pd.DataFrame(np.array(total_mass_arr).transpose())
        tot_mass_df.to_csv(str(params_path) + params_output_name + 'tot_mass' + model_type[out_index] + '.csv')

        out_mass_df = pd.DataFrame(np.array(mass_out_arr).transpose())
        out_mass_df.to_csv(str(params_path) + params_output_name + 'out_mass' + model_type[out_index] + '.csv')


        exec_time = time.time()
        print("exec time --- %s seconds ---" % (time.time() - loop_time))
        # print(np.where(dot_radius_arr > 1000))

        # plotting_time_relation(time_arr, radius_arr, mass_out_arr, dot_mass_arr, observed_time_arr, model_type[out_index], ' _nongrow_')
        # # plotting_LumAGN_relation(luminosity_AGN_arr, dot_radius_arr, dot_mass_arr, model_type[out_index], ' _nongrow_')
        # plotting_r_relation(radius_arr, dot_radius_arr, mass_out_arr, dot_mass_arr, model_type[out_index], ' _nongrow_')
        # plotting_histogram(dot_radius_arr, dot_mass_arr, time_arr, model_type[out_index], ' _nongrow_')

        # plotting_time_relation(time_reduced_arr, radius_more_than_20_arr, mass_out_reduced_arr, dot_mass_reduced_arr, observed_time_reduced_arr,model_type[out_index], ' _nongrow_more_than20pc_')
        # plotting_LumAGN_relation(luminosity_AGN_reduced_arr, dot_radius_reduced_arr, dot_mass_reduced_arr,model_type[out_index], ' _nongrow_more_than20pc_')
        plotting_r_relation(radius_more_than_20_arr,dot_radius_reduced_arr, mass_out_reduced_arr, dot_mass_reduced_arr,model_type[out_index], ' _nongrow_more_than20pc_')
        # plotting_histogram(dot_radius_reduced_arr, dot_mass_reduced_arr, time_reduced_arr, model_type[out_index], ' _nongrow_more_than20pc_')

        print("plot time --- %s seconds ---" % (time.time() - exec_time))

    print("program time --- %s seconds ---" % (time.time() - start_time))


