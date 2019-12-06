from plots.PlotSetup import PlotSetup
import numpy as np
import matplotlib.pyplot as plt


def plotting_histogram(dot_radius_arr, dot_mass_arr, time_arr):
    path = '/home/monika/Documents/SMBHs/plots/'

    a = np.where(np.array(dot_radius_arr)>0, dot_radius_arr, float('nan'))
    a = np.where(np.array(a)<1000, a, float('nan'))

    Plot = PlotSetup()
    fig1, ax1 = Plot.setup_common_properties()
    ax1.set_xlim(0, 1000)
    ax1.set_ylabel('count')
    ax1.set_xlabel('velocity [$km/s$]')
    p1 = ax1.hist(a[0,], bins=100, color='black', alpha=0.5)
    p2 = ax1.hist(a[1,], bins=100, color='b', alpha=0.5)
    p3 = ax1.hist(a[2,], bins=100, color='g', alpha=0.5)
    p4 = ax1.hist(a[3,], bins=100, color='r', alpha=0.5)
    p5 = ax1.hist(a[4,], bins=100, color='yellow', alpha=0.5)

    fig1.savefig(path + 'hist_v2.png', bbox_inches='tight')
    plt.close(fig1)

    a = np.where(np.array(a) < 360, a, float('nan'))
    fig2, ax2 = Plot.setup_common_properties()
    ax2.set_xlim(0, 360)
    ax2.set_ylabel('count')
    ax2.set_xlabel('velocity [$km/s$]')
    p5 = ax2.hist(a[4,], bins=100, color='yellow', alpha=0.5,linestyle='dashed')
    p4 = ax2.hist(a[3,], bins=100, color='r', alpha=0.5,linestyle='dashed')
    p3 = ax2.hist(a[2,], bins=100, color='g', alpha=0.5,linestyle='dashed')
    p2 = ax2.hist(a[1,], bins=100, color='b', alpha=0.5,linestyle='dashed')
    p1 = ax2.hist(a[0,], bins=100, color='black', alpha=0.5, linestyle='dashed')

    # TODO figure wjy same legend doesn't work
    # ax1.legend(( p1, p2, p3, p4, p5), (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'))
    fig2.savefig(path + 'hist_zoomed_v1.png', bbox_inches='tight')
    plt.close(fig2)

    fig2, ax2 = Plot.setup_common_properties()
    # ax2.set_ylabel('velocity [$km/s$]')
    # ax2.set_xlabel('$time yr$ ')
    # ax2.scatter(time_arr[0,], dot_radius_arr[0,], marker='.', linewidth=0.3, s=0.3)
    # plt.show()
