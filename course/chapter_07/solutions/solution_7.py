numbers = [5, 10, 15, 20, 25, 30, 35, 40]
sum_numbers = 0
count = len(numbers)
for number in numbers:
    sum_numbers += number
s = sum_numbers / count
print("Среднее арифметическое:", s)
