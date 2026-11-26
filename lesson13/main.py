# Завдання 1
# numbers = [1, 8, -5, 9]
#
# print(numbers)
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 3
# print(numbers)
#
# for i in range(len(numbers)):
#     if numbers[i] > 10:
#         numbers[i] = 0
#
# print(numbers)

# # Завдання 2
# numbers = []
#
# while True:
#     num = int(input("Введіть число: "))
#
#     if num == -1:
#         break
#     numbers.append(num)
#
# print(numbers)
#
# print(f"Кількість елементів: {len(numbers)}")
#
# print("Кількість елементів:", len(numbers))
# print("Сума елементів масива:", sum(numbers))
# print("Мінімальне число в масиві:", min(numbers))
# print("Максимальне число в масиві:", max(numbers))
# print("Середнє:", sum(numbers) / len(numbers))

# # Завдання 3
# positive = []
# negative = []
#
# while True:
#     number = int(input("Введіть число (0 для завершення): "))
#
#     if number == 0:
#         break
#     elif number > 0:
#         positive.append(number)
#     else:
#         negative.append(number)
#
# print("Додатні числа:", positive)
# print("Від'ємні числа:", negative)

# # Завдання 4
# salaries = []
#
# while True:
#     salary = int(input("Введіть зарплату: "))
#
#     if salary == -1:
#         break
#     if salary < -1:
#         print("Введіть додатне число")
#         continue
#     salaries.append(salary)
#
# print(salaries)
#
# salary_change_percent = int(input("Введіть відсоток зміни зарплати"))
#
# for i in range(len(salaries)):
#     salaries[i] = salaries[i] * (1+(salary_change_percent/100))
#
# print(salaries)

# # Завдання 5

# days = int(input("Введіть кількість днів: "))
# temperatures = []
#
# for i in range(days):
#
#     temperature = float(input(f"Введіть температуру за {i + 1}-й день: "))
#     temperatures.append(temperature)
#
# print("Температури:", temperatures)
#
# for i in range(days):
#     if i != 0:
#         difference = temperatures[i] - temperatures[i - 1]
#         print(f"Різниця температур за {i + 1}-й день: {difference}")

# # Завдання 6

bank_client  = [100, 200, 300, 500]

while True:
    comand = int(input("Виберіть одну з команд \n1 - Додати клієнта \n2 - Видалити клієнта \n3 - Поповнити рахунок \n4 - Зняти кошти \n5 - Вихід \nВаш вибір: "))

    if comand == 1:
        bank_client.append(0)
    elif comand == 2:
        while True:
            index_client = int(input("Введіть індекс клієнта: "))
            if index_client < 0 or index_client >= len(bank_client):
                print("Ви ввели невірний індекс клієнта")
                continue
            else:
                bank_client.pop(index_client)
                break
    elif comand == 3:
        while True:
            index_client = int(input("Введіть індекс клієнта: "))
            if index_client < 0 or index_client >= len(bank_client):
                print("Ви ввели невірний індекс клієнта")
                continue
            else:
                deposit_amount = int(input("Введіть суму поповнення: "))
                bank_client[index_client] += deposit_amount
                break
    elif comand == 3:
        while True:
            index_client = int(input("Введіть індекс клієнта: "))
            if index_client < 0 or index_client >= len(bank_client):
                print("Ви ввели невірний індекс клієнта")
                continue
            else:
                deposit_amount = int(input("Введіть суму зняття: "))
                bank_client[index_client] -= deposit_amount
                break
    elif comand == 5:
        break

    else:
        print("Введіть вірну команду: ")
        continue

print(bank_client)

