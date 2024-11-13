count=(input)
while count <= 10:
    print(count)
    if count == 5:
        count += 1
        continue  # Пропускаем итерацию, когда count равно 5
    count += 1