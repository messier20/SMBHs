# TODO good naming? Or better dot_R, dotdot_R and add legend that R stands for radius?
# r = radius r = rvals[0]
# rdot = rvals[1] -> dot_radius
# rddot = rvals[2] -> dotdot_radius
# deltar=rvals[3]/0 -> delta_radius
# halo_profile = word_params[0]
# bulge_profile = word_params[1]
# disc_profile = word_params[2]
# mtot = num_params[0] -> total_mass
# rvir = num_params[1] -> virial_radius
# conc = num_params[2] -> halo_concentration_parameter
# bulge_scale = num_params[3] -->> could be bulge_scaled?
# disc_scale = num_params[4] -->> could be disc_scaled?
# fbt = num_params[5] -> bulge_disc_totalmass_fraction,
# fgh = num_params[6] -> halo_gas_fraction
# bulge_disc_gas_fraction = num_params[7] -> bulge_disc_gas_fraction
# bt = num_params[8] -> bulge_totalmass
from decimal import Decimal

from models.Isothermal import Isothermal
from models.NFW import NFW
from models.ProfileFormulas import ProfileFormulas
import math


# TODO figure out correct names for variables from physics
# TODO make this file readable

def mass_calculation(radius, dot_radius, dotdot_radius, delta_radius, halo_profile, bulge_profile, disc_profile,
                     total_mass, virial_radius, halo_concentration_parameter, bulge_scale, disc_scale,
                     bulge_disc_totalmass_fraction, halo_gas_fraction, bulge_disc_gas_fraction, bulge_totalmass):
    """

    :param radius:
    :param dot_radius:
    :param dotdot_radius:
    :param delta_radius:
    :param halo_profile:
    :param bulge_profile:
    :param disc_profile:
    :param total_mass:
    :param virial_radius:
    :param halo_concentration_parameter:
    :param bulge_scale:
    :param disc_scale:
    :param bulge_disc_totalmass_fraction:
    :param halo_gas_fraction:
    :param bulge_disc_gas_fraction:
    :param bulge_totalmass:
    :return: mp, mdp, mg, mdg, mddg, rhogas, sigma, deltaphi, phi, phigrad, rhogas2
    """
    Calculator = ProfileFormulas()

    halo_scale = virial_radius / halo_concentration_parameter
    radius_scaled = radius / halo_scale

    NFWHaloProfile = NFW(total_mass, radius_scaled, halo_concentration_parameter)
    (mt, mdt, mddt, rho_halo, rho2_halo, phi_halo, phi_grad_halo) = NFWHaloProfile.calc_mass(total_mass, dot_radius,
                                                                                             dotdot_radius, halo_scale,
                                                                                             radius_scaled, radius)

    bulge_disc_mass_member = 1 - bulge_disc_totalmass_fraction
    halo_gas_member = 1 - halo_gas_fraction
    bulge_halo_members = bulge_disc_mass_member * halo_gas_member

    mhp = mt * bulge_halo_members
    mdhp = mdt * bulge_halo_members
    mddhp = mddt * bulge_halo_members
    phihp = phi_halo * bulge_halo_members
    phigradhp = phi_grad_halo * bulge_halo_members

    mhg = mt * bulge_disc_mass_member * halo_gas_fraction
    mdhg = mdt * bulge_disc_mass_member * halo_gas_fraction
    mddhg = mddt * bulge_disc_mass_member * halo_gas_fraction
    phihg = phi_halo * bulge_disc_mass_member * halo_gas_fraction / 2
    phigradhg = phi_grad_halo * bulge_disc_mass_member * halo_gas_fraction / 2

    phih = phihp + phihg
    phigradh = phigradhp + phigradhg

    rhohgas = rho_halo * bulge_disc_mass_member * halo_gas_fraction
    rhohgas2 = rho2_halo * bulge_disc_mass_member * halo_gas_fraction

    #
    mbb = bulge_totalmass * bulge_disc_totalmass_fraction * total_mass  # mbb - what's that?
    bulge_scaled = radius / bulge_scale

    IsothermalBulgeProfile = Isothermal()
    # TODO think how to write these in more readable way
    (mb, mdb, mddb, rho_bulge, rho2_bulge, phi_bulge, phi_grad_bulge) = IsothermalBulgeProfile.calculate(mbb, radius,
                                                                                                         dot_radius,
                                                                                                         dotdot_radius,
                                                                                                         bulge_scale)
    bulge_disc_gas_member = 1 - bulge_disc_gas_fraction

    mbp = mb * bulge_disc_gas_member
    mdbp = mdb * bulge_disc_gas_member
    mddbp = mddb * bulge_disc_gas_member
    phibp = phi_bulge * bulge_disc_gas_member
    phigradbp = phi_grad_bulge * bulge_disc_gas_member

    mbg = mb * bulge_disc_gas_fraction
    mdbg = mdb * bulge_disc_gas_fraction
    mddbg = mddb * bulge_disc_gas_fraction
    phibg = phi_bulge * bulge_disc_gas_fraction / 2.
    phigradbg = phi_grad_bulge * bulge_disc_gas_fraction / 2.

    phib = phibp + phibg
    phigradb = phigradbp + phigradbg

    rhobgas = rho_bulge * bulge_disc_gas_fraction
    rhobgas2 = rho2_bulge * bulge_disc_gas_fraction

    # TODO remove usage of my Calculator
    deltaphi = Calculator.multiply(4, math.pi, radius ** 2, (rhohgas + rhobgas), delta_radius,
                                   1 + delta_radius / radius + (delta_radius ** 2) / (3. * radius ** 2), phih + phib)

    sigma = math.sqrt(mt * bulge_disc_mass_member + mb / 2 / radius)

    return mhp + mbp, mdhp + mdbp, mhg + mbg, mdhg + mdbg, mddhg + mddbg, rhohgas + rhobgas, sigma, deltaphi, phih + \
           phib, phigradh + phigradb, rhohgas2 + rhobgas2, mb
