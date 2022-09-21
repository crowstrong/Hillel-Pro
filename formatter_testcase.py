import unittest
from fullname import formatted_name


class FullNameTest(unittest.TestCase):
    def testCase1_first_last(self):
        result = formatted_name("mikhail", "zubenko")
        self.assertEqual(result, "Mikhail Zubenko")

    def testCase2_first_middle_last(self):
        result = formatted_name("mikhail", "zubenko", "petrovich")
        self.assertEqual(result, "Mikhail Petrovich Zubenko")

    def testCase3_exception(self):
        self.first_name = "Mikhail"
        self.last_name = "Zubenko"
        self.assertRaises(TypeError, formatted_name, self.first_name, self.last_name, -1)


if __name__ == '__main__':
    unittest.main()
