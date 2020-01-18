import matplotlib.pyplot as plt

from plotting_program.plots.PlotSetup import PlotSetup
from plotting_program.plots.plots_settings import *

def plotting_r_relation(radius, dot_radius, dot_mass, model_type, additional_string):
    # graphs_path = '/home/monika/Documents/SMBHs/plots/'
    Plot = PlotSetup()

    radius = radius.values
    dot_radius = dot_radius.values
    dot_mass = dot_mass

    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'orange']

# ?    p1, p2, p3, p4, p5, p6 = np.nan

    # fig1, ax1 = Plot.setup_common_properties()
    # ax1.set_ylim(1.e2, 1.e4)
    # ax1.set_xlim((3.e-2, 6.e1))
    # ax1.set_ylabel('velocity [$km/s$]')
    # ax1.set_xlabel('radius [$kpc$]')
    # ax1.set_yscale('log')
    # ax1.set_xscale('log')
    # p1 = ax1.plot(radius[:, 0], dot_radius[:, 0], color=colors[0], label=labels[0])
    # p2 = ax1.plot(radius[:, 1], dot_radius[:, 1], color=colors[1], label=labels[1])
    # p3 = ax1.plot(radius[:, 2], dot_radius[:, 2], color=colors[2], label=labels[2])
    # p4 = ax1.plot(radius[:, 3], dot_radius[:, 3], color=colors[3], label=labels[3])
    # p5 = ax1.plot(radius[:, 4], dot_radius[:, 4], color=colors[4], label=labels[4])
    # ax1.set_title(model_type + '$x10^{9}$')
    #
    # # Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
    # ax1.legend()
    # fig1.savefig(graphs_path + plots_version_folder + 'vel-radius-' + str(model_type) + '.png', bbox_inches='tight')
    # plt.close(fig1)

    fig2, ax2 = Plot.setup_common_properties()
    ax2.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    ax2.set_xlabel('radius [$kpc$]')
    # ax2.set_yscale('log')
    # ax2.set_xscale('log')
    # ax1.set_xlim((1.e-3, 1.e2))
    ax2.set_ylim(1.e-1, 12000)

    p1 = ax2.plot(radius[:, 0], dot_mass[:, 0], color=colors[0], label=labels[0])
    p2 = ax2.plot(radius[:, 1], dot_mass[:, 1], color=colors[1], label=labels[1])
    p3 = ax2.plot(radius[:, 2], dot_mass[:, 2], color=colors[2], label=labels[2])
    p4 = ax2.plot(radius[:, 3], dot_mass[:, 3], color=colors[3], label=labels[3])
    p5 = ax2.plot(radius[:, 4], dot_mass[:, 4], color=colors[4], label=labels[4])
    ax2.set_title(model_type + '$x10^{9}$')

    # Plot.add_legend_gas_fractions(ax2, p1, p2, p3, p4, p5)
    ax2.legend()
    fig2.savefig(graphs_path + plots_version_folder + 'dotmass-radius' + str(model_type) + additional_string + '.png',
                 bbox_inches='tight')
    plt.close(fig2)
    #
    # fig3, ax3 = Plot.setup_common_properties()
    # ax3.set_ylabel('Mass outflow [$M_{sun}}$]')
    # ax3.set_xlabel('radius [$kpc$]')
    #
    # ax3.set_yscale('log')
    # ax3.set_ylim(1.e8, 1.e13)
    # # ax3.set_xscale('log')
    # # ax1.set_xlim((1.e-3, 1.e2))
    # p1 = ax3.scatter(radius[0,], mass_out[0,], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    # p2 = ax3.scatter(radius[1,], mass_out[1,], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    # p3 = ax3.scatter(radius[2,], mass_out[2,], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    # p4 = ax3.scatter(radius[3,], mass_out[3,], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    # p5 = ax3.scatter(radius[4,], mass_out[4,], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    # ax3.set_title(model_type + '$x10^{9}$')
    #
    # Plot.add_legend_gas_fractions(ax3, p1, p2, p3, p4, p5)
    # fig3.savefig(graphs_path + plots_version_folder + 'massout_radius_' + type_name + str(model_type) + '.png',
    #              bbox_inches='tight')
    # plt.close(fig3)


