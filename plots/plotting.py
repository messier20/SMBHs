import matplotlib.pyplot as plt
import numpy as np

from plots.PlotSetup import PlotSetup


def plotting(time, radius, mass_out, dot_mass):
    path = '/home/monika/Documents/SMBHs/plots/'
    Plot = PlotSetup()
    fig1, ax1 = Plot.setup()
    ax1.set_ylim(1.e-2, 1.e2)
    ax1.set_ylabel('radius [$kpc$]')
    p1 = ax1.scatter(time[0, ], radius[0, ], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax1.scatter(time[1, ], radius[1, ], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax1.scatter(time[2,], radius[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax1.scatter(time[3,], radius[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax1.scatter(time[4,], radius[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)
    #
    ax1.legend((p1, p2, p3, p4, p5), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'), markerscale=10)
    fig1.savefig(path + 'plot_threepart1.png', bbox_inches='tight')
    plt.close(fig1)

    fig2, ax2 = Plot.setup()
    ax2.set_ylim(1.e7, 1.e11)
    ax2.set_ylabel('Total mass in outflow [$M_{sun}$]')
    p1 = ax2.scatter(time[0, ], mass_out[0, ], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax2.scatter(time[1,], mass_out[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax2.scatter(time[2,], mass_out[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax2.scatter(time[3,], mass_out[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax2.scatter(time[4,], mass_out[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)

    ax2.legend((p1, p2, p3, p4, p5), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
               markerscale=10)
    fig2.savefig(path + 'plot_threepart2.png', bbox_inches='tight')
    plt.close(fig2)

    fig3, ax3 = Plot.setup()
    ax3.set_ylim(10, 1.e4)
    ax3.set_ylabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    p1 = ax3.scatter(time[0,], dot_mass[0,], color='black', marker='.', linewidth=0.3, s=0.3)
    p2 = ax3.scatter(time[1,], dot_mass[1,], color='b', marker='.', linewidth=0.3, s=0.3)
    p3 = ax3.scatter(time[2,], dot_mass[2,], color='g', marker='.', linewidth=0.3, s=0.3)
    p4 = ax3.scatter(time[3,], dot_mass[3,], color='r', marker='.', linewidth=0.3, s=0.3)
    p5 = ax3.scatter(time[4,], dot_mass[4,], color='yellow', marker='.', linewidth=0.3, s=0.3)

    ax3.legend((p1, p2, p3, p4, p5), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
               markerscale=10)
    fig3.savefig(path + 'plot_threepart3.png', bbox_inches='tight')
    plt.close(fig3)


