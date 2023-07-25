import unittest
from Solver import Solver

class TestSolver(unittest.TestCase):
    # Pre-test routines
    def setUp(self):
        self.solver = Solver();


    # Step 3. No roots test
    def test_no_roots(self):
       res = self.solver.sqrSolve(1, 0, 1);
       self.assertEqual(len(res), 0);


# Executing the tests in the above test case class
if __name__ == "__main__":
  unittest.main()