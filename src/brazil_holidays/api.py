from datetime import date, timedelta
from brazil_holidays.models import Holiday


def get_easter_date(year: int) -> date:
    """ Get the easter date for a given year.

    Meeus/Jones/Butcher Algorithm
    
    Ref: https://pt.wikipedia.org/wiki/C%C3%A1lculo_da_P%C3%A1scoa

    Args:
        year (int): the year to get the easter date.

    Returns:
        date: the easter date.
    """
    a = year % 19
    b, c = divmod(year, 100)
    h = (19 * a + b - b // 4 - (b - (b + 8) // 25 + 1) // 3 + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * (b % 4) + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month, day = divmod(h + l - 7 * m + 114, 31)

    return date(year, month, day+1)


def get_national_holidays(year: int) -> list[Holiday]:
    """ Get a list of holidays in Brazil for a given year.

    Args:
        year (int): the year to get the holidays.

    Returns:
        list[Holiday]: a list of holiday (date, name).
    """
    easter_date = get_easter_date(year)

    holidays = [
        Holiday(date(year, 1, 1), "Ano Novo"),
        Holiday(date(year, 4, 21), "Tiradentes"),
        Holiday(date(year, 5, 1), "Dia do Trabalho"),
        Holiday(date(year, 9, 7), "Independência do Brasil"),
        Holiday(date(year, 10, 12), "Nossa Senhora Aparecida"),
        Holiday(date(year, 11, 2), "Finados"),
        Holiday(date(year, 11, 15), "Proclamação da República"),
        Holiday(date(year, 12, 25), "Natal"),
        Holiday(easter_date, "Páscoa"),
        Holiday(easter_date + timedelta(days=-47), "Carnaval"),
        Holiday(easter_date + timedelta(days=-2), "Sexta-feira Santa"),
        Holiday(easter_date + timedelta(days=60), "Corpus Christi")
    ]

    if year > 2023:
        holidays.append(Holiday(date(year, 11, 20), "Dia da Consciência Negra"))

    holidays.sort(key=lambda h: h.date)

    return holidays
