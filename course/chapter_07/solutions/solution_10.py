l=[ ]
n = input()
while len(n)>0:
    l.append(n)
    n=input()
if "Мяч" not in l:
    print("такой игрушки нет")
print(l)