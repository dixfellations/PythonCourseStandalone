N=int(input())
a=N^2
for i in range(1, N, 1):
    a=i*a^2
print(a)