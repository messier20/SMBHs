import numpy as np

from input_parameters.program_constants import ITERATIONS_NUM, TIMESTEPS_NUMB


def init_zero_arrays():
    radius_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    dot_radius_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    dotdot_radius_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    delta_radius_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    mass_out_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    total_mass_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    dot_mass_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    dot_rt_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    time_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    dot_time_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    luminosity_AGN_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
    pressure_contact_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))  # ;array to hold information about pressures at contact discontinuity
    pressure_outer_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))  # ;array to hold information about pressures at outer shock
    bulge_mass_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))

    return radius_arr, dot_radius_arr, dotdot_radius_arr, delta_radius_arr, mass_out_arr, total_mass_arr, dot_mass_arr, \
           dot_rt_arr, time_arr, dot_time_arr, luminosity_AGN_arr, pressure_contact_arr, pressure_outer_arr, bulge_mass_arr
