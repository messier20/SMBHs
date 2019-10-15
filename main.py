from input_parameters.arrays import *
from input_parameters.galaxy_parameters import *
from input_parameters.initial_values import *
from input_parameters.program_constants import *
from input_parameters.switches import *
from abstractions.DrivingForceIntegrator import DrivingForceIntegrator
from models.mas_calc import mass_calculation
from abstractions.FadeTypeSwitcher import FadeTypeSwitcher


def ending(is_main_loop):
    is_main_loop = False
    print('Iteration number ', k, ' finished')
    return is_main_loop

if __name__ == '__main__':
    # start of main loop
    # for k = 0, niter-1 do begin;n_elements(params[*, 0])-1 do begin

    FadeTypeSwitcher = FadeTypeSwitcher()
    Integrator = DrivingForceIntegrator()

    is_main_loop = True
    for k in range(ITERATIONS_NUM):
        #     # maybe niter-1?
        index = 0

        radius_arr[k, 0] = radius
        dot_radius_arr[k, 0] = dot_radius
        dotdot_radius_arr[k, 0] = dotdot_radius

        disc_mass = total_masses[k] * bulge_disc_totalmass_fractions[k] * (
                1 - bulge_totalmasses[k]) * disc_gas_fractions[k]
        # mdisc = mtot * fbt * (1 - bt) * fdg

        cooling_radius = 0.52 * math.sqrt(
            (bulge_disc_gas_fractions[k] / 0.16)) * 1.e-5 / unit_kpc  # cooling radius in kpc

        while is_main_loop:  # main loop, ends when one of the ending conditions is reached -
            # either number of timesteps, time or outflow radius pass a threshold

            (mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2) = \
                mass_calculation(radius, dot_radius, dotdot_radius, delta_radius, halo_profile, bulge_profile,
                                 disc_profile, total_masses[k], virial_radiuses[k], halo_concentration_parameters[k],
                                 bulge_scale, disc_scale, bulge_disc_totalmass_fractions[k],
                                 halo_gas_fraction, bulge_disc_gas_fractions[k], bulge_totalmasses[k])

            mass_out_arr[k, index] = mg
            total_mass_arr[k, index] = mg + mp
            dot_mass_arr[k, index] = mdg

            print(mp, 'mp')
            print(mdp)
            print(mg, ' mg')
            print(mass_out_arr, ' mass out')
            print(total_mass_arr, ' totalmass')
            print(mdg)
            print(dot_mass_arr, 'dotmass')
            print(mddg)
            print(rhogas)
            print(sigma)
            print(phi)
            print(phigrad)
            print(rhogas2, 'rhogas2')

            # ;this sets the timestep with 'Courant' criterion 0.1. In fact, this is
            # ;a little sloppy, since we should set the timestep after calculating
            # ;the expected acceleration, but since r, rdot, rddot, rtdot do not
            # ;change very significantly between timesteps, this is fine

            dot_t1 = (radius + 1.e-8) / (radius + 1.e-8)
            dot_t2 = (dot_radius + 1.e-8) / (dotdot_radius + 1.e-8)
            dot_t3 = (dotdot_radius + 1.e-8) / (dot_rt_arr[k, index] + 1.e-8)

            dt = 0.1 * min(abs(dot_t1), abs(dot_t2), abs(dot_t3))
            if dt > DT_MAX / 100. * (10. * time_arr[k, index] + 1.):
                dt = DT_MAX / 100. * (10. * time_arr[k, index] + 1.)
            if dt < DT_MIN:
                dt = DT_MIN
            dot_time_arr[k, index + 1] = dt
            time_arr[k, index + 1] = time_arr[k, index] + dt

            print(dt)
            print(dot_time_arr, ' dot time arr')
            print(time_arr, ' time arr')

            # ;AGN luminosity, first in terms of Eddington factor
            if repeating_equation:
                time_eff = time_arr[k, index] % quasar_dts[k]
            else:
                time_eff = time_arr[k, index]

            luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(fade, time_eff, quasar_duration)
            print(luminosity_coef)
            luminosity_edd = 1.3e38 * (smbh_masses[
                                           k] * unit_mass / 1.989e33) * unit_time / unit_energy  # ;eddington luminosity for the current SMBH mass
            luminosity = luminosity_coef * luminosity_edd
            luminosity_arr[k, index + 1] = luminosity  # ;actual luminosity

            # ;grow the SMBH
            if smbh_grows:
                smbh_mass = smbh_masses[k] * math.exp(luminosity_coef * dt / salpeter_timescale)  # ;new BH mass

            # ;SMBH growth and luminosity calculation ends

            (dot_radius_arr, dot_radius, dotdot_radius) = \
                Integrator.driving_force_calc(driving_force, mg, radius, eta_drive, integration_method, luminosity, mdg,
                                              dot_radius, dotdot_radius, mp, mdp, mddg, dot_rt_arr, radius_arr,
                                              dot_radius_arr, dotdot_radius_arr, k, index, dt)
            print(dot_radius_arr, ' dot_radius_arr')
            print(dot_radius, ' dot_radius')
            print(dotdot_radius, ' dotdot_radius')

            # TODO implement clearing oscillations
            # if clear_oscillations:

            pressure_contact_arr[k, index] = 4. / 3. * (dot_radius ** 2) * rhogas2 * (
                    1. - 1. / (5. * dot_radius / sigma) ** 2)
            pressure_outer_arr[k, index] = (mg * dotdot_radius + mdg * dot_radius + mg * (mp + mg / 2.) / (
                    radius ** 2)) / (4 * math.pi * (radius ** 2))
            # pres[k, i] = 4. / 3. * rd ^ 2. * rhogas2 * (1. - 1. / (5. * (rd / sigma) ^ 2.))  # ;pressure at the outer shock
            # p2 = (mg * rdd + mdg * rd + mg * (mp + mg / 2.) / r ^ 2.) / (4 *!pi * r ^ 2.)  # ;pressure at the contact discontinuity
            # pres2[k, i] = p2

            print(pressure_contact_arr)
            print(pressure_outer_arr)

            index += 1
            # can i write index >= TIMESTEPS
            if index >= len(radius_arr[:, 0]) - 1:
                is_main_loop = ending(is_main_loop)

            if time_arr[k, index] >= TIME_MAX:
                is_main_loop = ending(is_main_loop)

            if radius_arr[k, index] >= RADIUS_MAX:
                is_main_loop = ending(is_main_loop)


        radius_arr = radius_arr * unit_kpc
        dot_radius = dot_radius * unit_velocity/1.e5
        time_arr = time_arr * unit_year
        pressure_contact_arr = pressure_contact_arr / unit_length / (unit_time ** 2)
        pressure_outer_arr = pressure_outer_arr / unit_length / (unit_time ** 2)
        dot_mass_arr = dot_mass_arr * unit_sunmass / unit_year
        mass_out_arr = mass_out_arr * unit_sunmass
        total_mass_arr = total_mass_arr * unit_sunmass


