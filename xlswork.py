import pandas as pd
from datetime import datetime


def calculate_age_from_date(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

try:
    df = pd.read_csv('oleksiienko/people_data.csv')
except Exception as e:
    print("Не вдалося відкрити файл people_data.csv :", e)
    exit()


if df.empty:
    print("Файл people_data.csv порожній.")
    exit()


df['Дата народження'] = pd.to_datetime(df['Дата народження'])
df['Вік'] = df['Дата народження'].apply(calculate_age_from_date)

# Додаємо колонку з індексом для нумерації рядків
df['№'] = range(1, len(df) + 1)

# Вибираємо необхідні колонки для інших листів
columns = ['№', 'Прізвище', 'Ім’я', 'По батькові', 'Дата народження', 'Вік']

try:
    with pd.ExcelWriter('employees.xlsx') as writer:

        # Записуємо повну таблицю на лист 'all'
        df.to_excel(writer, index=False, sheet_name='all')

        # Фільтруємо та записуємо дані на відповідні листи з потрібними колонками
        younger_18 = df[df['Вік'] < 18][columns]
        younger_18.to_excel(writer, index=False, sheet_name='younger_18')

        between_18_45 = df[(df['Вік'] >= 18) & (df['Вік'] <= 45)][columns]
        between_18_45.to_excel(writer, index=False, sheet_name='18-45')

        between_45_70 = df[(df['Вік'] > 45) & (df['Вік'] <= 70)][columns]
        between_45_70.to_excel(writer, index=False, sheet_name='45-70')

        older_70 = df[df['Вік'] > 70][columns]
        older_70.to_excel(writer, index=False, sheet_name='older_70')

    print("Ok")

except Exception as e:
    print("Не вдалося створити файл employees.xlsx :", e)