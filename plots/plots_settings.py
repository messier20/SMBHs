import os
from input_parameters.initial_values import version

graphs_path = '/home/monika/Documents/SMBHs/results/graphs/'
plots_version_folder = 'v' + str(version)+'/'
# plots_version_folder = ''
try:
    os.mkdir(graphs_path + plots_version_folder)
except:
    pass


plot_velocities = 0
plot_massrate = 0
plot_momentum = 0                   #plots both momentum and energy of the outflow
plot_momentumvsl = 0
plot_pressures = 0
plot_sf = 0
plot_sixpart = 0
plot_threepart = 1
plot_enloadingandr = 0
plot_vandr = 0
plot_enloadingandv = 0
plot_ratios = 0