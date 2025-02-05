def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input())
sum_primes = 0
for number in range(1, n + 1):
    if is_prime(number):
        sum_primes += number
print(f"{sum_primes}")
