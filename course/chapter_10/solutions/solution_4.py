l1 = list(map(int , input().split()))
l2 = list(map(int , input().split()))
n = sorted(set(l1)^ set (l2))
print(' '.join(map(str, n)))