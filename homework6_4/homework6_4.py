numbers = [1,2,3,4,5,6,7,8,9,10]
paired_numbers = []
for item in numbers:
    if item % 2 == 0:
        paired_numbers.append(item)
print(sum(paired_numbers))