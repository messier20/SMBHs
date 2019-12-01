import numpy as np

from input_parameters.program_constants import ITERATIONS_NUM, TIMESTEPS_NUMB
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
luminosity_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))
pressure_contact_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))  #;array to hold information about pressures at contact discontinuity
pressure_outer_arr = np.zeros((ITERATIONS_NUM, TIMESTEPS_NUMB))  #;array to hold information about pressures at outer shock
