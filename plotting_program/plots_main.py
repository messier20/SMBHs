import pandas
from model_program.input_parameters.galaxy_parameters import bulge_disc_totalmass_fractions
from model_program.input_parameters.initial_values import model_type, version
from plotting_program.plots.plotting_time_relation import plotting_time_relation

outputs_path = "C:/Users/Monika/PycharmProjects/SMBHs/model_program/results/output_values/"
values_version_folder = 'v' + str(version) + '/'
params_output_name = values_version_folder +'fbt_v2'

for out_index in range(len(bulge_disc_totalmass_fractions)):
    time_arr = pandas.read_csv(outputs_path + params_output_name + 'time' + model_type[out_index] + '.csv')
    radius_arr = pandas.read_csv(outputs_path + params_output_name + 'radius' + model_type[out_index] + '.csv')
    dot_radius_arr = pandas.read_csv(outputs_path + params_output_name + 'dot_Radius' + model_type[out_index] + '.csv')
    dot_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'dot_mass' + model_type[out_index] + '.csv')
    tot_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'tot_mass' + model_type[out_index] + '.csv')
    out_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'out_mass' + model_type[out_index] + '.csv')

    print(time_arr)
    print(radius_arr)
    # plotting_time_relation(time_arr, radius_arr, out_mass_arr, dot_mass_arr, model_type[out_index])