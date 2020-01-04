from pytp.utils.evaluate import get_fde, get_ade
import numpy as np
import math
from unittest import TestCase


class UtilsTest(TestCase):
    def setUp(self):
        self.test_gt = np.zeros((10, 12, 2))
        self.pred_1 = np.zeros((10, 12, 2))
        self.pred_2 = np.ones((10, 12, 2))

    def test_get_ade(self):
        ade_1 = get_ade(self.pred_1, self.test_gt)
        ade_2 = get_ade(self.pred_2, self.test_gt)

        self.assertEqual(0, ade_1, "ADE is wrong!")
        self.assertAlmostEqual(math.sqrt(2), ade_2, 5, "ADE is wrong!")

    def tearDown(self):
        pass


