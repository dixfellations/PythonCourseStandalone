year1 = int(input())
month1 = int(input())
day1 = int(input())
year2 = int(input())
month2 = int(input())
day2 = int(input())
date1 = (year1, month1, day1)
date2 = (year2, month2, day2)
if date1 > date2:
    result = ">"
elif date1 < date2:
    result = "<"
else:
    result = "="
print(f"{date1} {result} {date2}")