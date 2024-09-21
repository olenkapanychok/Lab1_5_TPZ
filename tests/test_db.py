import unittest
from unittest.mock import patch
import db

class TestDatabaseRead(unittest.TestCase):

    @patch('db.read_from_db')
    def test_read_from_db(self, mock_read):
        mock_read.return_value = {"data": "mocked_data"}
        result = db.read_from_db()
        self.assertEqual(result, {"data": "mocked_data"})

if __name__ == '__main__':
    unittest.main()

# mock_read - параметр для псевдо-читання
# у параметрі є поле return_value, у яке зберігаємо результат повернення -
# словник {"data": "mocked_data"}
# атрибут patch реагує на виклик функції read_from_db з файлу db
# тобто коли ми викликаємо функцію у 10 стрічці, вона повертає вищезгаданий словник і записує до result
# result - це {"data": "mocked_data"} словник
# далі ми перевіряємо за допомогою assertEqual чи наш result отримав цей ток у вигляді заданого словника