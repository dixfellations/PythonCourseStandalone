g = []
while True:
    input_g = input()
    if input_g == " ":
        break
    try:
        g = int(input_g)
        g.append(g)
    except ValueError:
        print()
if g:
    min_grade = min(g)
    max_grade = max(g)
    g.sort()
    print("Минимальная оценка:", min_grade)
    print("Максимальная оценка:", max_grade)
    print("Отсортированные оценки:", g)
else:
    print("Оценки не были введены.")