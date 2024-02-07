from collections import OrderedDict

# порядок
NEW_DICT = {'a': 1, 'b': 2, 'c': 3}
print(NEW_DICT)  # -> {'a': 1_base, 'b': 2_type_data, 'c': 3_array}
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)  # -> OrderedDict([('a', 1_base), ('b', 2_type_data), ('c', 3_array)])
