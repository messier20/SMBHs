import math

# TODO remove calculations from constructor and transfer it to calc_mass
class NFW:
    def __init__(self, total_mass, radius_scaled, concentration):
        self.total_mass = total_mass
        self.radius_scaled = radius_scaled
        self.concentration = concentration
        self.radius_scaled_member = self.radius_scaled / (1 + self.radius_scaled)
        # TODO figure out physics meaning for this member
        self.radius_scaled_squared_member = self.radius_scaled / ((1 + self.radius_scaled) ** 2)
        # TODO figure out physics meaning for this member
        self.concentration_member = (math.log(1 + self.concentration) - self.concentration / (1 + self.concentration))

    def calc_mass(self, total_mass, dot_radius, dotdot_radius, halo_scale, radius_scaled, radius):
        """
        :rtype: list
        :param total_mass:
        :param dot_radius:
        :param dotdot_radius:
        :param halo_scale:
        :param radius_scaled:
        :param radius:
        :return: mt, mdt, mddt, rho, rho2, phi, phigrad
        """
        mass_t = total_mass / self.concentration_member * (math.log(1 + self.radius_scaled) - self.radius_scaled_member)
        dot_mass_t = total_mass / self.concentration_member * (
                (dot_radius / halo_scale) * self.radius_scaled_squared_member)

        third_mddt = dotdot_radius / halo_scale * self.radius_scaled_squared_member + (dot_radius ** 2) / (
                halo_scale ** 2) * (1. - radius_scaled) / ((1 + radius_scaled) ** 3)
        dotdot_mass_t = total_mass / self.concentration_member * third_mddt

        density = total_mass / (
                4 * math.pi * (halo_scale ** 3) * self.radius_scaled_squared_member) / self.concentration_member
        radius_scaled_with_coef = (4. * radius_scaled / 3.) / (1. + (4. * radius_scaled / 3.) ** 2)
        density2 = total_mass / (4 * math.pi * (halo_scale ** 3) * radius_scaled_with_coef) / self.concentration_member

        phi = -total_mass / halo_scale / self.concentration_member * (math.log(1. + radius_scaled) / radius_scaled)
        phi_grad = total_mass / (halo_scale ** 2) / self.concentration_member * ((math.log(1. + radius_scaled) -
                                                                self.radius_scaled_member) / (radius_scaled ** 2))

        mass_five_times = 5. * total_mass
        if mass_t > mass_five_times:
            mass_t = mass_five_times
            dot_mass_t = 0
            dotdot_mass_t = 0
            density = 0
            phi = -mass_five_times / radius
            phi_grad = mass_five_times / (radius ** 2)

        return mass_t, dot_mass_t, dotdot_mass_t, density, density2, phi, phi_grad
