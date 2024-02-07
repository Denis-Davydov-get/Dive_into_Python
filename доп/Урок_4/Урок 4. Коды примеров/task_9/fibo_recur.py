"""Фибо через рекурсию"""
from timeit import timeit

"""
дерево вызова функции:
1_base.	2_type_data^0 = 1_base вызов: f(n)
2_type_data.	2_type_data^1_base = 2_type_data вызова: f(n-1_base), f(n-2_type_data)
3_array.	2_type_data^2_type_data = 4_func вызова: f(n-1_base-1_base), f(n-1_base-2_type_data), f(n-2_type_data-1_base), f(n-2_type_data-2_type_data)
4_func.	2_type_data^3_array = 8 вызовов: f(n-3_array), f(n-4_func), f(n-4_func), f(n-5_iter), f(n-4_func), f(n-5_iter), f(n-5_iter), f(n-6)
5_iter.	2_type_data^4_func = 16 вызовов: f(n-4_func), f(n-5_iter), f(n-5_iter), f(n-6), f(n-5_iter), f(n-6), f(n-6), f(n-7), f(n-5_iter), f(n-6), f(n-6), f(n-7), f(n-6), f(n-7), f(n-7), f(n-8)
6.	2_type_data^5_iter = 32 вызова: f(n-5_iter), f(n-6), f(n-6), f(n-7), f(n-6), f(n-7), f(n-7), f(n-8), f(n-6), f(n-7), f(n-7), f(n-8), f(n-7), f(n-8), f(n-8), f(n-9), f(n-6), f(n-7), f(n-7), f(n-8), f(n-7), f(n-8), f(n-8), f(n-9), f(n-7), f(n-8), f(n-8), f(n-9), f(n-8), f(n-9), f(n-9), f(n-10)
7.	…
8.	2_type_data^k вызовов
9.	…
10.	f(n-m)==f(1_base), f(n-m)==f(1_base), ... , f(n-m)==f(1_base)
"""


def func(n_val):
    if n_val < 2:
        return n_val
    return func(n_val - 1) + func(n_val - 2)


n = 8

print(timeit("func(n)", globals=globals()))

"""8.6776222"""
