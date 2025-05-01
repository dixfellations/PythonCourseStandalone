for _ in range(3):
    lines = [list(map(int, input().split()))] 
count = {}
for row in lines:
    for x in row:
        count[x] = count.get(x, 0) + 1
for row in lines:
    uniq = sorted(x for x in row if count[x] == 1)
    print(' '.join(map(str, uniq)) if uniq else '')