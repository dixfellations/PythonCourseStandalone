numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
e_numbers = []
o_numbers = []
for n in numbers:
    if n % 2 == 0:
        e_numbers.append(numbers)
    else:
        o_numbers.append(numbers)
print(", ".join(map(str, e_numbers)))
print(", ".join(map(str, o_numbers)))