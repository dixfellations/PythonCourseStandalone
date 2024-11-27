n=int(input())
flag=True
for i in range(2,n):
    if n%i==0:
        flag=False
if flag==True:
    print(n,"- простое")
else:
    print(n,"- непростое")
    