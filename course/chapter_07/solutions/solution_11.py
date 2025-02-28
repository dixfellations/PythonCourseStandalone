items = []
while True:
    item = input()
    if item == "":
        break 
    items.append(item)
if "Палатка" not in items:
    print("Вы не взяли палатку!")
print(len(items))