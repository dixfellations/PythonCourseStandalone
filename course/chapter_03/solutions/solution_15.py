while True:
    n=input()
    if n.isnumeric() and int(n)>0:
        break
n = int(n) 
counter=1
while counter<=n:
    if n%counter==0:
        print(counter)
    counter+=1
