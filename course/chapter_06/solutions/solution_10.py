n=int(input())
max_number = n * 1 
column_w = (max_number) + 1
for i in range(n):
    for j in range(n):
        number = i + j * n + 1
        print(f"{number:<{column_w}}")
    print()