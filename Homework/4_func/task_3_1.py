# Задача о банкомате

# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, выполняя
# следующие операции, для выполнения которых необходимо написать следующие функции:
#
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.
#
# Пополнение счета:
#
# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. Пополнение счета
# возможно только на сумму, которая кратна MULTIPLICITY.
#
# Снятие средств:
#
# Функция withdraw(amount) позволяет клиенту снимать средства со счета. Сумма снятия также должна быть
# кратной MULTIPLICITY. При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая
# может варьироваться от MIN_REMOVAL до MAX_REMOVAL.
#
# Завершение работы:
#
# Функция exit() завершает работу с банковским счетом. Перед завершением, если на счету больше RICHNESS_SUM,
# начисляется налог на богатство в размере RICHNESS_PERCENT процентов.
#
# Проверка кратности суммы:
#
# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

import decimal
import random

MULTIPLICITY = 50  # ✔
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # ✔
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


# Введите ваше решение ниже
def check_multiplicity(count):  # готово
    '''Проверка кратности суммы, кратна ли сумма amount заданному множителю MULTIPLICITY, при пополнении и снятии.'''
    if count % MULTIPLICITY == 0:
        return True
    return False


def deposit(count):  # готово
    ''' Пополнение счёта.'''
    global bank_account
    global operations
    if check_multiplicity(count):
        bank_account += count
        operations.append(f"Пополнение карты на {count} у.е. Итого {bank_account} у.е.")
        return operations
    return f'Сумма должна быть кратной {MULTIPLICITY} у.е.'


def withdraw(amount):
    '''Снятие денег.'''
    global bank_account
    global operations
    if amount * PERCENT_REMOVAL > MAX_REMOVAL:
        temp_percent_removal = MAX_REMOVAL
    elif amount * PERCENT_REMOVAL < MIN_REMOVAL:
        temp_percent_removal = MIN_REMOVAL
    else:
        temp_percent_removal = amount * PERCENT_REMOVAL
    if bank_account >= (amount + temp_percent_removal):
        if check_multiplicity(amount):
            bank_account -= amount + temp_percent_removal
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {temp_percent_removal // 1} у.е.. '
                              f'Итого {bank_account // 1} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {(amount + temp_percent_removal) // 1} у.е. На карте '
            f'{bank_account} у.е. Возьмите карту на которой {bank_account} у.е.')


def exit():
    '''Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях'''
    global bank_account
    global operations
    if RICHNESS_SUM < bank_account:
        commission_rich = bank_account * RICHNESS_PERCENT
        bank_account -= commission_rich
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT} в сумме {commission_rich} у.е. Итого {bank_account} у.е.')
        return operations
    return operations


deposit(10000)
withdraw(4000)
exit()

print(operations)


# ['Пополнение карты на 1000 у.е. Итого 1000 у.е.', 'Снятие с карты 200 у.е. Процент за снятие 30 у.е.. Итого 770 у.е.', 'Возьмите карту на которой 770 у.е.']