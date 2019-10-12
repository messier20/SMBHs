# good naming? Or better dot_R, dotdot_R and add legend that R stands for radius?
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
# fgb = num_params[7] -> bulge_disc_gas_fraction
# bt = num_params[8] -> bulge_totalmass
from models.Isothermal import Isothermal
from models.NFW import NFW


def mass_calculation(radius, dot_radius, dotdot_radius, delta_radius, halo_profile, bulge_profile, disc_profile,
                     total_mass, virial_radius, halo_concentration_parameter, bulge_scale, disc_scale,
                     bulge_disc_totalmass_fraction, halo_gas_fraction, bulge_disc_gas_fraction, bulge_totalmass):

    halo_scale = virial_radius/halo_concentration_parameter
    radius_scaled = radius/halo_scale

    NFWHaloProfile = NFW(total_mass, radius_scaled, halo_concentration_parameter)
    halo_profile_ans = NFWHaloProfile.calc_mass(total_mass, dot_radius, dotdot_radius, halo_scale, radius_scaled)
    print(halo_profile_ans, 'halo')

    #
    mbb = bulge_totalmass * bulge_disc_totalmass_fraction * total_mass      # mbb - what's that?

    IsothermalBulgeProfile = Isothermal(mbb, radius, bulge_scale)
    mass = IsothermalBulgeProfile.calculate()
    print(mass, 'mass')
    print(bulge_profile)

    return radius, dot_radius, dotdot_radius, delta_radius, halo_profile, bulge_profile, \
           disc_profile, total_mass, virial_radius, halo_concentration_parameter, bulge_scale, disc_scale,\
           bulge_disc_totalmass_fraction, halo_gas_fraction, bulge_disc_gas_fraction, bulge_totalmass
