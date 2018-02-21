#
# title           :stampi.py
# description     :
# author          :David Cuesta
# company         :Grumpy Cat Software
# date            :
# usage           :
# python_version  :3.6
# ==============================================================================
########################################################################################################################
# IMPORT
########################################################################################################################

import ctypes
import numpy as np
import os
import tsa
########################################################################################################################

def stampi(first_time_series_list, new_double_point, old_profile_list, old_index_list, subsequence_length):
    """
    :param first_time_series_list:
    :param new_double_point:
    :param old_profile_list:
    :param old_index_list:
    :param subsequence_length:
    :return:
    """
    first_time_series_double_array = (ctypes.c_double * len(first_time_series_list))(*first_time_series_list)

    list_of_one_point = [new_double_point]

    c_doubles_array_of_one_point = (ctypes.c_double * 1)(*list_of_one_point)

    initialised_zero_matrix_profile = np.zeros(len(first_time_series_list) + 1 - 20)

    c_subsequence_lenght = ctypes.c_int(len(first_time_series_list))

    c_tsa_library = ctypes.CDLL(os.path.join(tsa.tsa_libraries.__path__[0], 'libmylib-cpu.dylib'))

    initialized_c_mp_array = (ctypes.c_double * (len(first_time_series_list) + 1 - 20))\
        (*initialised_zero_matrix_profile)

    initialized_c_ip_array = (ctypes.c_int * (int(len(first_time_series_list)) + 1 - int(20)))\
        (*initialised_zero_matrix_profile.astype(int))

    c_tsa_library.stampi(first_time_series_double_array, c_doubles_array_of_one_point,
                         (ctypes.c_int * len(old_index_list))(*old_index_list),
                         (ctypes.c_double * len(old_profile_list))(*old_profile_list),
                         subsequence_length, c_subsequence_lenght, initialized_c_mp_array, initialized_c_ip_array)

    np_array_mp = np.array(initialized_c_mp_array)
    np_array_ip = np.array(initialized_c_ip_array).astype(int)

    return {'matrix_profile': np_array_mp, 'index_profile': np_array_ip}