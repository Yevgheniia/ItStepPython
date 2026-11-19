# #Завдання 1
# count_cookies = int(input("Введіть кількість печива: "))
# cookies = "🍪"
#
# for i in range(count_cookies):
#     print(cookies, end="")
#
# #Завдання 2
#
# count_clients = int(input("Введіть кількість клієнтів:"))
# number = 1001
#
# print("Рахунки:")
#
# for i in range (count_clients):
#     print(f"INV-{number+i}")
from tempfile import tempdir

# #Завдання 3

# day_tr = int(input("Раз на скільки днів тренуватися: "))
#
# for i in range(1, 30, day_tr):
#     print(f"День тренування: {i}")

# #Завдання 4
# count_food = int(input("Введіть кількість печива: "))
# food = input("Введіть що саме в кошик Ви кладете 🍪 🧁 🍩 🍬 🍫 🍭 🥨 🥠 🍰 🍎 🍏 🍐 🍊 🍌 🍉 🍇 🍓 🫐 🍒 🍑 🥭 🥝: ")
#
# for i in range(count_food):
#     print(food, end="")

# #Завдання 5

# print("Починаю зворотній відлік")

# for i in range (10, 0, -1):
#     print(i)

# print("Запуск!")

# #Завдання 6

# num = int(input("Введіть число: "))
# for i in range(1, 11):
#     result = num * i
#     print(f"{num} * {i} = {result}")

# # завдання 7
#
# deposite=float(input("Введіть суму вкладу: "))
# interest_rate=float(input("Введіть відсоток ставки: "))
#
# for i in range(1, 6):
#     deposite*=(1+interest_rate/100)
#     print(f"Кількість років вкладу: {i} \n Сума вкладу писля нарахування відсотків: {deposite:.2f} грн")

# # Додаткові
# Завдання 1
# Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні.

number_1 = int(input("Введіть перше число: "))
number_2 = int(input("Введіть друге число: "))
#
# for i in range(number_1, number_2+1):
#     print(i)

# # Завдання 2
# Користувач вводить з клавіатури два числа.
# Вкажіть усі непарні числа у заданому діапазоні.

# if number_1 % 2 != 0:
#     for i in range(number_1, number_2+1, 2):
#         print(i)
# else:
#     for i in range(number_1 + 1, number_2 + 1, 2):
#         print(i)

# # Завдання 3
# Користувач вводить з клавіатури два числа.
# Вкажіть усі парні числа у заданому діапазоні.

# if number_1 % 2 == 0:
#     for i in range(number_1, number_2+1, 2):
#         print(i)
# else:
#     for i in range(number_1+1, number_2+1, 2):
#         print(i)

# # Завдання 4
# Користувач вводить з клавіатури два числа.
# Вкажіть усі числа у заданому діапазоні за спаданням.

# for i in range(number_2, number_1 - 1, -1):
#     print(i)

# Завдання 5
# Користувач вводить з клавіатури два числа. Вкажіть
# усі непарні числа у заданому діапазоні. Якщо межі
# діапазону вказані неправильно, потрібно провести
# нормалізацію меж. Наприклад, користувач ввів 33 і 13.
# Потрібна нормалізація, після якої початок діапазону
# дорівнюватиме 13, а кінець дорівнюватиме 33.

if number_1 > number_2:
    temp = number_1
    number_1 = number_2
    number_2 = temp
for i in range(number_1, number_2):
    print(i)