
#*************Task quantiy*****************

# import datetime

# now = datetime(1987, 3, 28, 13, 0, 0).weekday()
# print(now)

# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)



# def get_days_from_today(date):
#     pass

# from datetime import datetime, timedelta

# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)

# myDay = datetime(1987, 3, 28).toordinal()
# print(f"Мені {myDay} днів від Різдва Христового!!!")
# how_much = now - myDay
# print(how_much) 

# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу
# day = datetime.fromtimestamp(timestamp)
# print(day)

# myDay = datetime.timestamp(datetime(1987, 3, 28))
# print(myDay)

# back = datetime.fromtimestamp(myDay)
# print(back)

# my_day = datetime(1987, 3, 28, 13, 0, 0)

# print(my_day.strftime("%Y:%B-%d %A %H:%M:%S"))

# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

# print(iso_calendar)


# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC


# from datetime import datetime, timezone, timedelta

# utc_time = datetime.now(timezone.utc)

# # Створення часової зони для Східного часового поясу (UTC-5)
# eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# # Перетворює час UTC в час Східного часового поясу
# print(eastern_time)  


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")


# import time

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")


# import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")



# import random

# dice_roll = random.randint(1, 6)
# print(f"Ви кинули {dice_roll}")

# import random

# num = random.random()
# print(num)



#!!!!!!==========Task random Number============================


# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())
    
    #!!!!!!=========Regular============================

# import re

# text = "Вивчення Python може бути веселим."
# pattern = "Python"
# match = re.search(pattern, text)

# if match:
#     print("Знайдено:", match.group())
# else:
#     print("Не знайдено.")


# import re

# text = "Вивчення Python може бути веселим."
# pattern = r"в\w*м"
# match = re.search(pattern, text, re.IGNORECASE)

# if match:
#     print("Знайдено:", match.group())

# import re

# text = "Моя електронна адреса: example@example.com"
# pattern = r"\w+@\w+\.\w+"
# match = re.search(pattern, text)

# if match:
#     print("Електронна адреса:", match.group())


# import re

# email = "username@domain.com"
# pattern = r"(\w+)@(\w+\.\w+)"
# match = re.search(pattern, email)

# if match:
#     user_name = match.group(1)
#     domain_name = match.group(2)
#     print("Ім'я користувача:", user_name)
#     print("Домен:", domain_name)


# import re

# text = "Рік 2023 був складнішим, ніж 2022"
# pattern = r"\d+"
# matches = re.findall(pattern, text)

# print(matches)

# import re

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\w+"
# matches = re.findall(pattern, text)

# print(matches)  # Виведе список всіх слів у рядку

# import re

# file_name = "Мій документ Python.txt"
# pattern = r"\s"
# replacement = "_"
# formatted_name = re.sub(pattern, replacement, file_name)

# print(formatted_name)  


# import re

# text = "Python - потужна, універсальна; мова!"
# pattern = r"[;,\-:!\.]"
# replacement = ""
# modified_text = re.sub(pattern, replacement, text)

# print(modified_text)  

# import re

# phone = """
#         Михайло Куліш: 050-171-1634
#         Вікторія Кущ: 063-134-1729
#         Оксана Гавриленко: 068-234-5612
#         """
# pattern = r"(\d{3})-(\d{3})-(\d{4})"
# replacement = r"(\1) \2-\3"
# formatted_phone = re.sub(pattern, replacement, phone)

# print(formatted_phone)

# import re

# text = "Python - це проста, але потужна мова програмування."
# pattern = r"\s+"
# words = re.split(pattern, text)

# print(words)  # Виведе список слів у рядку

import re

text = "Python - потужна; проста, універсальна: мова!"
pattern = r"[;,\-:!\s]+"
elements = re.split(pattern, text)

print(elements)  # Виведе список частин, розділених пунктуацією
