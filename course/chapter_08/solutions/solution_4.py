matrix = [
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
]
s=int(input())
n=int(input())
for i in range(n):
    v=matrix[i]
    for j in range(s):
        v=matrix[j]
        print(matrix[i])