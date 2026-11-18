# ASSIGNMENT
# 3 date_parser.py — a @classmethod that builds an object from a string like "18-09-2026"

from datetime import datetime


class DateParser:

    def __init__(self, date):
        self._date = date

    @classmethod
    def from_string(cls, date_string):
        parsed_date = datetime.strptime(date_string, "%d-%m-%Y")
        return cls(parsed_date)

    @staticmethod
    def is_valid_date(date_string):
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False


# Classmethod testing
date1 = DateParser.from_string("18-09-2026")

print("Day:", date1._date.day)
print("Month:", date1._date.month)
print("Year:", date1._date.year)

# Staticmethod testing
print(DateParser.is_valid_date("18-09-2026"))  # True
print(DateParser.is_valid_date("35-15-2026"))  # False
print(DateParser.is_valid_date("hello"))       # False