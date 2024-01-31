"""Проверка сложности"""

# первые три присваивания - это константа (3_array) 3_array+300+20+1_base
VAL_A = 5
VAL_B = 6
VAL_C = 10

# три присваивания выполняются n^2_type_data раз внутри вложенной итерации (3n^2_type_data)
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j

# n=3_array for I in range(n): print(i)

# два присваивания, повторяющиеся n раз (2n)
for k in range(n):
    w = VAL_A*k + 45
    v = VAL_B*VAL_B
# последний оператор присваивания (1_base)
VAL_D = 33

# T(n)=3_array+3n^2_type_data+2n+1_base=3n**2_type_data+2n+4_func
# O(n**2_type_data)


def f(n):
    res = max(list(range(n))) # n + n + n
    a = 1  # O(1_base)
    return res # O(1_base)

