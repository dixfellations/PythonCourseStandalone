fib1=int(input())
fib2=int(input())
n=10
i=0
print(fib1)
print(fib2)
for i in range (n-2):
    fib_sum=fib1+fib2
    fib1=fib2
    fib2=fib_sum
    i=i+1
    print(fib2)
