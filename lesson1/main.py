#завдання 1
balance = input("Введіть суму на рахунку:")
purchase = input("Введіть суму покупки:")

balance=float(balance)
purchase=float(purchase)
balance-=purchase
print("Ваш баланс:", balance)

#завдання 2
priceCoffee=input("Введіть вартість кави ")
countCoffee=input("Введіть кількість чашок кави: ")
order=float(priceCoffee)*int(countCoffee)

print("Вартість замовлення: ",order, "грн")
#завдання 3
width = input("Введіть ширину: ")
height = input("Введіть висоту: ")
area = float(width) * float(height)
print("Площа дорівнює:", area)
#завдання 4
totalOrder=input("Введіть суму рахунку: ")
tipsPersent=input("Введіть видсоток чайових: ")
tipsMoney=int(tipsPersent)/100
totalOrderPlusTips=tipsMoney+float(totalOrder)
print("Чайові: ", tipsMoney, "грн")
print("Загальна сума чеку: ", totalOrderPlusTips, "грн")
#завдання 5
distance=input("Введіть відстань: ")
fuelСonsumption=input("Введіть витрати пального на 100км: ")
gasPrice=input("Введіть вартість пального: ")
distance=float(distance)
fuelСonsumption=float(fuelСonsumption)
gasPrice=float(gasPrice)
tripCost=distance/fuelСonsumption*gasPrice
print("Вартість поїздки: ", tripCost, "грн")
#завдання 6
num1 = int(input("перше число: "))
num2 = int(input("друге число: "))
resultSum = num1 + num2
resultMin = num1 - num2
resultMult = num1 * num2
print("Сума чисел: ",resultSum)
print("Різниця чисел: ",resultMin)
print("Добуток чисел: ",resultMult)
#завдання 7
countPeople=input("Введіть кількість людей: ")
countPeople=int(countPeople)
payOnePerson=totalOrderPlusTips/countPeople
print("Оплата з однієї людини: ", payOnePerson, "грн")
#завдання 8
sumMoneyBuyer = float(input("Введіть суму грошей покупця: "))
price = float(input("Введіть вартість товару: "))
change= sumMoneyBuyer - price
print("Здача:", change)
#завдання 9
userName=input("Введіть Ваше им'я: ")
userYearOfBirth=input("Введіть рік народження: ")
userYearOfBirth=int(userYearOfBirth)
userHeight=input("Введіть Ваш зріст: ")
userOld= 2026-userYearOfBirth
print("=== АНКЕТА КОРІСТУВАЧАccc ===\n")
print("Им'я: ",userName, "\n")
print("Вік: ",userOld,"\n" )
print("Зріст: ", userHeight)



