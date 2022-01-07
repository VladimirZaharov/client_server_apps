import unittest
import utils


class UtilsTestCase(unittest.TestCase):

    def test_load_config(self):
        self.config = utils.load_config()
        self.assertEqual(self.config['DEFAULT_IP_ADDRESS'], '127.0.0.1')

    def test_load_args(self):
        self.config = utils.load_config()
        self.assertEqual(utils.load_args(self.config).p, '7777')


if __name__ == '__main__':
    unittest.main()