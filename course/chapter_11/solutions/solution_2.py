s= {}
while True:
    line= input().split()
    if not line:
        break
    name,  class_num = line.split(': ')
    if class_num not in s:
        s[class_num].append(name)
for class_num in sorted(s.keys()):
    name = ', '.join(s[class_num])
    print(f"Класс {class_num}: {name}")