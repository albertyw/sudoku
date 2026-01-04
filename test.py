import unittest

import solve

# Test Cases come from http://sudopedia.enjoysudoku.com/Valid_Test_Cases.html

TEST_CASES = [
    {
        "name": "completed",
        "problem": "974236158638591742125487936316754289742918563589362417867125394253649871491873625",
        "solution": "974236158638591742125487936316754289742918563589362417867125394253649871491873625",
    },
    {
        "name": "last_empty_square",
        "problem": "2564891733746159829817234565932748617128x6549468591327635147298127958634849362715",
        "solution": "256489173374615982981723456593274861712836549468591327635147298127958634849362715",
    },
    {
        "name": "naked_singles",
        "problem": "3x542x81x4879x15x6x29x5637485x793x416132x8957x74x6528x2413x9x655x867x192x965124x8",
        "solution": "365427819487931526129856374852793641613248957974165283241389765538674192796512438",
    },
    {
        "name": "hidden_singles",
        "problem": "xx2x3xxx8xxxxx8xxxx31x2xxxxx6xx5x27xx1xxxxx5x2x4x6xx31xxxx8x6x5xxxxxxx13xx531x4xx",
        "solution": "672435198549178362831629547368951274917243856254867931193784625486592713725316489",
    },
    {
        "name": "generated",
        "problem": "xx3x1xxxx4xx56x2x97xxxx81xxx8x1xxxx3xx18x94xx3xxxx4x8xxx59xxxx72x9x53xx4xxxx4x9xx",
        "solution": "953412678418567239726398145684125793571839462392674581145986327269753814837241956",
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


class TestEdgeCases(unittest.TestCase):
    def test_empty_grid_raises_value_error(self):
        """An empty string should raise ValueError during initialization."""
        with self.assertRaises(ValueError):
            solve.Solver("")

    def test_invalid_characters_raise_value_error(self):
        """Non‑digit, non‑'x' characters should raise ValueError during parsing."""
        problem = "12345678a" + "x" * 72  # one invalid character
        with self.assertRaises(ValueError):
            solve.Solver(problem)

    def test_incorrect_row_length_raises_value_error(self):
        """Rows that are not 9 characters long should raise ValueError during initialization."""
        # 8 digits in the first row, then 9 digits each for the rest
        problem = "123456789" + "x" * 73
        with self.assertRaises(ValueError):
            solve.Solver(problem)
