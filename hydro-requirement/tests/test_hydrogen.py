import pytest
import numpy as np
import hydrogen as h2

# ===================================================================
# Tests for efficiency()
# ===================================================================


def test_efficiency_internal():
    """ Tests if the function works correctly for an internal point
        (temperature = 50 C) """

    exp = 0.04842
    obs = h2.efficiency(50)
    assert np.abs(exp - obs) < 1e-3


def test_efficiency_edge():
    """ Tests if the function works correctly for an edge case
        (temperature = -273 C) """

    with pytest.raises(Exception):
        assert h2.efficiency(-273)


# ===================================================================
# Tests for delta_H()
# ===================================================================


def test_delta_H_internal():
    """ Tests if the function works correctly for an internal point
        (Tout = 200 and Tin = 100 C)
    """
    exp = 7.7706
    obs = h2.delta_H(200, 100)
    assert np.abs(exp - obs) < 1e-3


def test_delta_H_edge1():
    """ Tests if the function works correctly for an edge case
        (Tout < Tin)
    """
    Tout = 300
    Tin = 400
    with pytest.raises(Exception):
        assert h2.delta_H(Tout, Tin)


def test_delta_H_edge2():
    """ Tests if the function works correctly for an edge case
        (Tin < 25 and Tout = 200)
    """
    Tout = 200
    Tin = 20
    with pytest.raises(Exception):
        assert h2.delta_H(Tout, Tin)


# ===================================================================
# Tests for lte_prod_rate()
# ===================================================================


def test_lte_prod_rate_internal():
    """ Tests if the function works correctly for an internal point
        (P = 1 and eta = 0.5)
    """
    exp = 8.333
    obs, _ = h2.lte_prod_rate(1., 0.5)
    assert np.abs(exp - obs) < 1e-3


def test_lte_prod_rate_edge():
    """ Tests if the function works correctly for an edge case
        (P = 1 and eta = 0)
    """
    P = 1
    eta = 0.
    with pytest.raises(Exception):
        assert h2.lte_prod_rate(P, eta)


# ===================================================================
# Tests for hte_req()
# ===================================================================


def test_hte_req_internal():
    """ Tests if the function works correctly for an internal point
        (P = 3 MPa = 29.6 atm and Te = 200)
    """
    exp1, exp2 = 232.868, 11.132
    obs1, obs2 = h2.hte_req(29.6, 200)
    assert np.abs(exp1 - obs1) < 1e-3 and np.abs(exp2 - obs2) < 1e-3


def test_hte_req_edge1():
    """ Tests if the function works correctly for an edge case
        (P = 1 and Te < 100)
    """
    P = 1
    Te = 50
    with pytest.raises(Exception):
        assert h2.hte_req(P, Te)


def test_hte_req_edge2():
    """ Tests if the function works correctly for an edge case
        (P = 0 and Te = 200)
    """
    P = 0
    Te = 200
    with pytest.raises(Exception):
        assert h2.hte_req(P, Te)


# ===================================================================
# Tests for hte_power_req()
# ===================================================================


def test_hte_power_req_internal():
    """ Tests if the function works correctly for an internal point
        (P = 3 MPa = 29.6 atm and To = 200)
    """
    exp1, exp2 = 137.896, 0.957
    obs1, obs2 = h2.hte_power_req(29.6, 200)
    assert np.abs(exp1 - obs1) < 1e-3 and np.abs(exp2 - obs2) < 1e-3


def test_hte_power_req_edge():
    """ Tests if the function works correctly for an internal point
        (P = 0 and To = 200)
    """
    P = 0
    To = 200
    with pytest.raises(Exception):
        assert h2.hte_power_req(P, To)
