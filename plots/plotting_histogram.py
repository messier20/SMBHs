from plots.PlotSetup import PlotSetup
import numpy as np
import matplotlib.pyplot as plt
from plots.plots_settings import *

def plotting_histogram(dot_radius_arr, dot_mass_arr, time_arr, index):
    # graphs_path = '/home/monika/Documents/SMBHs/results/graphs/'
    name = plots_version_folder + 'nongrow_quasar_alltime_fbtVar_'

    a = np.where(np.array(dot_radius_arr)>0, dot_radius_arr, float('nan'))
    a = np.where(np.array(a)<1000, a, float('nan'))

    dot_mass_nozero = np.where(np.array(dot_mass_arr) > 6, dot_mass_arr, float('nan'))
    dot_mass_nozero = np.where(np.array(dot_mass_nozero) < 3500, dot_mass_nozero, float('nan'))
    print(min(dot_mass_nozero[4,]))
    print(min(dot_mass_nozero[0,]))

    Plot = PlotSetup()

    fig1, ax1 = Plot.setup_common_properties()
    ax1.set_xlim(0, 1000)
    ax1.set_ylabel('count')
    ax1.set_xlabel('velocity [$km/s$]')
    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'yellow']
    ax1.hist([a[0,], a[1,], a[2,], a[3,], a[4,]], bins=600, histtype='stepfilled', color=colors, alpha=0.5, label=labels)

    # p1 = ax1.hist(a[0,], bins=100, color='black', alpha=0.5, label=r'$f_g$ = 0.05')
    # p2 = ax1.hist(a[1,], bins=100, color='b', alpha=0.5, label=r'$f_g$ = 0.1')
    # p3 = ax1.hist(a[2,], bins=100, color='g', alpha=0.5, label=r'$f_g$ = 0.25')
    # p4 = ax1.hist(a[3,], bins=100, color='r', alpha=0.5, label=r'$f_g$ = 1')
    # p5 = ax1.hist(a[4,], bins=100, color='yellow', alpha=0.5)
    # ax1.legend(ax1)

    fig1.savefig(graphs_path+ name + 'hist_v2'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig1)

    b = np.where(np.array(a) < 360, a, float('nan'))
    fig2, ax2 = Plot.setup_common_properties()
    ax2.set_xlim(0, 360)
    ax2.set_ylabel('count')
    ax2.set_xlabel('velocity [$km/s$]')
    ax2.hist([b[0,], b[1,], b[2,], b[3,], b[4,]], bins=600, histtype='stepfilled', color=colors, alpha=0.5,
             label=labels)
    ax2.legend(prop={'size': 10})
    fig2.savefig(graphs_path + name + 'hist_zoomed_v1'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig2)

    fig3, ax3 = Plot.setup_common_properties()
    # ax3.set_xlim(50, 360)
    ax3.set_ylabel('count')
    ax3.set_xlabel('velocity [$km/s$]')
    ax3.hist(a[0,], bins=600, histtype='stepfilled', color=colors[0], alpha=0.5, label=labels[0])
    ax3.legend(prop={'size': 10})
    fig3.savefig(graphs_path + name + 'hist_vel_fg05'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig3)

    fig4, ax4 = Plot.setup_common_properties()
    # ax4.set_xlim(50, 360)
    ax4.set_ylabel('count')
    ax4.set_xlabel('velocity [$km/s$]')
    ax4.hist(a[1,], bins=600, histtype='stepfilled', color=colors[1], alpha=0.5, label=labels[1])
    ax4.legend(prop={'size': 10})
    fig4.savefig(graphs_path + name + 'hist_vel_fg01'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig4)

    fig5, ax5 = Plot.setup_common_properties()
    # ax4.set_xlim(50, 360)
    ax5.set_ylabel('count')
    ax5.set_xlabel('velocity [$km/s$]')
    ax5.hist(a[2,], bins=600, histtype='stepfilled', color=colors[2], alpha=0.5, label=labels[2])
    ax5.legend(prop={'size': 10})
    fig5.savefig(graphs_path + name + 'hist_vel_fg025'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig5)

    fig6, ax6 = Plot.setup_common_properties()
    # ax4.set_xlim(50, 360)
    ax6.set_ylabel('count')
    ax6.set_xlabel('velocity [$km/s$]')
    ax6.hist(a[3,], bins=600, histtype='stepfilled', color=colors[3], alpha=0.5, label=labels[3])
    ax6.legend(prop={'size': 10})
    fig6.savefig(graphs_path + name + 'hist_vel_fg05'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig6)

    fig7, ax7 = Plot.setup_common_properties()
    # ax4.set_xlim(50, 360)
    ax7.set_ylabel('count')
    ax7.set_xlabel('velocity [$km/s$]')
    ax7.hist(a[4,], bins=600, histtype='stepfilled', color=colors[4], alpha=0.5, label=labels[4])
    ax7.legend(prop={'size': 10})
    fig7.savefig(graphs_path + name + 'hist_vel_fg1'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig7)


    fig1, ax1 = Plot.setup_common_properties()
    # ax1.set_xlim(1, 20)
    ax1.set_ylabel('count')
    ax1.set_xlabel('Mass outflow rate [$M_{sun}yr^{-1}$]')
    labels = [r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1']
    colors = ['black', 'b', 'g', 'r', 'yellow']
    ax1.hist([dot_mass_nozero[0,], dot_mass_nozero[1,], dot_mass_nozero[2,], dot_mass_nozero[3,], dot_mass_nozero[4,]], bins=800, histtype='stepfilled', color=colors, alpha=0.5,
             label=labels)

    fig1.savefig(graphs_path + name + 'hist_dmass_more_than6_less3500'+str(index)+'.png', bbox_inches='tight')
    plt.close(fig1)
