import matplotlib.pyplot as plt
class PlotSetup:
    def __init__(self):
        pass

    def setup_time_rel(self):
        # fig, ax = plt.subplots()
        # ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
        fig, ax = self.setup_common_properties()

        ax.set_xlim(1e4, 1e8)
        ax.set_yscale('log')
        ax.set_xscale('log')
        ax.set_xlabel('time [$yr$]')

        return fig, ax
    def setup_LAGN_rel(self):
        # fig, ax = plt.subplots()
        # ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)
        fig, ax = self.setup_common_properties()

        # ax.set_xlim(3800, 4400)
        # ax.set_xlabel('time [$yr$]')

        return fig, ax

    def setup_histogram(self, model_name):
        fig, ax = self.setup_common_properties()
        ax.set_ylabel('count')
        ax.set_title(model_name + '$x10^{9}$')

        return fig, ax

    def add_legend_gas_fractions(self, ax, *lines):
        return ax.legend(lines,
                   (r'$f_g$ = 0.05', r'$f_g$ = 0.1', r'$f_g$ = 0.25', r'$f_g$ = 0.5', r'$f_g$ = 1'),
                   markerscale=7)

    def setup_common_properties(self):
        fig, ax = plt.subplots()
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True)

        return  fig, ax


