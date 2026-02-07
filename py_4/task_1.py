from datetime import datetime

def get_days_from_today(date: str) -> int:
    today = datetime.today().date()
    try:
        parsed_date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        raise ValueError(f"Incorrect date format: {date}. Expected format is 'YYYY-MM-DD'.")
        
    difference = today - parsed_date
    return difference.days


if __name__ == '__main__':
    get_days_from_today('2020-10-09')
    get_days_from_today('2026-2-21')