'''
У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой,
выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
deposit(amount): Пополнение счёта.
withdraw(amount): Снятие денег.
exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

Пополнение счета:
Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму.
Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

Снятие средств:
Функция withdraw(amount) позволяет клиенту снимать средства со счета.
Сумма снятия также должна быть кратной MULTIPLICITY.
При снятии средств начисляется комиссия в процентах от снимаемой суммы,
которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

Завершение работы:
Функция exit() завершает работу с банковским счетом.
Перед завершением, если на счету больше RICHNESS_SUM,
начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

Проверка кратности суммы:
Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY.
Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.
Input:
deposit(10000)
withdraw(4000)
exit()

Print(operations)
Output:
 ['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']

'''
import decimal

MULTIPLICITY = 50  # Сумма снятия должна быть кратной этой переменной
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)  # процент за снятие
MIN_REMOVAL = decimal.Decimal(30)  # минимальное снятие
MAX_REMOVAL = decimal.Decimal(600)  # максимальное снятие
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)  # % депозита
COUNTER4PERCENTAGES = 3  # счетчик процента
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)  # налог на богатство
RICHNESS_SUM = decimal.Decimal(10_000_000)  # если на счету больше

bank_account = decimal.Decimal(0)  # банковский счет
count = 0  # сумма операции
operations = []  # Совершенные операции


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
    if amount * PERCENT_REMOVAL > MAX_REMOVAL: # если сумма снятия с комиссией больше макс. возможной
        temp_percent_removal = MAX_REMOVAL
    elif amount * PERCENT_REMOVAL < MIN_REMOVAL:
        temp_percent_removal = MIN_REMOVAL
    else:
        temp_percent_removal = amount * PERCENT_REMOVAL
    if bank_account >= (amount + temp_percent_removal):
        if check_multiplicity(amount):
            bank_account -= amount + temp_percent_removal
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {temp_percent_removal // 1} у.е.. '
                              f'Итого {bank_account // 1} у.е. Возьмите карту на которой {bank_account} у.е.')
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


deposit(1000)
withdraw(200)
exit()

print(operations)
