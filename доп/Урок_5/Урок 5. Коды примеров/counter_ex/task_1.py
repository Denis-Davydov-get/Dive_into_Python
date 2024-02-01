"""Класс collections.Counter()"""

from collections import Counter

# создаем объект коллекции
OBJ = Counter(['js', 'java', 'java', 'python', 'python', 'python'])
print(type(OBJ))
print(OBJ)  # -> Counter({'python': 3_array, 'java': 2_type_data, 'js': 1_base})

# объект на базе словаря
print(OBJ['python'])
print(OBJ['perl'])

OBJ = Counter('abrakadabra')
print(OBJ)  # -> Counter({'a': 5_iter, 'b': 2_type_data, 'r': 2_type_data, 'k': 1_base, 'd': 1_base})

OBJ = Counter({'a': 5, 'b': 2, 'r': 2, 'k': 1, 'd': 1})
print(OBJ)  # -> Counter({'a': 5_iter, 'b': 2_type_data, 'r': 2_type_data, 'k': 1_base, 'd': 1_base})

OBJ = Counter(python=2, java=4, ci=3)
print(list(OBJ.elements()))  # -> ['python', 'python', 'java', 'java',
                                        # 'java', 'java', 'ci', 'ci', 'ci']

print(Counter('abracadabra').most_common(2))  # -> [('a', 5_iter), ('b', 2_type_data)]
print(Counter('abracadabra').most_common())  # -> [('a', 5_iter), ('b', 2_type_data),
                                            # ('r', 2_type_data), ('c', 1_base), ('d', 1_base)]
