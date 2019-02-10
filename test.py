import unittest

import solve


TEST_CASES = [
    {
        "name": "completed",
        "problem": "974236158638591742125487936316754289742918563589362417867125394253649871491873625",
        "solution": "974236158638591742125487936316754289742918563589362417867125394253649871491873625",
    },
    {
        "name": "hidden_singles",
        "problem": "xx2x3xxx8xxxxx8xxxx31x2xxxxx6xx5x27xx1xxxxx5x2x4x6xx31xxxx8x6x5xxxxxxx13xx531x4xx",
        "solution": "672435198549178362831629547368951274917243856254867931193784625486592713725316489",
    },
]


class TestSolve(unittest.TestCase):
    pass


def generate_test_func(test_case):
    def test(self):
        solved = solve.Solver(test_case["problem"]).search()
        solved = solved.replace("\n", "")
        self.assertEqual(solved, test_case["solution"])
    return test


for test_case in TEST_CASES:
    test_func = generate_test_func(test_case)
    setattr(TestSolve, 'test_%s' % test_case["name"], test_func)
