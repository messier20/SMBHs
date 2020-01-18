import pandas
from model_program.input_parameters.galaxy_parameters import bulge_disc_totalmass_fractions
from model_program.input_parameters.initial_values import model_type, version
from plotting_program.plots.plotting_r_relation import plotting_r_relation
from plotting_program.plots.plotting_time_relation import plotting_time_relation

outputs_path = "C:/Users/Monika/PycharmProjects/SMBHs/model_program/results/output_values/"
values_version_folder = 'v' + str(version) + '/'
params_output_name = values_version_folder +'fbt_v2'

all_time_arr = []

for out_index in range(len(bulge_disc_totalmass_fractions)):
    out_index_str = str(out_index)
    # time_header = ['t1_' + out_index_str, 't2_' + out_index_str, 't3_' + out_index_str, 't4_' + out_index_str, 't5_' + out_index_str]
    time_arr = pandas.read_csv(outputs_path + params_output_name + 'time' + model_type[out_index] + '.csv', header=None)
    radius_arr = pandas.read_csv(outputs_path + params_output_name + 'radius' + model_type[out_index] + '.csv',header=None, index_col=False)
    dot_radius_arr = pandas.read_csv(outputs_path + params_output_name + 'dot_Radius' + model_type[out_index] + '.csv',header=None, index_col=False)
    dot_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'dot_mass' + model_type[out_index] + '.csv',header=None, index_col=False)
    tot_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'tot_mass' + model_type[out_index] + '.csv',header=None, index_col=False)
    out_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'out_mass' + model_type[out_index] + '.csv',header=None, index_col=False)

    # plotting_time_relation(time_arr.values, radius_arr.values, out_mass_arr.values, dot_mass_arr.values, model_type[out_index])
    plotting_r_relation(radius_arr.values, dot_radius_arr.values, out_mass_arr.values, dot_mass_arr.values, model_type[out_index])