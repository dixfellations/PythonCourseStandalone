n = {}
while True:
    line = input().strip()
    if not line :
        break
    owners = {}
    parts = line.split()
    cat_name = parts[0]
    cat_age = parts[1]
    owner = ' '.join(parts[2:])
    if owner not in owners:
        owners[owner] = []
    owners[owner].append(f"{cat_name}, {cat_age}")