# # Завдання 1
# text = input("Введіть рядок: ")
# symb = input("Введіть символ: ")
# count = 0
#
# print(f"Кількість символів {text.count(symb)}")
#
# for i in text:
#     if i == symb:
#         count += 1
# print(f"Кількість символів {count}")

# # Завдання 2

# text = input("Введіть рядок: ")
# word = "python"
#
# print(f"Кількість символів в рядку: {len(text)}")
# if word in text:
#     print("Слово python є в строці")
# else:
#     print("Слово python немає в строці")
#
# count = text.count("s") + text.count("z")+ text.count("h")
#
# print(f"Кількість символів {count}")

# # Завдання 3
# text = input("Введіть текст: ")
#
# result = text.replace(" ", "-")
# print(f"Змінений текст: {result}")

# # Завдання 4

# text = input("Введіть текст: ")
# word = input("Введіть слово: ")
# count = 0
#
# print(text.count(word))

# # Завдання 5

# items = input("Введіть ваші речі: ")
# items = items.lower()
#
# if "ніж" in items or "гроші" in items or "отрута" in items:
#     print("У вас є речі які заборонено перевозити")
# else:
#     print("Оформлено доставку")

# # Завдання 6
#
# text = input("Введіть текст: ")
#
# letter_count = 0
# number_count = 0
#
# for symbol in text:
#     if symbol.isdigit():
#         number_count += 1
#     elif symbol.isalpha():
#         letter_count += 1
#
# print(f"Літер: {letter_count}\nЦифр: {number_count}")

# # Завдання 7

while True:
    letter = False
    number = False
    password = input("Введіть пароль: ")

    if len(password) < 9:
        print("Пароль менше за 8 символів")
        continue

    for i in password:
        if i.isdigit():
            letter = True

        if i.isalpha():
            number = True


    if letter == False:
        print("Немає символів в паролі")
        continue
    elif number == False:
        print("Немає цифр в паролі")
        continue
    else:
        print("Пароль надійний")
        break



