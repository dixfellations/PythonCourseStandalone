h= int(input())
w = int(input())
max_n = h * w
cw = len(str(max_n)) + 1
for i in range(h):
    for j in range(w):
        n = i + j * h + 1
        print(f"{n:<{cw}}", end="")
    print()