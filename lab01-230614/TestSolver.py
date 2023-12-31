import unittest
import gr_globals
from Solver import Solver

class TestSolver(unittest.TestCase):
    # Pre-test routines
    def setUp(self):
        self.solver = Solver()


    # Step 3. No roots test
    def test_no_roots(self):
        res = self.solver.sqrSolve(1, 0, 1)
        self.assertEqual(len(res), 0)

    # Step 5. Two roots test
    def test_two_roots(self):
        res = self.solver.sqrSolve(1, 0, -1)

        self.assertEqual(len(res), 2)
        self.assertAlmostEqual(res[0], -1)
        self.assertAlmostEqual(res[1], 1)

    # Step 7. Double-the-same roots test
    def test_double_roots(self):
        res = self.solver.sqrSolve(1, 2, 1)

        self.assertEqual(len(res), 1)
        self.assertAlmostEqual(res[0], -1)

    # Step 9. Zero "a" test
    def test_zero_a(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve(0, 1, 1)

    # Step 11. Double-the-same roots with almost zero D
    def test_almost_zero_d(self):
        res = self.solver.sqrSolve(1, 2, 0.99875)

        self.assertEqual(len(res), 1)
        self.assertAlmostEqual(res[0], -1.035355339059327)

    # Step 13. Non-double args
    def test_string_a(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve('1', 1, 1)   

    def test_array_a(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve([1], 1, 1)   

    def test_string_b(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve(1, '1', 1)   

    def test_array_b(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve(1, [1], 1)   

    def test_string_c(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve(1, 1, '1')   

    def test_array_c(self):
        with self.assertRaises(Exception):
            self.solver.sqrSolve(1, 1, [1])   


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()
  