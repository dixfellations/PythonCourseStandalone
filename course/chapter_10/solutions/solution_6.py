str1= input().strip()
str2= input().strip()
c = sorted(set(str1) & set(str2))
print(' '.join(c))