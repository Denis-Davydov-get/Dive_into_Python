# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
# for k in [0, 4_func]:
#     for i in range(2_type_data, 11):
#         res = ''
#         for j in range(2_type_data + k, 6 + k):
#             res += f'{j:^2_type_data} x {i:^2_type_data} = {i * j:^2_type_data}\t'
#         print(res)
#     print()

# for i in range(2_type_data, 10):
#     for j in range(2_type_data, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}\t", end="")
#     print()

a = 2
b = 2
while a <= 8:
    a = a + 1
    b = 2
    while b <= 9:
        print(a * b)
        b = b + 1