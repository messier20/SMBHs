import math


class ProfileFormulas:
    def __init__(self):
        pass

    @staticmethod
    def calc_mass(mass, radius, distance1, distance2=1):
        return mass * radius / distance1 * distance2

    @staticmethod
    def calc_density(mass, coef, radius, distance=1, concentration=1):
        return mass / (coef * math.pi * (radius ** 3) * concentration) / distance

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
    def calc_phi(mass, distance, concentration1=1, concentration2=1):
        """
        mass/distance/concentration[0]*concentration[1]
        :rtype: float
        :param mass: Required
        :param distance: Required
        :param concentration1: Not required, but when using, pass two params so the calculation would be correct. Pass only for NFW model
        :param concentration2: Not required, but when using, pass two params so the calculation would be correct. Pass only for NFW model
        :return: phi
        """
        return mass / distance / concentration1 * concentration2
