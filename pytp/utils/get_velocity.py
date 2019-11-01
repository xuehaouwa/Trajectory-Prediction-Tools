# Authors: Hao Xue, Du Huynh
# Date created: 18/04/2018
# Last modified: 26/06/2019
#
# Copyright Department of Computer Science and Software Engineering
# The University of Western Australia

import numpy as np



def get_vel(trajs):
    """
    This function returns the velocity of the give trajectories.
    :param trajs: must be a Ntrajs x Ntime_step x 2 tensor.
    :return veltrajs: the velocity of trajs (same dimensions as trajs)
    """
    veltrajs = np.zeros(trajs.shape)
    veltrajs[:, 1:, :] = trajs[:, 1:, :] - trajs[:, 0:-1, :]
    veltrajs[:, 0, :] = veltrajs[:, 1, :]

    return veltrajs

# ------------------------------------------------------------------
def process_velocity(obs, pred):
    """
    This function compose the velocity component of each trajectory
    and append it to the observed part of the trajectory.
    :param obs: observed parts of the trajectories (must be an
                Ntrajs x Ntime_step x 2 numpy array)
    :param pred: predicted parts of the trajectories (same dimension
                 as obs)
    :return input_data: a Ntrajs x Ntime_step x 4 numpy array
                        containing the velocity components in the last
                        two elements of axis 2.
    :return output_data: same as pred
    """
    trajs = np.concatenate((obs, pred), axis=1)
    vel = get_vel(trajs)

    obs_len = obs.shape[1]
    input_data = np.concatenate((obs, vel[:, :obs_len, :]), axis=2)
    output_data = pred

    return input_data, output_data

