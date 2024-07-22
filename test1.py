import unittest
from main import main


class TestMainFunction(unittest.TestCase):

    def setUp(self):
        self.json_path = './data.json'

    def test_main_with_test1_json(self):
        result = main(self.json_path)
        expected_output = "Features\r\nфамилия\r\nкласс\r\nподгруппа\r\nпредмет\r\nвидДеятельности"

        self.assertEqual(result.strip(), expected_output.strip())

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            main('./non_existent_file.json')

if __name__ == '__main__':
    unittest.main()
