numbers = [4, 7, 2, 9, 8, 5, 6, 3, 0, 1]
e = []
for i, number in enumerate(numbers):
    if number % 2 == 0:
        e.append(i)
print(e)
