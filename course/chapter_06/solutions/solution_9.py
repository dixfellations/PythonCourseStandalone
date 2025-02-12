# Ввод высоты и ширины прямоугольника
h= int(input())
w = int(input())
max_number = h * w
c_w = len(str(max_number)) + 1
for i in range(h):
    for j in range(w):
        number = i + j * h + 1
        print(f"{number:<{c_w}}", end="")
    print()
