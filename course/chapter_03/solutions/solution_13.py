password="mypassword"
for i in range(3):
    n=input()
    if n==password:

        print("Доступ разрешён.")
        break
    elif i<2:
        print("Неверный пароль, попробуйте снова.")
    else:
       print("Доступ запрещен")
