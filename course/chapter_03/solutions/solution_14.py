while True:
    n=input("Введите пложительное целое число:")
    if n.isnumeric() and int(n)>0:
        break
sum_of_digits=sum(int(digit) for digit in n)
print(n)
print(sum_of_digits)