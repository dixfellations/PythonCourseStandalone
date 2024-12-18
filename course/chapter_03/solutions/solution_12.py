num=30
N=True
for i in range(5):
    n=int(input())
    if n==num:
        N=False
        print("Поздравляем! Вы угадали число.")
        break
    if n>num:
        print("Загаданное число меньше.")
    if n<num:
        print("Загаданное число больше.")
if N:
    print("Попытки закончились")