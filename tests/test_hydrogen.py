import numpy as np
import sys

sys.path.append("../hydro-requirement")
import hydrogen as h2


def test_efficiency_internal():
    """ Tests if the function function works correctly for an internal point
        (temperature = 50 C) """

    exp = 0.04842
    obs = h2.efficiency(50)
    assert np.abs(exp - obs) < 1e-3
