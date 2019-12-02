from input_parameters.parameters import DRIVING_FORCE
from input_parameters.physics_constants import LIGHT_SPEED
from input_parameters.program_units import *
from input_parameters.program_constants import *
from models.ProfileFormulas import ProfileFormulas


class DrivingForceIntegrator:
    def __init__(self):
        self.Calculator = ProfileFormulas()

    def driving_force_calc(self, driving_force, mg, radius, eta_drive, integration_method, luminosity, mdg, dot_radius,
                           dotdot_radius, mp, mdp, mddg, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, k,
                           index, dt):
        # TODO figure physics meaning of this member
        mg_mp_member = mg * mp + (mg ** 2) / 2.
        # TODO figure physics meaning of this member
        mass_member = (mdg * mp + mg * mdp + mg * mdg) / radius

        if driving_force == DRIVING_FORCE.ENERGY_DRIVING:
            optical_depth = 0.348 / (unit_length ** 2) * unit_mass * mg / (4 * math.pi * (radius ** 2))
            if optical_depth < 1:
                eta_drive = eta_drive * optical_depth
            if eta_drive < 0.05:
                eta_drive = 0.05  # transition to energy-driven wind

            dot_rt = self.dot_rt_initial_calc(mg, radius, eta_drive, luminosity, mdg, dot_radius,
                                              dotdot_radius, mg_mp_member, mass_member, mddg)

            method_name = str(integration_method)
            method = getattr(self, method_name, lambda: 'Invalid')
            return method(dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, k, index, dt, radius,
                          dot_radius,
                          dotdot_radius, eta_drive)
        elif driving_force == DRIVING_FORCE.MOMENTUM_DRIVING:
            # TODO implement momentum driving case
            print(driving_force)

    def simple_integration(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, k, index, dt,
                           radius, dot_radius,
                           dotdot_radius, eta_drive):
        dotdotdot_r = dot_rt * dt #trecia isvestine vadinos dot rt_dt
        dot_rt_arr[k, index] = dot_rt
        dotdot_radius_arr[k, index + 1] = dotdot_radius + dotdotdot_r
        dot_radius_arr[k, index + 1] = dot_radius + dotdot_radius * dt + 0.5 * dot_rt * (dt ** 2)
        artificial_cap = 2 * eta_drive * LIGHT_SPEED
        if dot_radius_arr[k, index + 1] > artificial_cap:
            dot_radius_arr[k, index + 1] = artificial_cap
            if dotdot_radius_arr[k, index + 1] > 0:
                dotdot_radius_arr[k, index + 1] = 0
            if dot_rt_arr[k, index] > 0:
                dot_rt_arr[k, index] = 0

        if dot_radius > artificial_cap:
            radius_arr[k, index + 1] = radius + dot_radius * dt
        else:
            radius_arr[k, index + 1] = radius + dot_radius * dt + 0.5 * dotdot_radius * dt ** 2 + (1. / 6.) * dot_rt * dt ** 3

        return radius_arr, dot_radius_arr, dotdot_radius

    #     arrrddot[k, i + 1] = rdd + rtdot * dt
    #     arrrdot[k, i + 1] = rd + rdd * dt + 0.5 * rtdot * dt ^ 2.
    #     if arrrdot[k, i + 1] gt 2 * eta_dr * cc then begin
    #       arrrdot[k, i + 1] = 2 * eta_dr * cc      ; artificial cap at v_out = 2 * eta_dr * c = v_wind
    #     if arrrddot[k, i + 1] gt 0 then arrrddot[k, i+1] = 0
    #     if arrrtdot[k, i] gt 0 then arrrtdot[k, i] = 0
    #
    # endif
    # if rd gt 2 * eta_dr * cc then arrr[k, i+1] = r + rd * dt else arrr[k, i+1] = r + rd * dt + 0.5 * rdd * dt ^ 2. + (1. / 6.) * rtdot * dt ^ 3.

    def leap_frog_dkd(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, k, index, dt, radius,
                      dot_radius,
                      dotdot_radius, eta_drive):
        # TODO implement leap_frog_dkd
        pass

    def leap_frog_kdk(self, dot_rt, dot_rt_arr, radius_arr, dot_radius_arr, dotdot_radius_arr, k, index, dt, radius,
                      dot_radius,
                      dotdot_radius, eta_drive):
        # TODO implement leap_frog_kdk
        pass

    def dot_rt_initial_calc(self, mg, radius, eta_drive, luminosity, mdg, dot_radius,
                            dotdot_radius, mg_mp_member, mass_member, mddg):
        # TODO figure which ones of these have physical meaning
        mg_r = mg * radius
        mdg_rd_squared = mdg * (dot_radius ** 2)
        rd_r_squared = dot_radius / (radius ** 2)
        add_member_1 = eta_drive * luminosity - mdg_rd_squared - mg * dot_radius * dotdot_radius
        add_member_2 = - 2 * rd_r_squared * mg_mp_member
        add_member = 3. * (GAMMA - 1.) / mg_r * (add_member_1 + add_member_2 + mass_member)
        mg_md_member = mddg * dot_radius / mg + mdg_rd_squared / mg_r
        mg_rdd_member = 2 * mdg * dotdot_radius / mg + dot_radius * dotdot_radius / radius
        add_member_3 = mg_md_member + mg_rdd_member
        add_member_4 = (mass_member - rd_r_squared * mg_mp_member)/mg_r
        sum_members = add_member - add_member_3 - add_member_4

        return sum_members

# rtdot = 3 * (gamma - 1.) / (mg * r) * (
#             eta_dr * lum - mdg * rd ^ 2 - mg * rd * rdd - 2 * rd / r ^ 2 * (mg * mp + mg ^ 2. / 2.) + (
#                 mdg * mp + mg * mdp + mg * mdg) / r) - (
#                     mddg * rd / mg + mdg * rd ^ 2 / (mg * r) + 2 * mdg * rdd / mg + rd * rdd / r) - (
#                     (mdg * mp + mg * mdp + mg * mdg) / r - rd / r ^ 2 * (mg * mp + mg ^ 2. / 2.)) / (
#                     mg * r)  # ;eom for arbitrary coupling eta and arbitrary gamma of the outflowing material
