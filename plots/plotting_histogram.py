from plots.PlotSetup import PlotSetup
import matplotlib.pyplot as plt


def plotting_histogram(dot_radius_arr, dot_mass_arr):
    Plot = PlotSetup()
    fig1, ax1 = Plot.setup_common_properties()
    ax1.hist(dot_radius_arr, bins=[0, 500, 1000, 1500, 2000, 2500, 3000])
    plt.show()