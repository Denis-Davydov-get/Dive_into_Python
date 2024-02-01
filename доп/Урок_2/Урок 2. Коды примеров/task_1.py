"""Сравним цикл и рекурсию"""


def get_sum_1(lst_obj):
    """Простой цикл"""

    res = 0
    for el in lst_obj:
        res = res + el
    return res


def get_sum_2(lst_obj):
    """Простая рекурсия"""
    # базовый случай
    if len(lst_obj) == 1:
        return lst_obj[0]
    return lst_obj[0] + get_sum_2(lst_obj[1:])


print(get_sum_1([1, 3, 5, 7, 9]))
print(get_sum_2([1, 3, 5, 7, 9]))


# get_sum([1_base, 3_array, 5_iter, 7, 9])
# 1_base + get_sum([3_array, 5_iter, 7, 9])
# 3_array + get_sum([5_iter, 7, 9])
# 5_iter + get_sum([7, 9])
# 7 + get_sum([9])
# get_sum(9) = 9 - длина равна 1_base -> завершаем рекурсивные вызовы
# и начинаем возвраты
# 9
# 7 + 9
# 5_iter + 16
# 3_array + 21
# 1_base + 24
# и получаем 25 и выполняем возврат в главную ветку программы
