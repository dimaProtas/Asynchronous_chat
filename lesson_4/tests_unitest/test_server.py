import unittest


from lesson_3.server import process_client_message
from lesson_3.variables import RESPONSE, ERROR, ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE


class TestServer(unittest.TestCase):

    error_result = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }
    result_ok = {RESPONSE: 200}

    # тест проверка Action(действие)
    def test_no_action(self):
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'dima_protasevich'}}), self.error_result)

    # тест на проверку нужного пользователя
    def test_user_not(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'no_name'}}), self.error_result)

    # тест на коректный запрос
    def test_corected_request(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'dima_protasevich'}}), self.result_ok)


if __name__ == '__main__':
    unittest.main()
