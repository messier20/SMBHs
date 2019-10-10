class ProfileFormulas:
    def __init__(self, total_mass):
        self.total_mass = total_mass

    def calc_masst(self, radius, distance):
        print(self.total_mass/distance, 'd')
        return self.total_mass * radius / distance
