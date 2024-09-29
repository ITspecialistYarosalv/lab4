import pandas as pd
import matplotlib.pyplot as plt
try:
    df = pd.read_csv('oleksiienko/people_data.csv')
    print("Ok")
except Exception as e:
    print("Не вдалося відкрити файл CSV:", e)
    exit()

if df.empty:
    print("Файл CSV порожній.")
    exit()


# Виводимо кількість співробітників чоловічої та жіночої статі
gender_counts = df['Стать'].value_counts()
print("Кількість співробітників за статтю:")
print(gender_counts)

# Будуємо діаграму для статі
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Кількість співробітників за статтю')
plt.xlabel('Стать')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.show()

# Рахуємо кількість співробітників кожної вікової категорії
df['Дата народження'] = pd.to_datetime(df['Дата народження'])

# Розраховуємо вік, поділяючи різницю між сьогоднішньою датою та датою народження на 365.25 (для врахування високосних років)
df['Вік'] = (pd.Timestamp.now() - df['Дата народження']).dt.days / 365.25

# Визначаємо вікові категорії
bins = [-1, 17, 45, 70, 100]  # Вікові категорії: <18, 18-45, 45-70, >70
labels = ['younger_18', '18-45', '45-70', 'older_70']
df['Вікова категорія'] = pd.cut(df['Вік'], bins=bins, labels=labels)

# Рахуємо кількість співробітників в кожній віковій категорії
age_category_counts = df['Вікова категорія'].value_counts()
print("\nКількість співробітників в кожній віковій категорії:")
print(age_category_counts)

# Будуємо діаграму для вікових категорій
age_category_counts.plot(kind='bar', color='green')
plt.title('Кількість співробітників за віковими категоріями')
plt.xlabel('Вікова категорія')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.show()

# Рахуємо кількість співробітників жіночої та чоловічої статі в кожній віковій категорії
gender_age_counts = df.groupby(['Стать', 'Вікова категорія']).size().unstack(fill_value=0)
print("\nКількість співробітників за статтю в кожній віковій категорії:")
print(gender_age_counts)

# Будуємо діаграму для кількості співробітників за статтю в кожній віковій категорії
gender_age_counts.plot(kind='bar', stacked=True)
plt.title('Кількість співробітників за статтю в кожній віковій категорії')
plt.xlabel('Вікова категорія')
plt.ylabel('Кількість')
plt.xticks(rotation=0)
plt.legend(title='Стать')
plt.show()