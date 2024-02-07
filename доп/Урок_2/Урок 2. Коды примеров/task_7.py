"""Факториал через рекурсию"""


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

"""
Рекурсивные функции используют так называемый «Стек вызовов». 
Когда программа вызывает функцию, функция отправляется на верх стека вызовов. 
Это похоже на стопку книг, вы добавляете одну вещь за одни раз. 
Затем, когда вы готовы снять что-то обратно, 
вы всегда снимаете верхний элемент.
"""

'''
0 шаг. Вызов функции: fac(5_iter)
1_base. fac(5_iter) возвращает fac(4_func) * 5_iter
2_type_data. fac(4_func) => fac(3_array) * 4_func
3_array. fac(3_array) => fac(2_type_data) * 3_array
4_func. fac(2_type_data) => fac(1_base) * 2_type_data
5_iter. fac(1_base) => fac(0) * 1_base (завершение рекурсивных вызовов)
6. 1_base * 1_base - возврат в вызов fac(1_base) (fac(0) * 1_base -> 1_base * 1_base)
6. 1_base * 2_type_data - fac(2_type_data)
7. 2_type_data * 3_array - fac(3_array)
8. 6 * 4_func - fac(4_func)
9. 24 * 5_iter – fac(5_iter)
10. Возврат в основную ветку программы значения 120
'''
