# Підключаємо модуль random
import random as rd 

def get_numbers_ticket(min, max, quantity):
    # Отримуємо список рандомних номерів за допомогою модуля randon та методу range
    list_random_numbers = rd.sample(range(min, max), quantity)
    # Встановлюємо обмеження, при яких функція має повернути нам пустий список
    if min < 1 or max > 1000 or quantity > max - min:
        return print(list())
    # Сортуємо список від менших до більших та вказуємо, що функція має повернути в разі задоволення усіх вимог
    else:
        list_random_numbers.sort()
        return print(list_random_numbers)
    
# Викликаємо функцію та запитуємо у користувача значення аргументів функції
get_numbers_ticket(int(input("Введіть число 'Від': ")),\
int(input("Введіть число 'До': ")), int(input("Введіть кількість випадкових номерів: ")))