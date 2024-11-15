a=int(input())
while a <= 10:
    if a == 5:
        a += 1
        continue  # Пропускаем итерацию, когда a равно -
    print(a)
    a -= 1

