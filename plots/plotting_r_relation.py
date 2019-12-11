import matplotlib.pyplot as plt
import numpy as np

from plots.PlotSetup import PlotSetup


def plotting_r_relation(radius, dot_radius, mass_out, dot_mass, index):
    path = '/home/monika/Documents/SMBHs/plots/'
    name = 'nongrow_quasar_alltime_fbtVar_'
    Plot = PlotSetup()

    fig1, ax1 = Plot.setup_common_properties()
    # # ax1.set_ylim(1.e-2, 1.e2)
    # # ax1.set_ylabel('radius [$kpc$]')
    # labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    # colors = ['black', 'b', 'g', 'r', 'yellow']
    # props = { 'label':labels}
    # ax1.scatter([time[0,], time[1,], time[2,], time[3,], time[4,]], [radius[0,],radius[1,], radius[2,], radius[3,], radius[4,]], color=colors)
    # plt.show()
    p1 = ax1.scatter(radius[0,], dot_radius[0,], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax1.scatter(radius[1,], dot_radius[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax1.scatter(radius[2,], dot_radius[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax1.scatter(radius[3,], dot_radius[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax1.scatter(radius[4,], dot_radius[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)

    Plot.add_legend_gas_fractions(ax1, p1, p2, p3, p4, p5)
    fig1.savefig(path + name + 'plot_radius_dot_radius_v1_'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig1)