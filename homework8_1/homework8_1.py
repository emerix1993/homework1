def numbers(s):
    try:
        symbols = [int(num) for num in s.split(',')]
        return sum(symbols)
    except ValueError:
        return "Не можу це зробити"


strings = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

results = [numbers(s) for s in strings]

for result in results:
    print(result)
