from faker import Faker
import random
import csv
fake = Faker(locale='uk_UA')
fathers_names = {
    "чоловічі": [
        "Андрійович", "Богданович", "Вікторович", "Григорович", "Дмитрович",
        "Євгенович", "Захарович", "Іванович", "Костянтинович", "Леонідович",
        "Михайлович", "Миколайович", "Олександрович", "Петрович", "Русланович",
        "Сергійович", "Тарасович", "Федорович", "Юрійович", "Ярославович"
    ],
    "жіночі": [
        "Андріївна", "Богданівна", "Вікторівна", "Григорівна", "Дмитрівна",
        "Євгенівна", "Захарівна", "Іванівна", "Костянтинівна", "Леонідівна",
        "Михайлівна", "Миколаївна", "Олександрівна", "Петрівна", "Русланівна",
        "Сергіївна", "Тарасівна", "Федорівна", "Юріївна", "Ярославівна"
    ]
}
table = [
    ["Прізвище", "Ім’я", "По батькові",
     "Стать", "Дата народження",
     "Посада", "Місто проживання",
     "Адреса проживання", "Телефон", "Email"]
]
woman = 0
man = 0

for i in range(0,2000):
    sex = random.choices(["чоловіча","жіноча"],weights=[0.6,0.4])[0]

    if sex == "чоловіча":
        surname = fake.last_name()  # Генеруємо випадкове прізвище
        name = fake.first_name_male()  # Генеруємо чоловіче ім’я
        fathername = random.choice(fathers_names["чоловічі"])  # Вибір по батькові
        man+=1

    elif sex=="жіноча":
        surname = fake.last_name()  # Генеруємо випадкове прізвище
        name = fake.first_name_female()  # Генеруємо жіноче ім’я
        fathername = random.choice(fathers_names["жіночі"])  # Вибір по батькові
        woman += 1


    birthday = fake.date_of_birth(minimum_age=16, maximum_age=96).strftime("%Y-%m-%d")  # Дата народження
    job = fake.job()  # Посада
    city = fake.city()  # Місто
    address = fake.address().replace('\n', ', ')  # Адреса
    telephone = fake.phone_number()  # Телефон
    email = fake.email()

    table.append([surname,name,fathername,sex,birthday,job,city,address,telephone,email])

filename = 'oleksiienko/people_data.csv'
print(man)
print(woman)
with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print(f"Data saved to {filename}")


