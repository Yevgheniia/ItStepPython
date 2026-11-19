import random

# # Завдання 1
#
# while True:
#     num = int(input("введіть число від 1 до 9: "))
#
#     if num < 1 or num > 9:
#         print("Ви ввели неправильне число! ")
#         continue
#
#     count = 0
#
#     while True:
#         if count >= 10:
#             break
#         else:
#             count += 1
#             print(f"{num} * {count} = {num * count}")
#     break
#
# # Завдання 2
#
# total = 0
# count = 0
# while True:
#   grade = int(input("Введіть оцінку: ") )
#
#     if grade == 0:
#         break
#
#     count += 1
#     total += grade
#     average_grade = total / count

#print(f"середня оцінка: {average_grade}")

# # Завдання 3
#
# num_1 = float(input("Введіть перше число: "))
# num_2 = float(input("Введіть друге число: "))
#
# while True:
#     answer = int(input("Оберіть яку дию виконати: 1. сума 2. різниця 3. добуток 4. частка 5. вихід "))
#
#     if answer < 1 or answer > 5:
#         continue
#
#     if answer == 1:
#         print(f"{num_1} + {num_2} = {num_1 + num_2}")
#     elif answer == 2:
#         print(f"{num_1} - {num_2} = {num_1 - num_2}")
#     elif answer == 3:
#         print(f"{num_1} * {num_2} = {num_1 * num_2}")
#     elif answer == 4:
#         if num_2 == 0.00:
#             print("Не можна ділити на 0")
#         else:
#             print(f"{num_1} / {num_2} = {num_1 / num_2}")
#     else:
#         break

# # Завдання 4
# count = 0
#
# while True:
#     if count == 3:
#         break
#
#     name = input("Введіть ім'я: ")
#
#     if name == "admin":
#         print("Це ім'я недоступне")
#     else:
#         count += 1
#         print(f"Учасник №{count}: {name}")

# # Завдання 5

count = 0
secret_num = random.randint(0, 100)

while True:
    count += 1
    print(secret_num)
    num_user = input("Вгадайте число від 0 до 100. Ваш варіант: ")

    if num_user.isdigit():
        num_user = int(num_user)

        if num_user > secret_num:
            print("Забагато")

        elif num_user < secret_num:
            print("Замало ")

        else:
            print(f"Ви вгадали(кінець програми) Кількість спроб: {count}")
            break


    else:
        if num_user == "stop":
            print(f"Ви не вгадали. Число було: {secret_num} Кількість спроб: {count}")
            break
        else:
            print("Ви ввели невірне число")








