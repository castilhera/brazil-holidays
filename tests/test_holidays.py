import unittest
from datetime import date
from brazil_holidays import HolidayService, Holiday

class TestBrazilHolidays(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.service = HolidayService()

    def test_get_brazil_national_holidays_2023_should_return_12(self):
        holidays = self.service.get_brazil_national_holidays(2023)
        self.assertEqual(len(holidays), 12)

    def test_get_brazil_national_holidays_2024_should_return_13(self):
        holidays = self.service.get_brazil_national_holidays(2024)
        self.assertEqual(len(holidays), 13)

    def test_get_brazil_national_holidays_should_contain_consciencia_negra(self):
        year = 2024
        holidays = self.service.get_brazil_national_holidays(year)

        self.assertIn(Holiday(date(year, 11, 20), "Dia da Consciência Negra"),
                      holidays)

if __name__ == '__main__':
    unittest.main(verbosity=2)
