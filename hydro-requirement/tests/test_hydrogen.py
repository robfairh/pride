import pytest
import numpy as np
import hydrogen as h2

# ===================================================================
# Tests for efficiency()
# ===================================================================


def test_efficiency_internal():
    """ Tests if the function function works correctly for an internal point
        (temperature = 50 C) """

    exp = 0.04842
    obs = h2.efficiency(50)
    assert np.abs(exp - obs) < 1e-3


def test_efficiency_edge():
    """ Tests if the function function works correctly for an edge case
        (temperature = -273 C) """

    with pytest.raises(Exception):
        assert h2.efficiency(-273)


# ===================================================================
# Tests for delta_H()
# ===================================================================


def test_delta_H_internal():
    """ Tests if the function function works correctly for an internal point
        (Tout =  C)
    """
    h2.delta_H(Tout, Tin)

def test_delta_H_internal():
    """ Tests if the function function works correctly for an edge case
        (Tout < Tin)
    """

