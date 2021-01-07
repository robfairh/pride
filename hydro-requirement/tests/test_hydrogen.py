import pytest
import numpy as np
from hydrogen import efficiency

# ===================================================================
# Tests for efficiency()
# ===================================================================


def test_efficiency_internal():
    """ Tests if the function function works correctly for an internal point
        (temperature = 50 C) """

    exp = 0.04842
    obs = efficiency(50)
    assert np.abs(exp - obs) < 1e-3


def test_efficiency_edge():
    """ Tests if the function function works correctly for an edge case
        (temperature = -273 C) """

    with pytest.raises(Exception):
        assert efficiency(-273)


# ===================================================================
# Tests for delta_H()
# ===================================================================


def test_delta_H_internal():
    """ Tests if the function function works correctly for an internal point
        (temperature = 50 C)
    """

def test_delta_H_internal():
    """ Tests if the function function works correctly for an edge case
        (Tout < Tin)
    """
    
