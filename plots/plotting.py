import matplotlib.pyplot as plt
import numpy as np
def plotting(time, radius):
    plt.ylim(1.e-2, 1.e2)
    plt.xlim(1e4, 1e8)
    plt.plot(time[0, ], radius[0, ])
    plt.yscale('log')
    plt.xscale('log')
    plt.show()