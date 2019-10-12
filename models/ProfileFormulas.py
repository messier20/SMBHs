import math


class ProfileFormulas:
    def __init__(self, total_mass):
        self.total_mass = total_mass
        self.multiply = self.multiply()

    @staticmethod
    def calc_mt(total_mass, radius, distance1, *distance2):
        try:
            distance2[0]
        except IndexError:
            return total_mass * radius / distance1
        else:
            return total_mass * radius / distance1 * distance2[0]

    @staticmethod
    def calc_density(total_mass, coef, radius, distance, *concentration):
        try:
            concentration[0]
        except IndexError:
            return total_mass / (coef * math.pi * (radius ** 3)) / distance
        else:
            return total_mass / (coef * math.pi * (radius ** 3) * concentration[0]) / distance

    @staticmethod
    def multiply(*args):
        """
        Multiplies all of the passed parameters
        :param args:
        :return:
        """
        multiplication_res = 1
        for a in args:
            multiplication_res = a * multiplication_res
        return multiplication_res

    @staticmethod
    def calc_phi(mass, distance, *concentration):
        """
        mass/distance/concentration[0]*concentration[1]
        :rtype: float
        :param mass: Required
        :param distance: Required
        :param concentration: Not required, but when using, pass two params so the calculation would be correct. Pass only for NFW model
        :return: phi
        """
        try:
            concentration[0]
            concentration[1]
        except IndexError:
            return mass / distance
        else:
            return mass / distance / concentration[0] * concentration[1]
