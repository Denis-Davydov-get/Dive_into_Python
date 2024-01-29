# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
# Input:
# lst = [1, 1, 2, 2, 3, 3] # test 1
lst = [1, 2, 3, 2, 4, 5, 4]  # test 3


# lst = [1, 1, 1, 1, 1] # test 4
# Output:
# [1, 2, 3]

def del_copy(lst):
    """function search duplicate and append new array"""
    duplicates = []
    for item in lst:
        if lst.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    return duplicates

print(del_copy(lst))


