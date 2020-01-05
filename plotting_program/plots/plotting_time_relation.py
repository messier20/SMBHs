import matplotlib.pyplot as plt

from plotting_program.plots.PlotSetup import PlotSetup
from plotting_program.plots.plots_settings import *

def plotting_time_relation(time_arr, radius, mass_out, dot_mass, index, type_name):
    # graphs_path = '/home/monika/Documents/SMBHs/plots/'

    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'orange']

    Plot = PlotSetup()
    fig1, ax1 = Plot.setup_time_rel()
    ax1.set_ylim(1.e-2, 1.e2)
    ax1.set_ylabel('radius [$kpc$]')
    p1 = ax1.scatter(time_arr[:, 0], radius[:, 0], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    p2 = ax1.scatter(time_arr[:, 1], radius[:, 1], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    p3 = ax1.scatter(time_arr[:, 2], radius[:, 2], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    p4 = ax1.scatter(time_arr[:, 3], radius[:, 3], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    p5 = ax1.scatter(time_arr[:, 4], radius[:, 4], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    #
    ax1.legend((p1, p2, p3, p4, p5), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'), markerscale=10)
    fig1.savefig(graphs_path +plots_version_folder  + 'threepart1' + type_name +str(index)+'.png', bbox_inches='tight')
    plt.close(fig1)

    # fig2, ax2 = Plot.setup_time_rel()
    # ax2.set_ylim(1.e4, 1.e12)
    # ax2.set_ylabel('Total mass in outflow [$M_{sun}$]')
    # p6 = ax2.scatter(time_arr[0, ], mass_out[0, ], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    # p7 = ax2.scatter(time_arr[1,], mass_out[1,], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    # p8 = ax2.scatter(time_arr[2,], mass_out[2,], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    # p9 = ax2.scatter(time_arr[3,], mass_out[3,], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    # p10 = ax2.scatter(time_arr[4,], mass_out[4,], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    #
    # ax2.legend((p6, p7, p8, p9, p10), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
    #            markerscale=10)
    # fig2.savefig(graphs_path +plots_version_folder  + 'threepart2' + type_name +str(index)+'.png', bbox_inches='tight')
    # plt.close(fig2)
    #
    # fig3, ax3 = Plot.setup_time_rel()
    # ax3.set_ylim(1.e3, 2.e4)
    # ax3.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    # p11 = ax3.scatter(time_arr[0,], dot_mass[0,], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    # p12 = ax3.scatter(time_arr[1,], dot_mass[1,], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    # p13 = ax3.scatter(time_arr[2,], dot_mass[2,], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    # p14 = ax3.scatter(time_arr[3,], dot_mass[3,], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    # p15 = ax3.scatter(time_arr[4,], dot_mass[4,], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    #
    # ax3.legend((p11, p12, p13, p14, p15), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
    #            markerscale=10)
    # fig3.savefig(graphs_path +plots_version_folder  + 'threepart3' + type_name +str(index)+'.png', bbox_inches='tight')
    # plt.close(fig3)

    # # obs_time = radius/dot_radius
    # fig3, ax3 = Plot.setup_common_properties()
    # # ax3.set_ylim(1.e-2, 1.e8)
    # ax3.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    # ax3.set_xlabel('observed time kpc/km/s')
    # p16 = ax3.scatter(observed_time[0,], dot_mass[0,], color=colors[0], marker='.', linewidth=0.3, s=0.4)
    # p17 = ax3.scatter(observed_time[1,], dot_mass[1,], color=colors[1], marker='.', linewidth=0.3, s=0.4)
    # p18 = ax3.scatter(observed_time[2,], dot_mass[2,], color=colors[2], marker='.', linewidth=0.3, s=0.4)
    # p19 = ax3.scatter(observed_time[3,], dot_mass[3,], color=colors[3], marker='.', linewidth=0.3, s=0.4)
    # p20 = ax3.scatter(observed_time[4,], dot_mass[4,], color=colors[4], marker='.', linewidth=0.3, s=0.4)
    #
    # ax3.legend((p16, p17, p18, p19, p20), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
    #            markerscale=10)
    # fig3.savefig(graphs_path + plots_version_folder + 'obst_dotmass' + type_name + str(index) + '.png',
    #              bbox_inches='tight')
    # plt.close(fig3)


