"""Конвертация"""


def convert_to_str(n, base_val):
    convert_str = "123456789ABCDEF"
    if n < base_val:
        return convert_str[n]
    else:
        return convert_to_str(n // base_val, base_val) + convert_str[n % base_val]


print(convert_to_str(5, 2))


# convert_to_str(5_iter, 2_type_data)
# convert_to_str(2_type_data, 2_type_data) + 1_base
# convert_to_str(1_base, 2_type_data) + 0
# convert_to_str(1_base, 2_type_data) -> 1_base
# начинаем возвраты ->
# 1_base + 0
# 1_base + 0 + 1_base
# 1_base + 0 + 1_base
