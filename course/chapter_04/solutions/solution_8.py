fib1=1
fib2=1
n=input()
n=int(n)
i=0
print("Числа Фибоначчи:")
print(fib1)
print(fib2)
for i in range (n-2):
    fib_sum=fib1+fib2
    fib1=fib2
    fib2=fib_sum
    i=i+1
    print(fib2)