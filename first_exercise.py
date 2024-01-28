# Підключаємо модуль random
from datetime import datetime as dt

def get_days_from_today(date):
    try:
        date_today = dt.now().date() #сьогоднішня дата (без годин, хвилин та секунд)
        other_date_strp = dt.strptime(date, "%Y%m%d").date() # Перетворюємо рядок в дату
        diff_between_dates = (date_today - other_date_strp).days # Вказуємо формулу для підрахунку різниці днів
        return diff_between_dates
    except ValueError:
        print("Дата введена у невірному форматі. Спробуйте ще раз")
# Отримуємо від користувача дату і виводимо результат
print(get_days_from_today(input("Введіть дату у форматі 'РРРРММДД': ")))
