import unittest

from lesson_3.variables import RESPONSE, ERROR, ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE
from lesson_3.client import create_presence, process_ans


class TestClient(unittest.TestCase):

    #Тест коректного запроса
    def test_corected_request(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'dima_protasevich'}})

    # Тест коректной работы ответа 200 : OK
    def test_corected_answer_ok(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    # Тест ответа ERROR: Bad Request
    def test_corected_answer_bad(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
