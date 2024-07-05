from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.07.06"},
    {"name": "Jane Smith", "birthday": "1990.08.24"},
    {"name": "Lora Stone", "birthday": "1987.05.12"},
]


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        print(days_until_birthday)

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            if birthday_this_year.weekday() == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
