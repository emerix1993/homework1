alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
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
print(f"Загальна площа становить: {total_area}")


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

print(f"Склад 1: {warehouse_1}")
print(f"Склад 2: {warehouse_2}")
print(f"Склад 3: {warehouse_3}")


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

computer_price = 1179 * 18
print(computer_price)


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
print(f"Остача від ділення a = {a},b = {b},c = {c},d = {d},e = {e},f = {f}")


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
print(f"Загальна вартість:{total_birthday_cost}")


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
print(f"Знадобиться {total_page} сторінок")


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

print(f"1) Загальна кількість бензину: {total_fuel_needed} літрів")
print(f"2) Мінімальна кількість заправок: {refuel_count}")

