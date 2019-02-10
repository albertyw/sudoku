import unittest

import solve


class TestSolve(unittest.TestCase):
    def test_completed(self):
        problem = "974236158638591742125487936316754289742918563589362417867125394253649871491873625"
        solution = problem
        solved = solve.Solver(problem).search()
        solved = solved.replace("\n", "")
        self.assertEqual(solved, solution)

    def test_hidden_singles(self):
        problem = "xx2x3xxx8xxxxx8xxxx31x2xxxxx6xx5x27xx1xxxxx5x2x4x6xx31xxxx8x6x5xxxxxxx13xx531x4xx"
        solution = "672435198549178362831629547368951274917243856254867931193784625486592713725316489"
        solved = solve.Solver(problem).search()
        solved = solved.replace("\n", "")
        self.assertEqual(solved, solution)
