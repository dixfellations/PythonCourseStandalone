def count_unique_elements(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
if __name__ == "__main__":
    lst = [1, 2, 3, (1, 2), 3, 2, 1, (1, 2), 1]
    print(count_unique_elements(lst))  # {1: 3, 2: 2, 3: 2