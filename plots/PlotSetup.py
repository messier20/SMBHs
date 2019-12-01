import matplotlib.pyplot as plt
class PlotSetup:
    def __init__(self):
        pass

    def setup(self):
        fig, ax = plt.subplots()
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)

        ax.set_xlim(1e4, 1e8)
        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.set_xlabel('time [$yr$]')

        return fig, ax
