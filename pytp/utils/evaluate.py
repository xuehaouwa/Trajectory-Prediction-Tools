# File name: evaluate.py
# Authors: Hao Xue, Du Huynh
# Date created: 18/04/2018
# Last modified: 26/06/2019
#
# Copyright Department of Computer Science and Software Engineering
# The University of Western Australia

import numpy as np


def get_ade(predicted, ground_truth):
    """
    calculate the ADE on predicted trajectories
    :param predicted: the predicted trajectories, in form of
           [num_trajectories, predicted_length, 2]
    :param ground_truth: ground truth label of predicted trajectories,
           in form of [num_trajectories, predicted_length, 2]

    :return: average ADE
    """

    mean_ADE = np.mean(np.sqrt(np.sum((predicted-ground_truth)**2, axis=-1)))
    return mean_ADE


def get_fde(predicted, ground_truth):
    """
    calculate the FDE on predicted trajectories
    :param predicted: predicted trajectories, in form of
          [num_trajectories, predicted_length, 2]
    :param ground_truth: ground truth label of predicted trajectories,
          in form of [num_trajectories, predicted_length, 2]
    :return: average FDE
    """

    mean_FDE = np.mean(np.sqrt(
            np.sum((predicted[:, -1, :]-ground_truth[:, -1, :])**2, axis=-1)))

    return mean_FDE

