import pandas
from model_program.input_parameters.galaxy_parameters import bulge_disc_totalmass_fractions, bulge_scales, \
    bulge_disc_gas_fractions
from model_program.input_parameters.initial_values import model_type, version
from plotting_program.plots.plotting_mbulge_relation import plotting_mbulge_relation
from plotting_program.plots.plotting_r_relation import plotting_r_relation
from plotting_program.plots.plotting_time_relation import plotting_time_relation
import numpy as np
outputs_path = "C:/Users/Monika/PycharmProjects/SMBHs/model_program/results/output_values/"
values_version_folder = 'v' + str(version) + '/'
params_output_name = values_version_folder +'fbt_v2'

all_time_arr = []
time_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
radius_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_radius_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_bulge_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
# dot_mass_one_point_arr = [0 for x in range(len(bulge_disc_totalmass_fractions))]
dot_mass_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
dot_radius_one_point_arr = [[0 for i in range(len(bulge_disc_totalmass_fractions))] for j in range(len(bulge_disc_gas_fractions))]
# print(dot_mass_one_point_arr)

for out_index in range(len(bulge_disc_totalmass_fractions)):
    out_index_str = str(out_index)
    # time_header = ['t1_' + out_index_str, 't2_' + out_index_str, 't3_' + out_index_str, 't4_' + out_index_str, 't5_' + out_index_str]
    time_arr[out_index] = pandas.read_csv(outputs_path + params_output_name + 'time' + model_type[out_index] + '.csv', header=None)
    radius_arr[out_index] = pandas.read_csv(outputs_path + params_output_name + 'radius' + model_type[out_index] + '.csv',header=None, index_col=False)
    dot_radius_arr[out_index] = pandas.read_csv(outputs_path + params_output_name + 'dot_Radius' + model_type[out_index] + '.csv',header=None, index_col=False)
    dot_mass_arr[out_index] = pandas.read_csv(outputs_path + params_output_name + 'dot_mass' + model_type[out_index] + '.csv',header=None, index_col=False)
    # tot_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'tot_mass' + model_type[out_index] + '.csv',header=None, index_col=False)
    # out_mass_arr = pandas.read_csv(outputs_path + params_output_name + 'out_mass' + model_type[out_index] + '.csv',header=None, index_col=False)

    # plotting_time_relation(time_arr[out_index], radius_arr[out_index], dot_mass_arr[out_index], model_type[out_index])
    # plotting_r_relation(radius_arr[out_index], dot_radius_arr[out_index], dot_mass_arr[out_index], model_type[out_index])
    radius_in_bulge_1d = radius_arr[out_index].values
    dot_mass_in_bulge_1d = dot_mass_arr[out_index].values
    dot_radius_in_bulge_1d = dot_radius_arr[out_index].values
    # print(radius_in_bulge)
    dot_mass_bulge_arr[out_index] = np.where(radius_in_bulge_1d < bulge_scales[out_index], dot_mass_in_bulge_1d , np.nan)

    # dot_mass_one_point_arr[out_index] =
    # plotting_r_relation(radius_arr[out_index], dot_radius_arr[out_index], dot_mass_bulge_arr[out_index],
    #                     model_type[out_index], '-mass-bulge')

    # temp_dot_mass = np.where(radius_in_bulge_1d < bulge_scales[out_index], dot_mass_in_bulge_1d, np.nan)
    temp_dot_mass = np.where(radius_in_bulge_1d < bulge_scales[out_index], dot_mass_in_bulge_1d, 0)
    temp_dot_mass = temp_dot_mass.transpose()
    # print(max(temp[:, 0]))
    for index, item in enumerate(temp_dot_mass[:, ]):
        count = 0
        for i in item:
            if i > 0:
                count = count + 1
        dot_mass_one_point_arr[index][out_index] = np.nansum(item)/count
        # dot_mass_one_point_arr[index][out_index] = max(item)

    temp_velocity = np.where(radius_in_bulge_1d < bulge_scales[out_index], dot_radius_in_bulge_1d, 0)
    # temp_velocity = np.where(radius_in_bulge_1d < bulge_scales[out_index], dot_radius_in_bulge_1d, np.nan)
    temp_velocity = temp_velocity.transpose()
    for index, item in enumerate(temp_velocity[:, ]):
        count = 0
        for i in item:
            if i > 0:
                count = count + 1
        dot_radius_one_point_arr[index][out_index] = np.nansum(item)/count
        # dot_radius_one_point_arr[index][out_index] = max(item)

plotting_mbulge_relation(dot_mass_one_point_arr, dot_radius_one_point_arr, 'average')
# plotting_mbulge_relation(dot_mass_one_point_arr, dot_radius_one_point_arr, 'max')