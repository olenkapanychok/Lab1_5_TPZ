import unittest
from unittest.mock import patch
import file_reader


class TestFileRead(unittest.TestCase):

    def test_read_from_file(self):
        def stub_read_from_file(file_path):
            return "stubbed data"

        with patch('file_reader.read_from_file', stub_read_from_file):
            result = file_reader.read_from_file("dummy_path")
            self.assertEqual(result, "stubbed data")


if __name__ == '__main__':
    unittest.main()