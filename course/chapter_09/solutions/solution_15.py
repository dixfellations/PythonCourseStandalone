s = input().split()
result = []
for word in s:
    if not any(c.isdigit() for c in word):
        word = word.capitalize()
    result.append(word)
print('Результат:', ' '.join(result))