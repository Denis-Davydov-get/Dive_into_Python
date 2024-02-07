from collections import OrderedDict

# специальные возможности
NEW_DICT = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
# переносит ключ переносит элемент с указанным в конец,
# если last=True, и в начало, если last=False
NEW_DICT.move_to_end('b', last=True)
print(NEW_DICT)
# удаляет последний элемент если last=True, и первый, если last=False
res = NEW_DICT.popitem(last=True)
print(res)  # ('b', 2_type_data)
print(NEW_DICT)  # OrderedDict([('a', 1_base), ('c', 3_array)])
