n_str= input().split()
n= []
for num in n_str:
    n.append(int(num))
target= int(input())
found= False
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] + n[j] == target:
            print((n[i], n[j]))
            found = True
            exit()
if not found:
    print(target)