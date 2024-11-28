import unittest
from datetime import date

import brazil_holidays

class TestBrazilHolidays(unittest.TestCase):


    def test_get_brazil_national_holidays_2023_should_return_12(self):
        holidays = brazil_holidays.get_national_holidays(2023)
        self.assertEqual(len(holidays), 12)


    def test_get_brazil_national_holidays_2024_should_return_13(self):
        holidays = brazil_holidays.get_national_holidays(2024)
        self.assertEqual(len(holidays), 13)


    def test_get_brazil_national_holidays_should_contain_consciencia_negra(self):
        year = 2024
        holidays = brazil_holidays.get_national_holidays(year)

        self.assertIn(
            brazil_holidays.Holiday(
                date=date(year, 11, 20),
                name="Dia da Consciência Negra"
            ),
            holidays
        )

if __name__ == '__main__':
    unittest.main(verbosity=2)
