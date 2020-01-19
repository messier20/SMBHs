import matplotlib.pyplot as plt
import numpy as np
from model_program.input_parameters.galaxy_parameters import bulge_masses
from plotting_program.plots.plots_settings import graphs_path, plots_version_folder


def plotting_mbulge_relation(dot_mass, dot_radius, additional_name):
    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'orange']
    fig, ax = plt.subplots()
    # print()
    dot_mass = np.array(dot_mass)
    ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
    ax.set_yscale('log')
    # ax.set_xscale('log')
    ax.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    ax.set_xlabel('Bulge mass [$M_{sun}$]')
    # print(dot_mass)
    ax.set_ylim(900, 20000)
    ax.set_xlim(5.e9, 4.e11)
    # ax.plot([bulge_masses,bulge_masses,bulge_masses,bulge_masses,bulge_masses], [dot_mass[0,], dot_mass[1,], dot_mass[2,], dot_mass[3,], dot_mass[4,]])
    ax.scatter(bulge_masses, dot_mass[0,], label = labels[0], color = colors[0], s=7)
    ax.scatter(bulge_masses, dot_mass[1,], label = labels[1], color = colors[1], s=7)
    ax.scatter(bulge_masses, dot_mass[2,], label = labels[2], color = colors[2], s=7)
    ax.scatter(bulge_masses, dot_mass[3,], label = labels[3], color = colors[3], s=7)
    ax.scatter(bulge_masses, dot_mass[4,], label = labels[4], color = colors[4], s=7)
    # ax.plot(bulge_masses, dot_mass[0,], '--', color=colors[0], linewidth=1)
    # ax.plot(bulge_masses, dot_mass[1,], '--', color=colors[1], linewidth=1)
    # ax.plot(bulge_masses, dot_mass[2,], '--', color=colors[2], linewidth=1)
    # ax.plot(bulge_masses, dot_mass[3,], '--', color=colors[3], linewidth=1)
    # ax.plot(bulge_masses, dot_mass[4,], '--', color=colors[4], linewidth=1)
    ax.legend(loc='upper right')
    # ax.legend(loc='upper left')
    fig.savefig(graphs_path + plots_version_folder + 'dot-mass-bulge-mass-' + additional_name + '-sctr-log.png', bbox_inches='tight')

    dot_radius = np.array(dot_radius)
   #  ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
   #  ax.set_yscale('log')
   #  ax.set_xscale('log')
   #  # print(dot_mass)
   #  ax.set_xlim(1.9e10, 4e11)
   #  ax.set_ylim(200, 1600)
   #  ax.set_ylabel('Velocity [km/s]')
   #  ax.set_xlabel('Bulge mass [$M_{sun}$]')
   #  ax.scatter(bulge_masses, dot_radius[0,], label = labels[0], color = colors[0], s=7)
   #  ax.scatter(bulge_masses, dot_radius[1,], label = labels[1], color = colors[1], s=7)
   #  ax.scatter(bulge_masses, dot_radius[2,], label = labels[2], color = colors[2], s=7)
   #  ax.scatter(bulge_masses, dot_radius[3,], label = labels[3], color = colors[3], s=7)
   #  ax.scatter(bulge_masses, dot_radius[4,], label = labels[4], color = colors[4], s=7)
   #  ax.plot(bulge_masses, dot_radius[0,], '--', color=colors[0], linewidth=1)
   #  ax.plot(bulge_masses, dot_radius[1,], '--', color=colors[1], linewidth=1)
   #  ax.plot(bulge_masses, dot_radius[2,], '--', color=colors[2], linewidth=1)
   #  ax.plot(bulge_masses, dot_radius[3,], '--', color=colors[3], linewidth=1)
   #  ax.plot(bulge_masses, dot_radius[4,], '--', color=colors[4], linewidth=1)
   #  ax.legend(loc='lower left')
   #
   #  fig.savefig(graphs_path + plots_version_folder + 'dot-radius-bulge-mass-' + additional_name + '-sctr-line-log.png',
   #              bbox_inches='tight')
   #