# Підключаємо модуль random
from datetime import datetime as dt

def get_days_from_today(date):
# Отримуємо дані про сьогоднішнє число (без часу)
    date_today = dt.now().date()
# Перетворюємо рядок в дату
    other_date_strp = dt.strptime(date, "%Y%m%d").date()
# Вказуємо формулу для підрахунку різниці днів
    diff_between_dates = (date_today - other_date_strp).days
    return print(diff_between_dates)

# Отримуємо від користувача дату
get_days_from_today(input("Введіть дату у форматі 'РРРРММДД': "))