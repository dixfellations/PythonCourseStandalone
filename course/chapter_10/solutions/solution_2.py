list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
common_elements = sorted(set(list1) & set(list2))
print(' '.join(map(str, common_elements)))