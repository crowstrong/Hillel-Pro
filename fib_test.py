import unittest
from fib import Fibonacci


class FibonacciTest(unittest.TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def testCase1_small(self):
        self.assertEqual(self.fibonacci(1), 1, "Case1 unit test")

    def testCase2_big(self):
        self.assertEqual(self.fibonacci(67), 44945570212853, "Case2 unit test")

    def testCase3_zero(self):
        self.assertEqual(self.fibonacci(0), 0, "Case3 unit test")

    def testCase4_negative(self):
        self.assertRaises(ValueError, self.fibonacci, -1)

    def testCase5_float(self):
        self.assertRaises(ValueError, self.fibonacci, 1.1)

    def testCase6_string(self):
        self.assertRaises(ValueError, self.fibonacci, "1")

    def testCase7_recursion(self):
        self.assertRaises(RecursionError, self.fibonacci, 500)


if __name__ == '__main__':
    unittest.main()
