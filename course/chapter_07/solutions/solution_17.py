ielements = input()
elements = ielements.split()
elements = [int(x) for x in elements]
n = int(input())
new_list = elements[0::n]
sorted_list = sorted(new_list)
print(sorted_list)