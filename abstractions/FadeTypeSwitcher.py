from input_parameters.galaxy_parameters import drop_timescale, eddingtion_ration, alpha_drop
import math


class FadeTypeSwitcher:
    def __init__(self):
        pass

    def calc_luminosity_coef(self, type, eff_time, quasar_duration):
        method_name = str(type)
        method = getattr(self, method_name, lambda: 'Invalid')
        return method(eff_time, quasar_duration)

    def none(self, eff_time, quasar_duration):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ration
        else:
            return 0

    def exponential(self, eff_time, quasar_duration):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ration
        else:
            return eddingtion_ration * math.exp(-(eff_time - quasar_duration) / drop_timescale)

    def power_law(self, eff_time, quasar_duration):
        if self.is_eff_time_less_then_quasar_duration(eff_time, quasar_duration):
            return eddingtion_ration
        else:
            return eddingtion_ration * (eff_time / quasar_duration) ** (-1. * alpha_drop)

    def king(self, eff_time, quasar_duration):
        return eddingtion_ration * (1 + eff_time / quasar_duration) ** (-19. / 16.)

    def is_eff_time_less_then_quasar_duration(self, eff_time, quasar_duration):
        if eff_time <= quasar_duration:
            return True
        else:
            return False
