# # Завдання 1
# str = input("Введіть рядок: ")
# symb = input("Введіть символ: ")
# count = 0
#
# print(f"Кількість символів {str.count(symb)}")
#
# for i in str:
#     if i == symb:
#         count += 1
# print(f"Кількість символів {count}")

# # Завдання 2

str = input("Введіть рядок: ")
word = "python"

print(f"Кількість символів в рядку: {len(str)}")
if word in str:
    print("Слово python є в строці")
else:
    print("Слово python немає в строці")

count = str.count("s") + str.count("z")+ str.count("h")

print(f"Кількість символів {count}")

