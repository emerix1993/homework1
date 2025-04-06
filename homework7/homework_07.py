# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if result > 25:
            break
            # Enter the action to take if the result is greater than 25
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def sum_of_two_numbers(sum1: int, sum2: int) -> int:
    total_sum = sum1 + sum2
    return total_sum


print(sum_of_two_numbers(10, 20))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def arithmetic_mean(a: int, b: int, c: int) -> float:
    result = (a + b + c) / 3
    return result


print(arithmetic_mean(1, 20, 6))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reverse(text: str) -> str:
    return text[::-1]


print(reverse("hello world"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word(a: str, b: str, c: str, d: str) -> str:
    words = [a, b, c, d]
    return max(words, key=len)


print(longest_word("github", "python", "pycharm", "sqlalchemy"))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1


# task 7
# Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук
def quantity(apples: int) -> int:
    banana = apples * 4
    return banana


print("Bananas:", quantity(3))


# task 8
def calculate_pages(all_photos: int, photos_per_page: int) -> int:
    return (all_photos + photos_per_page - 1) // photos_per_page


all_photo = 232
one_page = 8

total_page = calculate_pages(all_photo, one_page)

print(f"Задача 9: Скільки сторінок потрібно для фотоальбому?")
print(f"Загальна кількість фото: {all_photo}")
print(f"На одній сторінці вміщується: {one_page} фото")
print(f"Необхідно сторінок: {total_page}\n")


# task 9
def sum_of_even_numbers(numbers: list) -> int:
    return sum(number for number in numbers if number % 2 == 0)


numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum = sum_of_even_numbers(numbers_list)

print(f"Сума парних чисел: {total_sum}")


# task 10
def filter_strings(lst: list) -> list:
    return [item for item in lst if isinstance(item, str)]


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

lst2 = filter_strings(lst1)

print(lst2)
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
