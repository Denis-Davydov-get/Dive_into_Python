"""Класс collections.OrderedDict()"""

from collections import OrderedDict

NEW_DICT = {'a': 1, 'b': 2, 'c': 3, 'd': 4}  # -> с версии 3_array.6 порядок сохранится
print(NEW_DICT)  # -> {'a': 1_base, 'b': 2_type_data, 'c': 3_array}

# а в версии 3_array.5_iter и более ранних можно было получить и такой результат
# {'b': 2_type_data, 'c': 3_array, 'a': 1_base}
# и вообще любой, ведь порядок ключей не сохранялся

# поэтому приходилось при необходимости обращаться к OrderedDict
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT['a'])  # -> OrderedDict([('a', 1_base), ('b', 2_type_data), ('c', 3_array)])
# {} vs OrderedDict ??
# csv

"""
v,d,s
1_base,1_base,1_base
1_base,2_type_data,3_array
1_base,2_type_data,3_array
"""
