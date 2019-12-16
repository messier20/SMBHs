import matplotlib.pyplot as plt
import numpy as np

from plots.PlotSetup import PlotSetup
from plots.plots_settings import *

def plotting_r_relation(radius, dot_radius, mass_out, dot_mass, model_type, type_name):
    # graphs_path = '/home/monika/Documents/SMBHs/plots/'
    Plot = PlotSetup()

    fig1, ax1 = Plot.setup_common_properties()
    # ax1.set_ylim(1.e-2, 1.e2)
    ax1.set_ylabel('velocity [$km/s$]')
    ax1.set_xlabel('radius [$kpc$]')
    ax1.set_yscale('log')
    ax1.set_xscale('log')
    p1 = ax1.scatter(radius[0,], dot_radius[0,], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax1.scatter(radius[1,], dot_radius[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax1.scatter(radius[2,], dot_radius[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax1.scatter(radius[3,], dot_radius[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax1.scatter(radius[4,], dot_radius[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)
    ax1.set_title(model_type + '$x10^{9}$')

    Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
    fig1.savefig(graphs_path + plots_version_folder + 'vel_radius_' + type_name + str(model_type) + '.png', bbox_inches='tight')
    plt.close(fig1)

    fig2, ax2 = Plot.setup_common_properties()
    ax2.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    ax2.set_xlabel('radius [$kpc$]')
    ax2.set_yscale('log')
    # ax2.set_xscale('log')

    p1 = ax2.scatter(radius[0,], dot_mass[0,], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax2.scatter(radius[1,], dot_mass[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax2.scatter(radius[2,], dot_mass[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax2.scatter(radius[3,], dot_mass[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax2.scatter(radius[4,], dot_mass[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)
    ax2.set_title(model_type + '$x10^{9}$')

    Plot.add_legend_gas_fractions(ax2, p1, p2, p3, p4, p5)
    fig2.savefig(graphs_path + plots_version_folder + 'dotmass_radius_' + type_name + str(model_type) + '.png',
                 bbox_inches='tight')
    plt.close(fig2)

    fig3, ax3 = Plot.setup_common_properties()
    ax3.set_ylabel('Mass outflow [$M_{sun}}$]')
    ax3.set_xlabel('radius [$kpc$]')

    ax3.set_yscale('log')
    ax3.set_xscale('log')
    p1 = ax3.scatter(radius[0,], mass_out[0,], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax3.scatter(radius[1,], mass_out[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax3.scatter(radius[2,], mass_out[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax3.scatter(radius[3,], mass_out[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax3.scatter(radius[4,], mass_out[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)
    ax3.set_title(model_type + '$x10^{9}$')

    Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
    fig3.savefig(graphs_path + plots_version_folder + 'massout_radius_' + type_name + str(model_type) + '.png',
                 bbox_inches='tight')
    plt.close(fig3)


