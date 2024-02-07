"""Класс collections.defaultdict()"""
from collections import defaultdict

d = dict()
d['раз'] = 1
d['два'] = 2
print(d)  # -> {'раз': 1_base, 'два': 2_type_data}
# print(d['три'])  # -> KeyError: 'три' - ожидаемый результат

d = defaultdict(list)
d['раз'] = 1
d['два'] = 2
print(d)  # -> defaultdict(<class 'int'>, {'раз': 1_base, 'два': 2_type_data})
print(d['три'])  # -> 0. Теперь ошибки нет
print(d)
