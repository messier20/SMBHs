import math

from models.ProfileFormulas import ProfileFormulas


class NFW:
    def __init__(self, total_mass, radius_scaled, concentration):
        self.total_mass = total_mass
        self.radius_scaled = radius_scaled
        self.concentration = concentration
        self.Calculator = ProfileFormulas(self.total_mass)
        self.radius_scaled_member = self.radius_scaled / (1 + self.radius_scaled)
        self.concentration_member = (math.log(1 + self.concentration) - self.concentration / (1 + self.concentration))
        self.first_multip_member = self.total_mass / self.concentration_member

    def calc_mass(self, total_mass, dot_radius, dotdot_radius, halo_scale, radius_scaled):
        mass_t = self.Calculator.calc_mt(total_mass, 1., self.concentration_member,
                                         (math.log(1 + self.radius_scaled) - self.radius_scaled_member))
        dot_mass_t = self.Calculator.calc_mt(total_mass, 1., self.concentration_member,
                                             (dot_radius / halo_scale * (self.radius_scaled_member ** 2)))

        third_mddt = dotdot_radius / halo_scale * (self.radius_scaled_member ** 2) + (dot_radius ** 2) / (
                halo_scale ** 2) * (1. - radius_scaled) / ((1 + radius_scaled) ** 3)
        dotdot_mass_t = self.Calculator.calc_mt(total_mass, 1., self.concentration_member, third_mddt)
        # TODO figure out why in idl code ! was written before pi
        density = self.Calculator.calc_density(total_mass, 4., halo_scale, self.radius_scaled_member ** 2,
                                               self.concentration_member)
        radius_scaled_with_coef = (4. * radius_scaled / 3.) / (1. + (4. * radius_scaled / 3.) ** 2)
        density2 = self.Calculator.calc_density(total_mass, 4., halo_scale, radius_scaled_with_coef,
                                                self.concentration_member)
        phi = self.Calculator.calc_phi(-total_mass, halo_scale, self.concentration_member,
                                       math.log(1. + radius_scaled) / radius_scaled)
        phi_grad = self.Calculator.calc_phi(total_mass, halo_scale ** 2, self.concentration_member,
                                            (math.log(1. + radius_scaled) - self.radius_scaled_member) / (
                                                        radius_scaled ** 2))
        return mass_t, dot_mass_t, dotdot_mass_t, density, density2, phi, phi_grad

    # def rho(self, total_mass, concentration_member, halo_scale, radius_scaled_member):
    #
    #     a = self.Calculator.multiply(4, math.pi, halo_scale ** 3, concentration_member)
    #     return total_mass / a / (radius_scaled_member ** 2)

