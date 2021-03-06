import unittest
from app import main, home_work


class TestClass(unittest.TestCase):
    def setUp(self):
        # Дана функція налаштовує початкові агрументи визначені лише для класу
        self.date_url = 'http://date.jsontest.com/'
        self.ip_url = 'http://ip.jsontest.com/'

    def test_date_work_successfully(self):
        # Перевіряєм чи функція відправювала до кінця і вертаємо True
        self.assertTrue(main(self.date_url))

    def test_empty_url(self):
        # Перевіряєм чи у функцію не було передано URL
        self.assertFalse(main())

    def test_no_date_in_response(self):
        # Перевіряємо що у відповіді відсутнє поле дата (тобто передана направильна URL)
        with self.assertRaises(Exception):
            main(self.ip_url)

    def test_home_work(self):
        # Ваш захист
        self.assertEqual(home_work("12:12:12 AM"), "Day")
        self.assertEqual(home_work("12:12:12 PM"), "Night")
        
        try: 
            home_work("example non time text")
            self.assertTrue(False)
        except RuntimeError:
            self.assertTrue(True)

