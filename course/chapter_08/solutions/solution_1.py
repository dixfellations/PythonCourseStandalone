names = ('Иван', 'Ольга', 'Мария', 'Анна')
n= input()
for i in n:
    index = names.index(n)
    print(f"'{n}': {index}")
    break
