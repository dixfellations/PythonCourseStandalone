i = input( ).strip()
words = i.split()
a = [ ]
for word in words :
    if len(word) <= 2:
        a.append(word)
    else:
        new_word = word[0] + word[-1]
        a.append(new_word)
result = ' '.join(a)
print(f"Результат: {result}")