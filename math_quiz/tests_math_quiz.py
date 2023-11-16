import unittest
from math_quiz import function_D, function_E, function_F


class TestMathGame(unittest.TestCase):

    def test_function_D(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 100
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_D(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_E(self):
        # TODO
        pass

    def test_function_F(self):
            test_cases = [
                (3, 4, '+', '3 + 4', 7), (5, 2, '-', '5 - 2', 3), (6, 6, '*', '6 * 6', 36 )
                ''' TODO add more test cases here '''
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                pass

if __name__ == "__main__":
    unittest.main()
