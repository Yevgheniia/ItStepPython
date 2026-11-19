# #Завдання 1
# age_user = int(input("Введіть Ваш вік: "))
#
# if age_user <= 12:
#     ticket_price = 80
# elif age_user >= 65:
#     ticket_price = 120
# else:
#     ticket_price = 200
#
# print(f"Вартість квитка: {ticket_price:.2f} грн")
# print("Гарного дня!")

# #Завдання 2
#
# weight = float(input("Введіть вагу товару в кг: "))
#
# if weight < 1:
#     print("Дрібна посилка")
# elif weight < 5:
#     print("Середня посилка")
# elif weight < 10:
#     print("Велика посилка")
# else:
#     print("Надважка посилка")

# #Завдання 3

# date_day = int(input("Введіть чісло місяця: "))
# date_month = input("Введіть назву місяця: ")
#
# if date_day == 1 or date_day == "січня":
#     print(f"сьогодні {date_day} {date_month} це свято Новий рік")
# elif date_day == 14 or date_day == "лютого":
#     print(f"сьогодні {date_day} {date_month} це свято день св Валентина")
# elif date_day == 25 or date_day == "грудня":
#     print(f"сьогодні {date_day} {date_month} це свято Різдво")
# elif date_day == 1 or date_day == "квітня":
#     print(f"сьогодні {date_day} {date_month} це свято день сміху")
# else:
#     print(f"сьогодні {date_day} {date_month} це будній день")

# #Завдання 4
# age_1 = int(input("Введіть вік першої людини: "))
# age_2 = int(input("Введіть вік другої людини: "))
# age_3 = int(input("Введіть вік третьої людини: "))
#
# if age_1 <= 12:
#     price_1 = 80
# elif age_1 >= 65:
#     price_1 = 120
# else:
#     price_1 = 200
#
# if age_2 <= 12:
#     price_2 = 80
# elif age_2 >= 65:
#     price_2 = 120
# else:
#     price_2 = 200
#
# if age_3 <= 12:
#     price_3 = 80
# elif age_3 >= 65:
#     price_3 = 120
# else:
#     price_3 = 200
#
# total_price = price_1 + price_2 + price_3
#
# print(f"Вартість першого квитка: {price_1:.2f} грн")
# print(f"Вартість другого квитка: {price_2:.2f} грн")
# print(f"Вартість третього квитка: {price_3:.2f} грн")
# print(f"Загальна вартість: {total_price:.2f} грн")
# print("Гарного дня!")

# #Завдання 5
#
# # запит користувачу, щоб він ввів назву товару
# product = input("Введіть назву товару: ")
#
# # Перевірка виду товару
# if product == "алкоголь" or product == "тютюн":
#     # запит користувачу, щоб він ввів свій вік
#     age = int(input("Введіть ваш вік: "))
#     # перевірка віку
#     if age >= 18:
#         print("Дозволено до продажу")
#     #
#     else: print("Дозволено до продажу")
#
# # продовження циклу перевірки виду товару
# elif product == "ліки":
#     # запит рецепта
#     prescription = input("У вас є рецепт від лікаря? ")
#     # перевірка наявності рецепта
#     if prescription == "так":
#         print("Дозволено до продажу")
#     else:
#         print("Заборонено до продажу")
# #  продовження циклу перевірки виду товару
# else:
    #print("Дозволено до продажу")

# #Завдання 6
# is_logged_in = input("Ви увійшли в систему? (так/ні): ")
# cart_is_empty = input("Ваш кошик порожній? (так/ні): ")
# balance = float(input("Введіть баланс: "))
# total_price = float(input("Введіть вартість замовлення: "))
# # if is_logged_in == "так":
# #     if cart_is_empty == "ні":
# #         if balance >= total_price:
# #             print("Замовлення успішно оформлено!")
# #         else: print("Недостатньо коштів на рахунку")
# #     else: print("Ваш кошик порожній")
# # else: print("Будь ласка, увійдіть в систему")
# if is_logged_in != "так":
#     print("Будь ласка, увійдіть в систему")
# elif cart_is_empty != "ні":
#     print("Ваш кошик порожній")
# elif balance < total_price:
#     print("Недостатньо коштів на рахунку")
# else:
#     print("Замовлення успішно оформлено!")

speed_user = float(input("Введіть швидкість: "))

if speed_user >= 90:
    place_user = input("Де їдете місто чи траса: ")
    if place_user == "місто":
        print("Ви отримуєте штраф")
    else:
        print("Ви отримуєте попередження")
elif speed_user <= 15:
    year_car = int(input("Введіть вік машини: "))
    if year_car >= 15:
        print("Купіть нову машину ")
    else:
        print("Треба поїхати на СТО")
else:
    print("Гарної подорожі")