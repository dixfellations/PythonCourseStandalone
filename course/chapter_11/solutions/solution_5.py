emails = []
while True:
    line = input().strip()
    if not line:
        break
    emails = []
    domain_part, users_part = line.split(':')
    domain = domain_part.strip()
    users = users_part.strip().split()
    for user in users:
        email = f"{user}@{domain}"
        emails.append(email)
for email in sorted(emails):
    print(email)