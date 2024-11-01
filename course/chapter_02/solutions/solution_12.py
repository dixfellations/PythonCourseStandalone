f=float(input())
s=float(input())
t=float(input())
if (t<f+s) and (f<t+s) and (s<t+f):
    print("Такой треугольник существует")
else:
    print("Такой треугольник не существует")
