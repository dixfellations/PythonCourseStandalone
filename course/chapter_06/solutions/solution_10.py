n = int(input())
s = [[0] * n for _ in range(n)]
for l in range((n + 1) // 2):
    for i in range(l, n - l):
        s[l][i] = l + 1 
        s[n - l - 1][i] = l + 1
    for j in range(l, n - l):
        s[j][l] = l + 1 
        s[j][n - l - 1] = l + 1 
for row in s:
    print(" ".join(str(num) for num in row))
