import math

import pandas
from model_program.input_parameters.galaxy_parameters import bulge_disc_totalmass_fractions, bulge_scales, \
    bulge_disc_gas_fractions
from model_program.input_parameters.initial_values import model_type, version
from plotting_program.plots.plotting_fg_relation import plotting_fg_relation
from plotting_program.plots.plotting_mbulge_relation import plotting_mbulge_relation
from plotting_program.plots.plotting_r_relation import plotting_r_relation
from plotting_program.plots.plotting_time_relation import plotting_time_relation
from plotting_program.initial_arrays import *
import numpy as np

from plotting_program.turning_plots_on_off import time_relation_on, radius_relation_on, average_dm_bm_on, dm_bm_on, \
    max_dm_bm_on, fg_relation

outputs_path = "C:/Users/Monika/PycharmProjects/SMBHs/model_program/results/output_values/"
values_version_folder = 'v' + str(version) + '/'
params_output_name = values_version_folder +'fbt_v2'


for index in range(len(bulge_disc_totalmass_fractions)):
    out_index_str = str(index)
    # time_header = ['t1_' + out_index_str, 't2_' + out_index_str, 't3_' + out_index_str, 't4_' + out_index_str, 't5_' + out_index_str]
    time_arr[index] = pandas.read_csv(outputs_path + params_output_name + 'time' + model_type[index] + '.csv', header=None)
    radius_arr[index] = pandas.read_csv(outputs_path + params_output_name + 'radius' + model_type[index] + '.csv', header=None, index_col=False)
    dot_radius_arr[index] = pandas.read_csv(outputs_path + params_output_name + 'dot_Radius' + model_type[index] + '.csv', header=None, index_col=False)
    dot_mass_arr[index] = pandas.read_csv(outputs_path + params_output_name + 'dot_mass' + model_type[index] + '.csv', header=None, index_col=False)
    # tot_mass_arr[out_index] = pandas.read_csv(outputs_path + params_output_name + 'tot_mass' + model_type[out_index] + '.csv',header=None, index_col=False)
    out_mass_arr[index] = pandas.read_csv(outputs_path + params_output_name + 'out_mass' + model_type[index] + '.csv',header=None, index_col=False)

    if time_relation_on:
        plotting_time_relation(time_arr[index], radius_arr[index], dot_mass_arr[index], out_mass_arr[index], model_type[index], index)
    if radius_relation_on:
        plotting_r_relation(radius_arr[index], dot_radius_arr[index], dot_mass_arr[index], model_type[index], index)

    if dm_bm_on or fg_relation:

        radius_in_bulge_1d = radius_arr[index].values
        dot_mass_in_bulge_1d = dot_mass_arr[index].values
        dot_radius_in_bulge_1d = dot_radius_arr[index].values

        temp_velocity = np.where(radius_in_bulge_1d < bulge_scales[index], dot_radius_in_bulge_1d, 0)
        temp_velocity = temp_velocity.transpose()

        dot_mass_bulge_arr[index] = np.where(radius_in_bulge_1d < bulge_scales[index], dot_mass_in_bulge_1d, np.nan)
        temp_dot_mass = np.where(radius_in_bulge_1d < bulge_scales[index], dot_mass_in_bulge_1d, np.nan)
        temp_dot_mass = temp_dot_mass.transpose()

        for idx, item in enumerate(temp_dot_mass[:, ]):
            count = 0
            for i in item:
                if i > 0:
                    count = count + 1
            avg_dot_mass_one_point_arr_ln[idx][index] = math.log(np.nansum(item) / count)
            avg_dot_mass_one_point_arr[idx][index] = np.nansum(item) / count

            max_dot_mass_one_point_arr_ln[idx][index] = math.log(np.nanmax(item))
            max_dot_mass_one_point_arr[idx][index] = np.nanmax(item)
            # dot_mass_one_point_arr[idx][index] = max(item)

        for idx, item in enumerate(temp_velocity[:, ]):
            count = 0
            for i in item:
                if i > 0:
                    count = count + 1
            avg_dot_radius_one_point_arr[idx][index] = np.nansum(item) / count
            avg_dot_radius_one_point_arr_ln[idx][index] = math.log(np.nansum(item) / count)

            max_dot_radius_one_point_arr_ln[idx][index] = math.log(np.nanmax(item))
            max_dot_radius_one_point_arr[idx][index] = np.nanmax(item)

if average_dm_bm_on:
    plotting_mbulge_relation(avg_dot_mass_one_point_arr, avg_dot_radius_one_point_arr, avg_dot_mass_one_point_arr_ln,
                         avg_dot_radius_one_point_arr_ln, 'average')

if max_dm_bm_on:
    plotting_mbulge_relation(max_dot_mass_one_point_arr, max_dot_radius_one_point_arr, max_dot_mass_one_point_arr_ln,
                         max_dot_radius_one_point_arr_ln, 'max')

if fg_relation:
    plotting_fg_relation(np.array(avg_dot_radius_one_point_arr), np.array(avg_dot_radius_one_point_arr_ln), np.array(avg_dot_mass_one_point_arr), np.array(avg_dot_mass_one_point_arr_ln))