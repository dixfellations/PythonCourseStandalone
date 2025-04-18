text = input()
words = text.split()
v=[]
for w in words[::-1]:
    v.append(w)
b = " ".join(v)
print(b)