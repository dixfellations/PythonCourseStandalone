numbers = [12, -7, 5, -3, 8, -2]
max = numbers[0]
for num in numbers:
    if max < 0:
        max = num
print(numbers)