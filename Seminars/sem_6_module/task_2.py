
from random import randint
def guess_the_number_attempts(bottom_line, footer_line, number_of_attempts):
    random_num = randint(bottom_line, footer_line)
    while number_of_attempts > 0:
        user_num = int(input(("Введите номер: ")))
        if user_num > random_num:
            print("меньше")
            number_of_attempts -= 1
            continue
        elif user_num < random_num:
            print("больше")
            number_of_attempts -= 1
            continue
        elif user_num == random_num:
            print("Вы угадали")
            return True
    print("У вас кончились попытки")
    return False


bottom_line = int(input("Введите нижнее значение: "))
footer_line = int(input("Введите верхнее значение: "))
number_of_attempts = int(input("Введите количество попыток: "))
guess_the_number_attempts(bottom_line, footer_line, number_of_attempts)
