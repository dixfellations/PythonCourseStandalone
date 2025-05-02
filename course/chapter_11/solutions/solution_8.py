d = {}
while True:
    s = input().strip()
    if not s:
        break
    name, books = s.split(':', 1)
    name = name.strip()
    books = [b.strip() for b in books.split(',')]
    d[name] = books