from datetime import datetime

def get_days_from_today(date):
    
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        days_difference = current_date - given_date
    
        print(f"Кількість днів між заданими датами складає {days_difference.days}")
        return days_difference.days
    
    except ValueError:
        print('Дата має бути введена у форматі "РРРР-ММ-ДД"')

print(get_days_from_today("2021-10-09"))

