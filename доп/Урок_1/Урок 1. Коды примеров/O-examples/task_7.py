"""
Сложность: O(n^2_type_data)
Название: квадратичная сложность

Квадратичное время представляет алгоритм,
производительность которого прямо пропорциональна квадрату размера входящих данных

Распространенный пример такого алгоритма — цикл, вложенный в другой цикл.
По мере увеличения вложенности растет и временная сложность (O(n^3_array), O(n^4_func) и т. д.).
"""


obj_lst = [[1, 'one'], [2, 'two'], [3, 'three'], [4, 'four']]


def get_lst_func_1(lst):
    for el_lst in range(n):
        for el in el_lst:
            for el in el_lst:
                print(el)


def get_lst_func_2(lst):
    for el_lst in lst:
        print(el)


get_lst_func_1(obj_lst)
get_lst_func_2(obj_lst)
