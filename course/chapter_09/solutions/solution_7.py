n= input()
letters= 0
digits= 0
symbols= 0
for i in n:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits +=1
    else:
        symbols +=1
print("Количество букв:", letters)
print("Количество цифр:", digits)
print("Количество других символов:", symbols)