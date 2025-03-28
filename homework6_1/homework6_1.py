s = input("Enter something: ")
unique_chars = len(set(s))
if unique_chars >= 10:
    print(True)
else:
    print(False)
