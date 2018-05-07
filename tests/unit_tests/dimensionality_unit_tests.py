# Copyright (c) 2018 Grumpy Cat Software S.L.
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


########################################################################################################################
# IMPORT
########################################################################################################################
import unittest
from tsa.dimensionality import *
from tsa.array import array
import numpy as np


########################################################################################################################


class DimensionalityTest(unittest.TestCase):
    DELTA = 1e-6
    DECIMAL = 6

    def setUp(self):
        pass

    def test_ramer_douglas_peucker(self):
        a = array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0.1, -0.1, 5.0, 6.0, 7.0, 8.1, 9.0, 9.0, 9.0]])
        ramer_douglas_peucker_result = ramer_douglas_peucker(a, 1.0).to_numpy()
        expected = np.array([[0, 2, 3, 6, 9], [0, -0.1, 5.0, 8.1, 9.0]])
        np.testing.assert_array_almost_equal(ramer_douglas_peucker_result, expected, decimal=self.DECIMAL)

    def test_visvalingam(self):
        a = array([[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0.1, -0.1, 5.0, 6.0, 7.0, 8.1, 9.0, 9.0, 9.0]])
        visvalingam_result = visvalingam(a, 5).to_numpy()
        expected = np.array([[0, 2, 5, 7, 9], [0, -0.1, 7.0, 9.0, 9.0]])
        np.testing.assert_array_almost_equal(visvalingam_result, expected, decimal=self.DECIMAL)

    def test_paa(self):
        a = array(
            [[0.0, 0.1, -0.1, 5.0, 6.0, 7.0, 8.1, 9.0, 9.0, 9.0], [0.0, 0.1, -0.1, 5.0, 6.0, 7.0, 8.1, 9.0, 9.0, 9.0]])
        paa_result = paa(a, 5).to_numpy()
        expected = np.array([[0.05, 2.45, 6.5, 8.55, 9.0], [0.05, 2.45, 6.5, 8.55, 9.0]])
        np.testing.assert_array_almost_equal(paa_result, expected, decimal=self.DECIMAL)

    def test_sax(self):
        a = array([[0.05, 2.45, 6.5, 8.55, 9.0], [0.05, 2.45, 6.5, 8.55, 9.0]])
        sax_result = sax(a, 3).to_numpy()

        expected = np.array([[0, 0, 1, 2, 2], [0, 0, 1, 2, 2]], dtype=np.int32)
        np.testing.assert_array_almost_equal(sax_result, expected, decimal=self.DECIMAL)

    def test_pip(self):
        a = array(
            [[0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0], [0.0, 0.1, -0.1, 5.0, 6.0, 7.0, 8.1, 9.0, 9.0, 9.0]])
        pip_result = pip(a, 6).to_numpy()

        expected = np.array([[0.0, 2.0, 4.0, 5.0, 6.0, 9.0], [0.0, -0.1, 6.0, 7.0, 8.1, 9.0]])
        np.testing.assert_array_almost_equal(pip_result, expected, decimal=self.DECIMAL)

    if __name__ == '__main__':
        unittest.main()