import math


class Isothermal:
    def __init__(self):
        pass

    def calculate(self, mass, radius, dot_radius, dotdot_radius, bulge_scale):
        mb = mass * radius / bulge_scale
        mdb = mass * dot_radius / bulge_scale
        mddb = mass * dotdot_radius / bulge_scale
        rho = mass / (4 * math.pi * (radius ** 3))
        rho2 = mass / (4 * math.pi * ((4. * radius / 3.) ** 3))
        phi = mass / radius * math.log(radius / (2.718281828 * 10 * bulge_scale))
        phigrad = mass / (radius ** 2)

        if mb > mass:
            mb = mass
            mdb = 0
            mddb = 0
            phi = - mb / radius
            phigrad = mb / (radius ** 2)

        return mb, mdb, mddb, rho, rho2, phi, phigrad
