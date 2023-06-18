sum = 0
tickets = int(input("Введите количество билетов:"))
for age in range(tickets):
    age = int(input("Введите возраст посетителя:"))
    if age < 18:
       sum += 0
    elif age >= 18 and age <= 25:
       sum += 990
    elif age > 25:
       sum += 1390
if tickets > 3 :
    print("Кол-во билетов:", tickets)
    discount = sum / 100 * 10
    print("Скидка:", discount, "руб.")
    print("К оплате с учетом скидки:", (sum - discount), "руб.")
if tickets < 4 :
    print("Кол-во билетов:", tickets)
    Nodiscount = sum
    print("К оплате:", Nodiscount, "руб.")