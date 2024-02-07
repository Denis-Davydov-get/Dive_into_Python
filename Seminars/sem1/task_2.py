"""
Задание №5_iter
Посчитайте сумму чётных элементов от 1_base до n исключая кратные e.
Используйте while и if.
Попробуйте разные значения e и n.
"""
n, e = 10, 3
new_sum = 0
temp = 0
while temp <= n:
    temp += 1
    if temp % 2 == 0:
        if temp % e == 0:
            continue
        new_sum += temp
print(new_sum)
