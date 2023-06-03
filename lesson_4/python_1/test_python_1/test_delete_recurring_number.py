import unittest
from lesson_4.python_1.delete_recurring_number import delete_recurring_number_2, delete_recurring_number


class TestDeleteRecurringNumber(unittest.TestCase):
    my_list_1 = [2, 5, 8, 125, 2, 12, 12, 3, 4]
    my_list_2 = [2, 7, 12, 3]

    def test_delete_recurring_number(self):
        self.assertEqual(delete_recurring_number(self.my_list_1, self.my_list_2), [5, 8, 125, 4])

    def test_delete_recurring_number_2(self):
        self.assertEqual(delete_recurring_number_2(self.my_list_1, self.my_list_2), [5, 8, 125, 4])


if __name__ == '__main__':
    unittest.main()
