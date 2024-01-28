# Підключаємо модуль re
import re


def normalize_phone(phone_number):
    # Отримуємо список рандомних номерів за допомогою модуля re та методу range
    p1=r"[\d\+]+"  
    # Отримуємо номер телефону в заданому форматі
    phone_number=''.join(re.findall(p1,phone_number))
    # Встановлюємо умови для додавання символів відповідно до довжини введеного номеру
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)==11:
        phone_number='+3'+phone_number
    elif len(phone_number)==12:
        phone_number='+'+phone_number
    return print(phone_number)
normalize_phone(input("Введіть номер телефону: "))