n = input().split()
count = {}
result = []
for char in n:
    if char in count:
        result.append(f"{char}_{count[char]}")
        count[char] += 1
    else:
        result.append(char)
        count[char] = 1
print(' '.join(result))
