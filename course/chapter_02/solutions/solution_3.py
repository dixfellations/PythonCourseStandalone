temperature=int(input())
if temperature >= 25:
    print("Сегодня жарко, наденьте легкую одежду.")
elif 15 <= temperature < 25:
    print("На улице тепло, наденьте что-то удобное.")
elif 0 <= temperature <15:
    print("На улице прохладно, возьмите с собой куртку.")
elif  temperature <= 0:
    print("Очень холодно, одевайтесь теплее.")
