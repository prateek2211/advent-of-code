import unittest


class MyTestCase(unittest.TestCase):
    def test_program(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
