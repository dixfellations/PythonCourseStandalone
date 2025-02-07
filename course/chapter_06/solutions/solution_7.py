ts = 1000
for a in range(1, ts// 3):
    for b in range(a + 1, ts // 2):
        c = ts - a - b
        if a**2 + b**2 == c**2:
            print(a, b, c)