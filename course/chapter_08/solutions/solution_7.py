start = (10.5, 22.7)
n= input()
s= n-start
v= n+start
if n == start:
    print("Вы находитесь в начальной точке маршрута")
if n > start:
    print(s)
if n < start:
    print(v)