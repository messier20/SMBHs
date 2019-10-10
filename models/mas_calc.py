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
    halo_profile_ans = NFWHaloProfile.calc_mass()
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

#
#
#
# def halo_profile

# function
# masscalc, rvals, word_params, num_params;
# r, rdot, rddot, mtot, halo_profile, rvir, conc, bulge_profile, bulge_scale, disc_profile, disc_scale, fg, bt
#
# ; This
# function
# calculates
# the
# values
# of
# m( < r), mdot( < r) and
# ; mddot( < r), required
# for the equation of motion, separated into
# ; background
# potential and gas
# parts.It
# can
# do
# that
# for
#     ; any
#     halo, bulge and disc
#     profile
#     encoded, and for any given gas
# ; fraction and bulge_to_total
# ratio.sigma is the
# maximum
# effective
# ; velocity
# dispersion, i.e.v_c, max / sqrt(2), assuming
# all
# gas is
# ; distributed as in the
# halo._scale
# are
# scale
# factors
# of
# the
# ; potentials(not required in the
# isothermal
# model)
#
# ; for the moment, the gravity due to disc is neglected to keep the
# ; calculation
# strictly
# spherically
# symmetric
#
#
# @natconst.pro
#
#
# r = rvals[0]
# rdot = rvals[1]
# rddot = rvals[2]
# if n_elements(rvals) gt 3 then deltar=rvals[3] else deltar = 0.
# halo_profile = word_params[0]
# bulge_profile = word_params[1]
# disc_profile = word_params[2]
# mtot = num_params[0]
# rvir = num_params[1]
# conc = num_params[2]
# bulge_scale = num_params[3]
# disc_scale = num_params[4]
# fbt = num_params[5]
# fgh = num_params[6]
# fgb = num_params[7]
# bt = num_params[8]
#
# halo_scale = rvir / conc
# x = r / halo_scale
#
# case
# halo_profile
# of
# 'Isothermal': begin
# mt = mtot * r / rvir
# mdt = mtot * rdot / rvir
# mddt = mtot * rddot / rvir
# rho = mtot / (4 *!pi * (r) ^ 3.)
# rho2 = mtot / (4 *!pi * (4. * r / 3.) ^ 3.);factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# phi = mt / r * alog(r / (2.718281828 * rvir))
# phigrad = mt / r ^ 2.
# if mt gt mtot then begin
# mt = mtot
# mdt = 0.
# mddt = 0.
# rho = 0.
# phi = -mtot / r
# phigrad = mtot / r ^ 2.
# endif
# end
# 'Hernquist': begin
# mt = mtot * x ^ 2. / (1 + x) ^ 2.
# mdt = mtot * rdot / halo_scale * 2 * x / (1 + x) ^ 3.
# mddt = mtot * 2 / (1 + x) ^ 3. * (rddot / halo_scale * x + rdot ^ 2. / halo_scale ^ 2. * (1. - 2 * x) / (1. + x))
# rho = mtot / (2 *!pi * halo_scale ^ 3.) / (x) / (1 + (x)) ^ 3.
# rho2 = mtot / (2 *!pi * halo_scale ^ 3.) / (4. * x / 3.) / (1 + (4. * x / 3.)) ^ 3.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# end
# 'Jaffe': begin;
# needs
# double - checking!
# mt = mtot * x / (1 + x)
# mdt = mtot * rdot / halo_scale * (1 + x) ^ (-2.)
# mddt = mtot * (rddot / halo_scale * (1 + x) ^ (-2.) - rdot ^ 2. / halo_scale ^ 2. * 2 * (1 + x) ^ (-3.))
# rho = mtot / (4 *!pi * halo_scale ^ 3.) / x ^ 2. / (1 + x) ^ 2.
# rho2 = mtot / (4 *!pi * halo_scale ^ 3.) / (4. * x / 3.) ^ 2. / (1 + (4. * x / 3.)) ^ 2.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# end
# 'NFW': begin
# mt = mtot / (alog(1 + conc) - conc / (1. + conc)) * (alog(1 + x) - x / (1 + x))
# ;      if mt gt mtot then mt = mtot
# mdt = mtot / (alog(1 + conc) - conc / (1. + conc)) * rdot / halo_scale * x / (1 + x) ^ 2.
# mddt = mtot / (alog(1 + conc) - conc / (1. + conc)) * (
#             rddot / halo_scale * x / (1 + x) ^ 2. + rdot ^ 2. / halo_scale ^ 2. * (1. - x) / (1 + x) ^ (3.))
# rho = mtot / (4 *!pi * halo_scale ^ 3. * (alog(1.+conc) - conc / (1. + conc))) / (x) / (1 + (x)) ^ 2.
# rho2 = mtot / (4 *!pi * halo_scale ^ 3. * (alog(1.+conc) - conc / (1. + conc))) / (4. * x / 3.) / (
#             1 + (4. * x / 3.)) ^ 2.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# phi = -mtot / halo_scale / (alog(1 + conc) - conc / (1. + conc)) * alog(1 + x) / x
# phigrad = mtot / halo_scale ^ 2. / (alog(1 + conc) - conc / (1. + conc)) * (alog(1. + x) - x / (1. + x)) / x ^ 2.
# if mt gt 5. * mtot then begin
# mt = 5. * mtot
# mdt = 0.
# mddt = 0.
# rho = 0.
# phi = -5. * mtot / r
# phigrad = 5. * mtot / r ^ 2.
# endif
# end
# endcase
#
# mhp = mt * (1 - fbt) * (1 - fgh)
# mdhp = mdt * (1 - fbt) * (1 - fgh)
# mddhp = mddt * (1 - fbt) * (1 - fgh)
# phihp = phi * (1 - fbt) * (1 - fgh)
# phigradhp = phigrad * (1 - fbt) * (1 - fgh)
#
# mhg = mt * (1 - fbt) * fgh
# mdhg = mdt * (1 - fbt) * fgh
# mddhg = mddt * (1 - fbt) * fgh
# phihg = phi * (1 - fbt) * fgh / 2.
# phigradhg = phigrad * (1 - fbt) * fgh / 2.
#
# phih = phihp + phihg
# phigradh = phigradhp + phigradhg
#
# rhohgas = rho * (1 - fbt) * fgh
# rhohgas2 = rho2 * (1 - fbt) * fgh
#
# mbb = bt * fbt * mtot
# x = r / bulge_scale
#
# case
# bulge_profile
# of
# 'Isothermal': begin
# mb = mbb * r / bulge_scale
# mdb = mbb * rdot / bulge_scale
# mddb = mbb * rddot / bulge_scale
# rho = mbb / (4 *!pi * (r) ^ 3.)
# rho2 = mbb / (4 *!pi * (4. * r / 3.) ^ 3.);factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# phi = mbb / r * alog(r / (2.718281828 * 10 * bulge_scale))
# phigrad = mbb / r ^ 2.
# if mb gt mbb then begin
# mb = mbb
# mdb = 0.
# mddb = 0.
# rho = 0.
# phi = -mb / r
# phigrad = mb / r ^ 2.
# endif
# end
# 'Hernquist': begin
# mb = mbb * x ^ 2. / (1 + x) ^ 2.
# mdb = mbb * rdot / bulge_scale * 2 * x / (1 + x) ^ 3.
# mddb = mbb * 2 / (1 + x) ^ 3. * (rddot / bulge_scale * x + rdot ^ 2. / bulge_scale ^ 2. * (1. - 2 * x) / (1. + x))
# rho = mbb / (2 *!pi * bulge_scale ^ 3.) / (x) / (1 + (x)) ^ 3.
# rho2 = mbb / (2 *!pi * bulge_scale ^ 3.) / (4. * x / 3.) / (1 + (4. * x / 3.)) ^ 3.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# phi = -mbb / bulge_scale / (1 + x)
# phigrad = mbb / bulge_scale ^ 2. / (1. + x) ^ 2.
# end
# 'Jaffe': begin
# mb = mbb * x / (1 + x)
# mdb = mbb * rdot / bulge_scale * (1 + x) ^ (-2.)
# mddb = mbb * (rddot / bulge_scale * (1 + x) ^ (-2.) - rdot ^ 2. / bulge_scale ^ 2. * 2 * (1 + x) ^ (-3.))
# rho = mbb / (4 *!pi * bulge_scale ^ 3.) / x ^ 2. / (1 + x) ^ 2.
# rho2 = mbb / (4 *!pi * bulge_scale ^ 3.) / (4. * x / 3.) ^ 2. / (1 + (4. * x / 3.)) ^ 2.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# end
# 'NFW': begin
# mb = mbb * (alog(1 + x) - x / (1 + x))
# mdb = mbb / (alog(1 + conc) - conc / (1. + conc)) * rdot / bulge_scale * x / (1 + x) ^ 2.
# mddb = mbb / (alog(1 + conc) - conc / (1. + conc)) * (
#             rddot / bulge_scale * x / (1 + x) ^ 2. + rdot ^ 2. / bulge_scale ^ 2. * (1. - x) / (1 + x) ^ (3.))
# rho = mbb / (4 *!pi * bulge_scale ^ 3. * (alog(1.+conc) - conc / (1. + conc))) / x / (1 + x) ^ 2.
# rho2 = mbb / (4 *!pi * bulge_scale ^ 3. * (alog(1.+conc) - conc / (1. + conc))) / (4. * x / 3.) / (
#             1 + (4. * x / 3.)) ^ 2.;
# factor
# 4 / 3
# required
# because
# we
# are
# interested in density
# at
# the
# outer
# shock, which is 4 / 3
# times
# the
# distance
# of
# the
# contact
# discontinuity
# end
# endcase
#
# mbp = mb * (1 - fgb)
# mdbp = mdb * (1 - fgb)
# mddbp = mddb * (1 - fgb)
# phibp = phi * (1 - fgb)
# phigradbp = phigrad * (1 - fgb)
#
# mbg = mb * fgb
# mdbg = mdb * fgb
# mddbg = mddb * fgb
# phibg = phi * fgb / 2.
# phigradbg = phigrad * fgb / 2.
#
# phib = phibp + phibg
# phigradb = phigradbp + phigradbg
#
# rhobgas = rho * fgb
# rhobgas2 = rho2 * fgb
#
# deltaphi = 4 *!pi * r ^ 2 * (rhohgas + rhobgas) * deltar * (1 + deltar / r + deltar ^ 2 / (3. * r ^ 2)) * (phih + phib)
#
# sigma = sqrt((mt * (1 - fbt) + mb) / 2 / r)
#
# output = [mhp + mbp, mdhp + mdbp, mhg + mbg, mdhg + mdbg, mddhg + mddbg, rhohgas + rhobgas, sigma, deltaphi,
#           phih + phib, phigradh + phigradb, rhohgas2 + rhobgas2]
#
# ;stop
# return, output
# end
#
