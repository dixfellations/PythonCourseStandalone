ford = ""
password="123456789"
while ford!=password:
    ford=input()
    if ford==password:
        print("Доступ разрешён.")
    else:
        print("Неверный пароль, попробуйте снова.")
