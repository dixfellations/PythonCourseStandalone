v= input().split()
res= {}
for name in v:
    res[name] = res.get(name, 0) + 1
for name, count in sorted(res.items()):
    print(f"{name}: {count}")