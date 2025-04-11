n = input().strip()
result = ""
for char in n:
    if not char.isdigit():
        result += char
print(result)