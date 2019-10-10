import math

from models.ProfileFormulas import ProfileFormulas


class NFW:
    def __init__(self, total_mass, radius_scaled, concentration):
        self.total_mass = total_mass
        self.radius_scaled = radius_scaled
        self.concentration = concentration

        self.Calculator = ProfileFormulas(self.total_mass)

    def calc_mass(self):
        masst = self.distance()
        return masst

    def radius(self):
        return math.log(1 + self.radius_scaled) - self.radius_scaled / 1 + self.radius_scaled

    def distance(self):

        return self.total_mass /(math.log(1 + self.concentration) - self.concentration / (1 + self.concentration)) * (
                math.log(1 + self.radius_scaled) - self.radius_scaled / (1 + self.radius_scaled))

