# number of parameter combinations to use for the run
from input_parameters.program_units import unit_year, unit_kpc

ITERATIONS_NUM = 5
TIMESTEPS_NUMB = 30000

DT_MIN = 1 / unit_year  # ;1 year
DT_MAX = 15000. * DT_MIN  # ;15000 years
T_MAX = 1.5e8 / unit_year  # ;time until the end of simulation, in years
R_MAX = 200. / unit_kpc  # ;stop the simulation once the c.d. reaches this radius_

RADIATIVE_EFFICIENCY_ETA = 0.1  # ;radiative efficiency
GAMMA = 5./3. #;adiabatic index of the outflowing material

TIME_MAX = 1.5e9/unit_year            #;time until the end of simulation, in years
RADIUS_MAX = 200./unit_kpc             #;stop the simulation once the c.d. reaches this radius
