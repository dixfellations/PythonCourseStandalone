numbers = list(map(int, input().split()))
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
print(' '.join(map(str, unique_numbers)))