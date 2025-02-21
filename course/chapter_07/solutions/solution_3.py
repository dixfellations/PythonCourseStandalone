numbers = [3, 17, 6, 12, 9, 21, 5]
max = numbers[0]
min = numbers[0]
for i in numbers:
    if i > max:
        max = i
    if i < min:
        min = i
print("Максимальный элемент:",max)