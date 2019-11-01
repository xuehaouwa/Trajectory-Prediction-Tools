# File name: normalize.py
# Authors: Hao Xue, Du Huynh
# Date created: 26/06/2019
# Last modified: 01/07/2019
#
# This file contains codes for normalizing the scene or image space
# to a workable space (where we don't have numbers that are too large
# and that may cause gradient explosion problems) for the deep learning
# algorithm.
#
# Copyright Department of Computer Science and Software Engineering
# The University of Western Australia

import numpy as np
from copy import deepcopy


class Normalization:

    @staticmethod
    def normalize(trajectories, shift_x=None, shift_y=None, scale=None):
        """
        This is the forward transformation function which transforms the
        trajectories to a square region around the origin such as
        [-1,-1] - [1,1] while the original trajectories could be in
        pixel unit or in metres. The transformation would be applied
        to the trajectories as follows:
          new_trajectories = (old_trajectories - shift) / scale

        :param trajectories: must be a 3D Python array of the form
               Ntrajectories x Ntime_step x 2D_x_y
        :param shift_x, shift_y: the amount of desired translation.
               If not given, the centroid of trajectory points
               would be used.
        :param scale: the desirable scale factor. If not given, the scale
              would be computed so that the trajectory points fall inside
              the [-1,-1] to [1,1] region.

        :return new_trajectories: the new trajectories after the
                transformation.
        :return shift_x, shift_y, scale: if these arguments were not
                supplied, then the function computes and returns them.

        The function assumes that either all the optional parameters
        are given or they are all not given.
        """
        if shift_x is not None:
            shift = np.array([shift_x, shift_y]).reshape(1, 2)
            new_trajectories = deepcopy((trajectories - shift) / scale)
            return new_trajectories
        else:
            shift = np.mean(trajectories, axis=-1).reshape(1, 2)
            new_trajectories = deepcopy(trajectories - shift)
            minxy = np.min(new_trajectories, axis=-1)
            maxxy = np.max(new_trajectories, axis=-1)
            scale = np.max(maxxy - minxy) / 2.0
            new_trajectories /= scale
            return new_trajectories, shift[0], shift[1], scale

    # ------------------------------------------------------------------

    @staticmethod
    def unnormalize(trajectories, shift_x, shift_y, scale):
        """
        This function does the inverse transformation to bring the trajectories
        back to their original coordinate system (in pixels or in metres).

        :param trajectories: must be a 3D Python array of the form
               Ntrajectories x Ntime_step x 2D_x_y
        :param shift_x, shift_y, scale: these should be the same
               parameters as the function 'normalise' above.

        :return new_trajectories: the new trajectories after the
                transformation.
        """
        shift = np.array([shift_x, shift_y])
        new_trajectories = deepcopy((trajectories * scale) + shift)
        return new_trajectories

    # ------------------------------------------------------------------

    @staticmethod
    def nabs_process(obs, pred):
        """
        This function performs a origin shift operation by translating
        obs and pred so that the end-point of each trajectory in the obs
        variable is at the origin. This operation has been reported
        to improve the trajectory prediction result in the SR-LSTM paper.
        Note that this function should be applied only to the trajectories
        in the test set.

        :param obs: The observed part of the trajectories. Must be an
               Ntrajectories x Nobs_time_step x 2 numpy array.
        :param pred: The predicted part of the trajectories. Must be an
               Ntrajectories x Npred_time_step x 2 numpy array.
        :return obs_data, pred_data: the new trajectories of the same
                size.
        """

        last_obs_pts = obs[:, -1, :].reshape(-1, 1, 2)
        obs_data = obs - last_obs_pts
        pred_data = pred - last_obs_pts

        return obs_data, pred_data
