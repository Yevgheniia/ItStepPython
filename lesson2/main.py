# завдання 1

# #Встановлює значення числу Пі
# pi = 3.1415
#
# #Просить користувача ввести значення радіусу та одразу переводить його в необхідний тип
# radius = float(input("Введіть радіус: "))
#
# #розраховує площу
# area = pi * radius ** 2
#
# #виводить отриманні дані користувачу
# print(f"Площа кола: {area:.2f}")

# # завдання 2
#
# cup_price=float(input("Введіть ціну однієї кружки: "))
# budget_total=float(input("Введіть бюджет: "))
# cup_can_buy=budget_total//cup_price
#
# print(f"Можна купити: {cup_can_buy} кружки ")

# # завдання 3
# feet=3.2808399
# yards=1.0936133
#
# meters=float(input("Введіть довжину в метрах: "))
#
# meters_to_feet=meters/feet
# meters_to_yards=meters/yards
#
# print(f"Метрів - {meters:.2f}, це {meters_to_feet:.2f} футів або {meters_to_yards:.2f} ярдів.")

# # завдання 4
#
# change=budget_total%cup_price
# print(f"Решта складає {change:.2f} грн")

# # завдання 5

# total_time_minute=int(input("Введіть кількість хвилин: "))
#
# hour=int(total_time_minute//60)
# minute=total_time_minute%60
#
# print(f"Всього часу : {total_time_minute} хвилин \n Годин: {hour} \n Хвилин: {minute}")

# # завдання 6
# apple_recipe = 4
# milk_recipe = 1.2
#
# apple = int(input("Введіть кількість яблук: "))
# milk = float(input("Введіть кількість молока (л): "))
#
#
# cake_can_bake = int(apple // apple_recipe)
# milk_can_bake = int(milk // milk_recipe)
#
#
# cake = min(cake_can_bake, milk_can_bake)
#
# apple_leftover = apple - (cake * apple_recipe)
# milk_leftover = milk - (cake * milk_recipe)
#
# print(f"Можна спекти пирогів: {cake}")
# print(f"Залишиться яблук: {apple_leftover}")
# print(f"Залишиться молока: {milk_leftover:.2f}")

# # завдання 7

# deposite=float(input("Введіть суму вкладу: "))
# interest_rate=float(input("Введіть видсоток ставки: "))
# year=0
# sum_balance=(deposite*(1+interest_rate/100))
# year=year+1
# print(f"Кількість років вкладу: {year} \n Сума вкладу писля нарахування відсотків: {sum_balance:.2f} грн")
#
# sum_balance*=(1+interest_rate/100)
# year=year+1
# print(f"Кількість років вкладу: {year} \n Сума вкладу писля нарахування відсотків: {sum_balance:.2f} грн")
#
# sum_balance*=(1+interest_rate/100)
# year=year+1
# print(f"Кількість років вкладу: {year} \n Сума вкладу писля нарахування відсотків: {sum_balance:.2f} грн")
#
# sum_balance*=(1+interest_rate/100)
# year=year+1
# print(f"Кількість років вкладу: {year} \n Сума вкладу писля нарахування відсотків: {sum_balance:.2f} грн")
#
# sum_balance*=(1+interest_rate/100)
# year=year+1
# print(f"Кількість років вкладу: {year} \n Сума вкладу писля нарахування відсотків: {sum_balance:.2f} грн")

# # завдання 8

total_day_user=int(input("Введіть кількість днів: "))

year_user=total_day_user//365
week_user=total_day_user%365//7
day_user=total_day_user%365%7

print(f"{total_day_user} днів — це {year_user:.0f} рік, {week_user:.0f} тижні та {day_user:.0f} днів.")


