a=input( )
n="аеёиоуэюя"
v=0
for i in a :
    if i in n:
        v+=1
print("Количество гласных букв:", v )