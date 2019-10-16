import math
from models.ProfileFormulas import ProfileFormulas


class Isothermal:
    def __init__(self):
        self.Callculator = ProfileFormulas()

    def calculate(self, mass, radius, dot_radius, dotdot_radius, bulge_scale):
        mb = self.Callculator.calc_mass(mass, radius, bulge_scale)
        mdb = self.Callculator.calc_mass(mass, dot_radius, bulge_scale)
        mddb = self.Callculator.calc_mass(mass, dotdot_radius, bulge_scale)
        rho = self.Callculator.calc_density(mass, 4, radius)
        rho2 = self.Callculator.calc_density(mass, 4, (4. * radius / 3.))
        phi = mass / radius * math.log(radius / (2.718281828 * 10 * bulge_scale))
        # print(mass, ' mass')
        # print(radius, ' radius')
        phigrad = mass / (radius ** 2)

        if mb > mass:
            mb = mass
            mdb = 0
            mddb = 0
            phi = - mb / radius
            phigrad = mb / (radius ** 2)

        return mb, mdb, mddb, rho, rho2, phi, phigrad
