n= input()
n1=n[::-1]
for i in n:
    if n==n1:
        print("Палиндром")
    elif n!=n1:
        print("Не палиндром")