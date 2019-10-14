from input_parameters.arrays import *
from input_parameters.galaxy_parameters import *
from input_parameters.initial_values import *
from input_parameters.program_constants import *
from input_parameters.switches import *
from models.driving_force_calc import DrivingForceIntegrator
from models.mas_calc import mass_calculation
from abstractions.FadeTypeSwitcher import FadeTypeSwitcher

if __name__ == '__main__':
    # start of main loop
    # for k = 0, niter-1 do begin;n_elements(params[*, 0])-1 do begin

    FadeTypeSwitcher = FadeTypeSwitcher()
    DrivingForceIntegrator = DrivingForceIntegrator()

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

            print(mp)
            print(mdp)
            print(mg)
            print(mass_out_arr)
            print(total_mass_arr)
            print(mdg)
            print(dot_mass_arr)
            print(mddg)
            print(rhogas)
            print(sigma)
            print(phi)
            print(phigrad)
            print(rhogas2)

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
                time_eff = time_arr[k, i]

            luminosity_coef = FadeTypeSwitcher.calc_luminosity_coef(fade, time_eff, quasar_duration)
            print(luminosity_coef)
            luminosity_edd = 1.3e38 * (smbh_masses[k] * unit_mass / 1.989e33) * unit_time / unit_energy  # ;eddington luminosity for the current SMBH mass
            luminosity = luminosity_coef * luminosity_edd
            luminosity_arr[k, index + 1] = luminosity  # ;actual luminosity

            # ;grow the SMBH
            if smbh_grows:
                smbh_mass = smbh_masses[k] * math.exp(luminosity_coef * dt / salpeter_timescale)  #;new BH mass

            # ;SMBH growth and luminosity calculation ends

            a = DrivingForceIntegrator.driving_force_calc(driving_force, mg, radius, eta_drive, integration_method)
            print(a)
            index += 1
            is_main_loop = False
