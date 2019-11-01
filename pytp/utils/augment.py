# File name: augment.py
# Authors: Hao Xue, Du Huynh
# Date created: 26/06/2019
# Last modified: 01/07/2019
#
# This file contains codes for augmenting the trajectories for improving
# the training of the prediction model.
#
# Copyright Department of Computer Science and Software Engineering
# The University of Western Australia

import numpy as np
import math
from copy import deepcopy


class Augmentation:

    @staticmethod
    def reverse(trajs, return_concated=False):
        """
        reverse trajectories
        :param trajs:
        :param return_concated:
        :return:
        """
        reversed_trajs = deepcopy(trajs)
        reversed_trajs = np.flip(reversed_trajs, 1)

        if return_concated:
            reversed_trajs = np.concatenate((reversed_trajs, trajs), axis=0)

        return reversed_trajs

    # ------------------------------------------------------------------

    @staticmethod
    def random_rotate(trajs, origin=None):
        """
        A random rotation angle would be generated and the 2D rotation
        of the generated angle about the origin would be applied to
        the trajectories stored in trajs. As the rotation is about
        the origin, the trajectories should have been normalized
        so that they are defined around the origin. The new rotated
        trajectories would be returned which can be concatenated
        to the original trajectories to augment the training set.
        Input parameter:
          trajs - should be Ntrajectories x Ntime_step x xy_coords
        Output parameter:
          new_trajs - the matrix storing the new, rotated trajectories.
        """
        rotated = np.zeros(trajs.shape)
        pi2 = 2 * np.pi
        if origin is None:
            orig = np.zeros((2, 1))
        else:
            orig = np.array(origin).reshape(2, 1)
        for i in range(trajs.shape[0]):
            angle = np.random.rand() * pi2
            cangle, sangle = math.cos(angle), math.sin(angle)
            rot_mat = np.array([[cangle, -sangle], [sangle, cangle]])
            rotated[i, :, :] = np.matmul(rot_mat, trajs[i, :, :].T - orig).T
        return rotated

    # ------------------------------------------------------------------

    @staticmethod
    def swap_xy(trajs):
        """
        This function returns new trajectories by swapping the x- and
        y-coordinates of the trajectories.
        """
        new_trajs = np.zeros(trajs.shape)
        new_trajs[:, :, 0] = trajs[:, :, 1]
        new_trajs[:, :, 1] = trajs[:, :, 0]
        return new_trajs

    # ------------------------------------------------------------------

    @staticmethod
    def augment_turning(trajs, p=0.5, proportion=1):
        """
        This function selectively augments trajectories that are turning (i.e.,
        very non-linear). The function inspects the distance d1 between
        the starting and ending coordinates of each trajectory and compares
        it with the distance d2 along the trajectory. If d1 < p*d2 then
        the trajectory is considered to be turning. A proportion of such
        turning trajectories can be specified for augmentation. The
        augmentation implemented below include translating the trajectory
        left, right, up, and down by 0.1.

        Input parameter:
           trajs - the input trajectories which should have already been
                   normalized.
           p - the 'threshold' value that determines whether trajectories
               are turning or not.
           proportion - the proportion of turning trajectories to be augmented.

        Output parameter:
           new_trajs - the new augmented trajectories that can be concatenated
                       to the training set.

        *** Warning: This function may take some time to run (because of
            the square root function) if there are many trajectories in
            the parameter trajs.
        """

        d1 = np.sqrt(np.sum((trajs[:, -1, :] - trajs[:, 0, :]) ** 2, axis=-1))
        d2 = np.sum(np.sqrt(np.sum((trajs[:, 1:, :] - trajs[:, 0:-1, :]) ** 2, axis=-1)), axis=1)

        rows = (d1 < p * d2)
        turning_trajs = trajs[rows, :, :]
        N = turning_trajs.shape[0]
        if proportion < 1.0:
            index = int(np.random.rand(np.round(N * proportion), 1) * N)
            turning_trajs = turning_trajs[index, :, :]

        N = turning_trajs.shape[0]
        new_trajs = np.zeros((4 * N, turning_trajs.shape[1], turning_trajs.shape[2]))
        new_trajs[0::4, :, :] = turning_trajs - np.array([[[0.1, 0.0]]])  # move left
        new_trajs[1::4, :, :] = turning_trajs + np.array([[[0.1, 0.0]]])  # move right
        new_trajs[2::4, :, :] = turning_trajs - np.array([[[0.0, 0.1]]])  # move up
        new_trajs[3::4, :, :] = turning_trajs + np.array([[[0.0, 0.1]]])  # move down

        return new_trajs
