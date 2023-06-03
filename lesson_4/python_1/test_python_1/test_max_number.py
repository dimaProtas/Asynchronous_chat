import unittest
from lesson_4.python_1.max_number import f_max


class TestMaxNumber(unittest.TestCase):

    def test_max_number(self):
        self.assertEqual(f_max(1, 4, 2), 4)


if __name__ == '__main__':
    unittest.main()
