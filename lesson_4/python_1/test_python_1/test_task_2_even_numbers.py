import unittest
from lesson_4.python_1.task_2_even_numbers import my_func


class TestEventNumber(unittest.TestCase):

    def test_event_number(self):
        self.assertEqual(my_func(2224441), 'Четные числа: 6, Не четные числа: 1')


if __name__ == '__main__':
    unittest.main()
