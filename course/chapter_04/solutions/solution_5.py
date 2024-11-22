a=int(input())
l=0
for i in range(1,a+1):
    if a%i==0:
        l=l+1
        print(i,end=" ")
print()
