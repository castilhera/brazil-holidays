"""
Brazilian Holidays API
~~~~~~~~~~~~~~~~~~~~~

Library to get the brazilian holidays.
"""
from .models import Holiday

from .api import (
    get_easter_date,
    get_national_holidays
)
