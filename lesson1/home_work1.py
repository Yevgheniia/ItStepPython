#завдання 1
num1 = input("перше число: ")
num2 = input("друге число: ")
sum = float(num1) * float(num2)
average = sum / 3
print("Сума:", sum)
print("Середнє:", average)
#Завдання 2 Користувач вводить суму в гривнях та курс долара. Переведіть гривні в долари та виведіть на екран
sum=input("Введіть суму в грн: ")
exchange_rate=input("Введіть курс долару: ")
exchange=float(sum)/float(exchange_rate)
print("Сума в доларах:", exchange)
#Завдання 3 Користувач вводить ціну товару та відсоток знижки. Виведіть суму знижки
price=input("Введіть ціну товару: ")
discount=input("Введіть відсоток знижки: ")
price_discount=float(price)*(1-(float(discount)/100))
print("Ціна зі знижкою :", price_discount)
# Завдання 4
slow_walk_kcal=3
fast_walk_kcal=4.5
jogging_kcal=9
slow_walk_time=input("Введіть час повільної ходьби: ")
fast_walk_time=input("Введіть час швідької ходьби: ")
jogging_time=input("Введіть час легкого бігу: ")
slow_walk_kcal_user=float(slow_walk_time)/slow_walk_kcal
fast_walk_kcal_user=float(fast_walk_time)/fast_walk_kcal
jogging_kcal_user=float(jogging_time)/jogging_kcal
total_burned_kcal=slow_walk_kcal_user+fast_walk_kcal_user+jogging_kcal_user
print("всього спалено ккал: ",total_burned_kcal," ккал")
