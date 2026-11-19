# # Завдання 1
#
# name_user = input("Введіть ім'я: ")
#
#
# while True:
#     age_user = int(input("Введіть вік: "))
#     if age_user >= 0:
#         print(f"Привіт {name_user}. Тобі {age_user} років")
#         break
#     else:
#         print("Введіть правильний вік")

# # Завдання 2

# goal = float(input("Цільова сума? "))
# total = 0
# while True:
#
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто! У скарбничці {total} грн.")

# # Завдання 3

# yard = 0.9144
# foot = 0.3048
#
# while True:
#     meter = float(input("Введіть довжину в метрах: "))
#     meter_in_yard = meter * yard
#     meter_in_foot = meter * foot
#     print(f"Сума в ярдах {meter_in_yard}")
#     print(f"Сума в футах {meter_in_foot}")
#     cont_answ = input("продовжувати роботу програми так/ні ?")
#     if cont_answ == "ні":
#         break

# # Завдання 4

# goal = float(input("Цільова сума? "))
# total = 0
# day_count = 0
#
# while True:
#     day_count += 1
#     daily_amount = float(input("Сьогоднішній вклад? "))
#     total += daily_amount
#     if total >= goal:
#         break
#
# print(f"Мету досягнуто! У скарбничці {total} грн за {day_count}.")

# # Завдання 5

# total_items = 0
# print("Додайте товари. Для завершення введіть 'stop'.")
# while True:
#     item = input("Введіть товар: ")
#
#     if item == "stop":
#         print("Підрахунок завершений")
#         break
#
#     total_items += 1
#
# print(f"Всього товарів додано: {total_items}")

# # Завдання 6

correct_password = 1234
login_attempt = 0
while True:

    print(f"Введіть пароль. У Вас є {3 - login_attempt} спроб")
    login_attempt += 1

    password = int(input("Введіть пароль: "))

    if password == correct_password:
        input("Ви ввели вірний пароль")
        break

    if login_attempt >= 3:
        print("Спроб більше немає")
        break







