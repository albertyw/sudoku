import unittest

import solve


class TestSolve(unittest.TestCase):
    def test_completed(self):
        problem = "974236158638591742125487936316754289742918563589362417867125394253649871491873625"
        solution = problem
        solved = solve.Solver(problem).search()
        solved = solved.replace("\n", "")
        self.assertEqual(solved, solution)
