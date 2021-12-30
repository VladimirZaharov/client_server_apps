import unittest
import client
import server


class ClientTestCase(unittest.TestCase):

    def test_send_and_rsv_msg(self):
        server.main()
        self.assertEqual(client.main()['alert'], 'ответ сервера')

# знаю, что работать не будет, но не смог придумать как проверить
# прием-передачу


if __name__ == '__main__':
    unittest.main()