alice_in_wonderland =  (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)
print(alice_in_wonderland)
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
apostrophes = []
for char in alice_in_wonderland:
    if char == "'":
        apostrophes.append(char)

print("Знайдено одинарних лапок:", len(apostrophes), "шт.")
print("Список знайдених лапок:", apostrophes)

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("\nТекст з книги 'Alice In Wonderland':")
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f"Задача 4: Яку площу займають Чорне та Азовське моря разом?")
print(f"Чорне море: {black_sea_area} км²")
print(f"Азовське море: {azov_sea_area} км²")
print(f"Разом: {total_area} \n")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_warehouse = 375291
warehouse_1_2 = 250449
warehouse_2_3 = 222950
warehouse_2 = warehouse_1_2 + warehouse_2_3 - total_warehouse
warehouse_1 = warehouse_1_2 - warehouse_2
warehouse_3 = warehouse_2_3 - warehouse_2

print(f"Задача 5: Скільки товарів знаходиться на кожному складі?")
print(f"Склад 1: {warehouse_1} товарів")
print(f"Склад 2: {warehouse_2} товарів")
print(f"Склад 3: {warehouse_3} товарів\n")



# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
months = 18
computer_price = monthly_payment * months
print(f"Задача 6: Яка загальна вартість комп'ютера?")
print(f"Щомісячний платіж: {monthly_payment} грн")
print(f"Кількість місяців: {months}")
print(f"Загальна вартість: {computer_price} грн\n")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9

print("Задача 7: Знайди остачу від ділення чисел:")
print(f"8019 : 8 -> Остача: {a}")
print(f"9907 : 9 -> Остача: {b}")
print(f"2789 : 5 -> Остача: {c}")
print(f"7248 : 6 -> Остача: {d}")
print(f"7128 : 5 -> Остача: {e}")
print(f"19224 : 9 -> Остача: {f}")


# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

big_pizza_price = 274*4
middle_pizza_price = 218*2
juice = 35*4
cake = 350
water = 21*3
total_birthday_cost = big_pizza_price + middle_pizza_price + juice + cake + water
print(f"Задача 8: Скільки грошей знадобиться на день народження?")
print(f"Велика піца: {big_pizza_price} грн")
print(f"Середня піца: {middle_pizza_price} грн")
print(f"Сік: {juice} грн")
print(f"Торт: {cake} грн")
print(f"Вода: {water} грн")
print(f"Загальна сума: {total_birthday_cost} грн\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

all_photo = 232
one_page = 8
total_page = all_photo//one_page

print(f"Задача 9: Скільки сторінок потрібно для фотоальбому?")
print(f"Загальна кількість фото: {all_photo}")
print(f"На одній сторінці вміщується: {one_page} фото")
print(f"Необхідно сторінок: {total_page}\n")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

fuel_tank = 48
distance = 1600
fuel_per_100km = 9

#1
total_fuel_needed = (distance / 100) * fuel_per_100km
#2
refuel_count = total_fuel_needed / fuel_tank

print(f"Задача 10: Скільки бензину потрібно для поїздки з Харкова в Будапешт?")
print(f"Загальна відстань: {distance} км")
print(f"Витрати пального: {fuel_per_100km} л на 100 км")
print(f"Необхідно пального: {total_fuel_needed:.2f} л")
print(f"Місткість бака: {fuel_tank} л")
print(f"Мінімальна кількість заправок: {int(refuel_count)}\n")

