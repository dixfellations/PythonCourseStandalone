n=int(input())
invait=input()
if  (n>=18) and (invait== "Y"):
    print("Добро пожаловать в клуб!")
elif (0 <= n <18)  or (invait == "N"): 
    print("Извините, вход запрещен.")
else :
    print("Введите корректные значения.")


    