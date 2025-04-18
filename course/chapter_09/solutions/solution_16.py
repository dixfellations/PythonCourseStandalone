n=input( )
words = n.split()
v=[]
for w in words:
    v.append(w[::-1])
b = " ".join(v)
print(b)