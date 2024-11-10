import unittest
from math_quiz import randomIntGenerator, randomOperatorGenerator, randomProblemGenerator

class TestMathGame(unittest.TestCase):
    def test_randomIntGenerator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = randomIntGenerator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)
    def test_randomOperatorGenerator(self):
        # Test if the operator is one of the expected values
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test multiple selections to ensure randomness
            operator = randomOperatorGenerator()
            self.assertIn(operator, operators)
    def test_randomProblemGenerator(self):
            #Define test cases with different operators and outcomes
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (10, 4, '+', '10 + 4', 14),
                (10, 4, '-', '10 - 4', 6),
                (10, 4, '*', '10 * 4', 40)
                
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = randomProblemGenerator(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer, expected_answer)
                
if __name__ == "__main__":
    unittest.main()
