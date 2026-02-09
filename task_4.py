from calendar import isleap
from datetime import date, datetime, timedelta
from typing import TypedDict

DATE_FORMAT = "%Y.%m.%d"

class User(TypedDict):
    name: str
    birthday: str

class UpcomingBirthday(TypedDict):
    name: str
    congratulation_date: str

def get_birthday_this_year(birthday: date, current_year: int) -> date:
    if birthday.month == 2 and birthday.day == 29 and not isleap(current_year):
        return date(current_year, 2, 28)
    
    return birthday.replace(year=current_year)

def get_upcoming_birthdays(users: list[User]) -> list[UpcomingBirthday]:
    upcoming_birthdays: list[UpcomingBirthday] = []
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        parsed_birthday = datetime.strptime(birthday, DATE_FORMAT).date()
        birthday_this_year = get_birthday_this_year(parsed_birthday, today.year)

        if birthday_this_year < today:
            closest_birthday = birthday_this_year.replace(year=today.year + 1)
        else:
            closest_birthday = birthday_this_year

        days_to_closest_birthday = (closest_birthday - today).days
        
        if 0 <= days_to_closest_birthday <= 7:
            congratulation_date = closest_birthday
            weekday = congratulation_date.isoweekday()

            if weekday in (6, 7):
                congratulation_date += timedelta(days=(8 - weekday))

            upcoming_birthdays.append({ 
                "name": name, 
                "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
            })

    return upcoming_birthdays

if __name__ == '__main__':
    users = [
        {"name": "John Doe", "birthday": "1985.02.08"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Emily Davis", "birthday": "1992.02.14"},
    ]
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
