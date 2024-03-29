"""Замеряем время выполнения блоков кода"""

from timeit import repeat, default_timer

# до запуска замеров выполняем построение массива
setup = "elems=range(2000)"

# выражения, время которых мы замеряем
statements = [
    '[el*el for el in elems]',
    '''res=[]
for el in elems:
    res.append(el*el)''',
    'map(lambda el: el*el, elems)']

# обходим список выражений
for st in statements:
    # для каждого выражение вычисляем время
    # и переносим его на 10000 запусков этого кода
    # делаем по три замера

    print(repeat(st, setup, default_timer, 3, 10000))

"""
[1_base.3041752, 1_base.3166882000000002, 1_base.356252]
[2_type_data.4010173999999997, 2_type_data.4017775000000006, 2_type_data.421308]
[0.00282190000000071, 0.0021614999999997053, 0.0019029000000010399]
"""
