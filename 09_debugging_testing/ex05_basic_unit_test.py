import unittest
from math_tool import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2,3),6)

if __name__ == "__main__":
    unittest.main()