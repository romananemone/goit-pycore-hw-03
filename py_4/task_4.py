from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.02.08"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

DATE_FORMAT = "%Y.%m.%d"

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    upcoming_birthdays = []
    today = datetime.today().date()
    
    for user in users:
        name = user["name"]
        birthday = user["birthday"]

        birthday_this_year = datetime.strptime(birthday, DATE_FORMAT).date().replace(year=today.year)
        
        closest_birthday = birthday_this_year.replace(year=today.year + 1) if (birthday_this_year < today) else birthday_this_year
        days_to_closest_birthday = (closest_birthday - today).days
        
        if days_to_closest_birthday <= 7 and days_to_closest_birthday >= 0:
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
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
