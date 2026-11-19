# #завдання 1
# age_user=int(input("введіть свій вік: "))
#
# if 18<= age_user <=65:
#     print("Працездатний/на")
# else:
#     print("Непрацездатний/на")
#
# #завдання 2
#
# secret_password = "OpenSesame123"
# secret_login = "AliBaba"
#
# user_password=input("Введіть пароль: ")
# user_login=input("Введіть логін: ")
#
# if secret_password==user_password and user_login==secret_login:
#     print("Доступ дозволено")
# else:
#     print("Доступ заблоковано")
#
# #завдання 3
#
# price=float(input("Введіть вартість товару: "))
# count=float(input("Введіть кількість товару: "))
# age_user=int(input("Введіть Ваш вік: "))
# discount=0.15
#
# if age_user<18 or age_user>65:
#     total_sum=price*count*(1-discount)
#     print(f"Сума чеку зі зніжкою 15% складає {total_sum:.2f} грн")
# else:
#     total_sum = price * count
#     print(f"Сума чеку складає {total_sum:.2f} грн")
#
# #завдання 4
#
# age = 23
# has_license = "так"
# accidents = 0
# # if age >= 18:
# # if has_license == "так":
# # if accidents == 0:
# # print("Оренда дозволена")
# # else:
# # print("Оренда заборонена")
# # else:
# # print("Оренда заборонена")
# # else:
# # print("Оренда заборонена")
# if age>=18 and has_license == "так" and accidents == 0:
#     print("Оренда дозволена")
# else:
#     print("Оренда заборонена")
#
# #завдання 5
#
# sum_user=float(input("Введіть суму покупки: "))
# delievery=120
#
# if sum_user<500:
#     total_sum=sum_user+delievery
#     print(f"Сума покупки з доставкою складає: {total_sum:.2f} грн")
# elif 500 < sum_user < 1000:
#     total_sum = sum_user + delievery*0.95
#     print(f"Сума покупки з доставкою та зі знижкою 5% складає: {total_sum:.2f} грн")
# elif 1000 <= sum_user < 2000:
#     total_sum = sum_user + delievery * 0.8
#     print(f"Сума покупки з доставкою та зі знижкою 20% складає: {total_sum:.2f} грн")
# elif sum_user>=2000:
#     total_sum = sum_user
#     print(f"Сума покупки : {total_sum:.2f} грн. Доставка безкоштовна")
# else:
#     print("Сума покупки невірна")

# #завдання 6

# sum_credit_user=float(input("Введіть суму кредиту: "))
# credit_term_user=float(input("Введіть термін у роках: "))
#
# if sum_credit_user <= 0 or credit_term_user <= 0:
#     print("Невірні дані")
# else:
#     if sum_credit_user <= 10000 and credit_term_user <= 3:
#         interest_rate = 8
#     elif sum_credit_user <= 10000 and credit_term_user > 3:
#         interest_rate = 10
#     elif 10000 < sum_credit_user <= 50000 and credit_term_user <= 3:
#         interest_rate=12
#     elif 10000 < sum_credit_user <= 50000 and credit_term_user > 3:
#         interest_rate=14
#     else:
#         interest_rate = 20
#
#     sum_credit_total = sum_credit_user * (1 + interest_rate / 100 * credit_term_user)
#     monthly_payment=sum_credit_total/credit_term_user/12
#
#     print(f"Відсоткова ставка складає: {interest_rate:.2f} %\nЗагальна сума кредиту: {sum_credit_total:.2f} "
#           f"$\nЩомісячний платіж: {monthly_payment:.2f} $")

# #Додаткове завдання
# # Користувач з клавіатури вводить кількість годин. Якщо отримане значення перебуває в діапазоні від 0 до 6
# # потрібно вивести напис "Good Night", якщо в діапазоні від 6 до 13 — "Good Morning",
# # якщо в діапазоні від 13 до 17 — "Good Day", якщо в діапазоні від 17 до 0 — "Good Evening".
# # Верхня межа діапазону не включається. Наприклад, число 6 відноситься до 6 до 13.
#
# hours_user=int(input("Введіть кількість годин: "))
#
# if 0 < hours_user <6:
#     print("Good Night")
# elif 6 <= hours_user <13:
#     print("Good Morning")
# elif 13 <= hours_user <17:
#     print("Good Day")
# elif 17 <= hours_user <24 or hours_user==0:
#     print("Good Evening")
# else:
#     print("Невірний час")

# # Користувач вводить поточну температуру в градусах Цельсія. Залежно від температури програма виводить повідомлення:
# #
# # Якщо температура менше -10°C — "Дуже холодно";
# # Від -10°C до 0°C — "Холодно";
# # Від 0°C до 15°C — "Прохолодно";
# # Від 15°C до 25°C — "Тепло";
# # Вище 25°C — "Спекотно".
#
# temp_user=int(input("Введіть поточну температуру в градусах Цельсія: "))
#
# if temp_user < -10:
#     print("Дуже холодно")
# elif -10 <= temp_user < 0:
#     print("Холодно")
# elif 0 <= temp_user < 15:
#     print("Прохолодно")
# elif 15 <= temp_user < 25:
#     print("Тепло")
# else:
#     print("Спекотно")

# # Користувач вводить з клавіатури розмір файлу в гігабайтах і швидкість інтернет-з'єднання в бітах за секунду.
# # Залежно від вибору користувача порахувати, за скільки годин, або хвилин, або секунд завантажиться файл.
# file_size=float(input("Введіть розмір файлу в гігабайтах: "))
#
# internet_speed=float(input("Введіть швидкість інтернет-з'єднання в бітах за секунду: "))
#
# time_unit = input("Оберіть одиницю часу (годин/хвилин/секунд): ")
#
# if time_unit=="годин":
#     download_time = (file_size * 1024 ** 3 * 8) / internet_speed / 3600
#
# elif time_unit=="хвилин":
#     download_time = (file_size * 1024 ** 3 * 8) / internet_speed / 60
# else:
#     download_time = (file_size * 1024 ** 3 * 8) / internet_speed
#
# print(f"Файл завантажиться за {download_time:.2f} {time_unit}")



