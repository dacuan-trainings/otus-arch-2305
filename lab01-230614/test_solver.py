import pytest
import gr_globals
from Solver import Solver

@pytest.fixture()
def solver(): 
    return Solver()

# Step 3. No roots test
def test_no_roots(solver):
    res = solver.sqrSolve(1, 0, 1)
    assert 0 == len(res)

# Step 5. Two roots test
def test_two_roots(solver):
    res = solver.sqrSolve(1, 0, -1)

    assert 2 == len(res)
    assert -1 == pytest.approx(res[0])
    assert 1 == pytest.approx(res[1])

# Step 7. Double-the-same roots test
def test_double_roots(solver):
    res = solver.sqrSolve(1, 2, 1)

    assert 1 == len(res)
    assert -1 == pytest.approx(res[0])

# Step 9. Zero "a" test
def test_zero_a(solver):
    with pytest.raises(Exception):
        solver.sqrSolve(0, 1, 1)

# Step 11. Double-the-same roots with almost zero D
def test_almost_zero_d(solver):
    res = solver.sqrSolve(1, 2, 0.99875)

    assert 1 == len(res)
    assert -1.035355339059327 == pytest.approx(res[0])

# Step 13. Non-double args
def test_string_a(solver):
    with pytest.raises(Exception):
        solver.sqrSolve('1', 1, 1)   

def test_array_a(solver):
    with pytest.raises(Exception):
        solver.sqrSolve([1], 1, 1)   

def test_string_b(solver):
    with pytest.raises(Exception):
        solver.sqrSolve(1, '1', 1)   

def test_array_b(solver):
    with pytest.raises(Exception):
        solver.sqrSolve(1, [1], 1)   

def test_string_c(solver):
    with pytest.raises(Exception):
        solver.sqrSolve(1, 1, '1')   

def test_array_c(solver):
    with pytest.raises(Exception):
        solver.sqrSolve(1, 1, [1])   
