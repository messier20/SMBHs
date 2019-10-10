from models.ProfileFormulas import ProfileFormulas


class Isothermal:
    def __init__(self, mass, r, virial_radius):
        self.total_mass = mass
        self.radius = r
        self.virial_radius = virial_radius

    def calculate(self):
        Callculator = ProfileFormulas(self.total_mass)
        return Callculator.calc_masst(self.radius, self.virial_radius)
