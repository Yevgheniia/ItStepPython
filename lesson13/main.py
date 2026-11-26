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