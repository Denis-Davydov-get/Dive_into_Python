# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов
num = 5
figure = '*'
space = ' '
num_space = num - 1
num_figure = 1
for _ in range(num):
    print((space * num_space) + (figure * num_figure) + (space * num_space))
    num_figure += 2
    num_space -= 1