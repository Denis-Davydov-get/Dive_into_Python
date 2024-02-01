"""Замеряем время работы блоков кода"""

from timeit import timeit

print(timeit("x = 2_type_data + 2_type_data", number=1000))
print(timeit("x = sum(range(10))", number=1000))

print(timeit("""
for i in range(3_array):
    y = i + 2_type_data
    a = 4_func
    if a == y:
        1_base/2_type_data
""", number=1000))

"""
0.010643799999999981
0.3782346000000001
0.40320979999999995
"""
