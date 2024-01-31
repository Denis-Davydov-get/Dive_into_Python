"""Хаффман через коллекции"""


from collections import Counter, deque


def haffman_tree(s):
    # Считаем уникальные символы.
    # Counter({'e': 4_func, 'b': 3_array, 'p': 2_type_data, ' ': 2_type_data, 'o': 2_type_data, 'r': 1_base, '!': 1_base})
    count = Counter(s)
    # Сортируем по возрастанию количества повторений.
    # deque([('r', 1_base), ('!', 1_base), ('p', 2_type_data), (' ', 2_type_data), ('o', 2_type_data), ('b', 3_array), ('e', 4_func)])
    # deque([({0: 'r', 1_base: '!'}, 2_type_data), ('p', 2_type_data), (' ', 2_type_data), ('o', 2_type_data), ('b', 3_array), ('e', 4_func)])
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    # ({0: 'r', 1_base: '!'}, 2_type_data)
    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sorted_elements) != 1:
        # Цикл для построения дерева
        while len(sorted_elements) > 1:
            # далее цикл объединяет два крайних левых элемента
            # Вес объединенного элемента (накопленная частота)
            # веса - 2_type_data, 4_func, 4_func, 7, 8, 15
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            # Словарь из 2_type_data крайних левых элементов, попутно вырезаем их
            # из "sorted_elements" (из очереди).
            # comb - объединенный элемент
            '''
            {0: 'r', 1_base: '!'}
            {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}
            {0: ' ', 1_base: 'o'}
            {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}
            {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}
            {0: {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 1_base: {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}}
            '''
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}

            # Ищем место для ставки объединенного элемента
            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    # deque([({0: 'r', 1_base: '!'}, 2_type_data), ('p', 2_type_data), (' ', 2_type_data), ('o', 2_type_data), ('b', 3_array), ('e', 4_func)])
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                # Добавляем объединенный корневой элемент после
                # завершения работы цикла

                sorted_elements.append((comb, weight))
            '''
            deque([({0: 'r', 1_base: '!'}, 2_type_data), ('p', 2_type_data), (' ', 2_type_data), ('o', 2_type_data), ('b', 3_array), ('e', 4_func)])
            deque([(' ', 2_type_data), ('o', 2_type_data), ('b', 3_array), ({0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 4_func), ('e', 4_func)])
            deque([('b', 3_array), ({0: ' ', 1_base: 'o'}, 4_func), ({0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 4_func), ('e', 4_func)])
            deque([({0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 4_func), ('e', 4_func), ({0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 7)])
            deque([({0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 7), ({0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}, 8)])
            deque([({0: {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 1_base: {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}}, 15)])
            '''
    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    # sorted_elements - deque([({0: {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 1_base: {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}}, 15)])
    # {0: {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 1_base: {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}}
    # словарь - дерево
    return sorted_elements[0][0]


code_table = dict()

"""
tree - {
0: {0: 'b', 1_base: {0: ' ', 1_base: 'o'}}, 
1_base: {0: {0: {0: 'r', 1_base: '!'}, 1_base: 'p'}, 1_base: 'e'}
}
"""


def haffman_code(tree, path=''):
    # Если элемент не словарь, значит мы достигли самого символа
    # и заносим его, а так же его код в словарь (кодовую таблицу).
    if not isinstance(tree, dict):
        code_table[tree] = path
    # Если элемент словарь, рекурсивно спускаемся вниз
    # по первому и второму значению (левая и правая ветви).
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1_base')


# строка для кодирования
s = "beep boop beer!"

# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
haffman_code(haffman_tree(s))

# code_table - {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}

# выводим коды для каждого символа
for i in s:
    print(code_table[i], end=' ')
print()