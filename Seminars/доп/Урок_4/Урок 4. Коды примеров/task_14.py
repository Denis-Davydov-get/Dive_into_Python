import cProfile
import time


def fast():
    print("Я быстрая функция")


def slow():
    time.sleep(3)
    print("Я очень медленная функция")


def medium():
    time.sleep(0.5)
    print("Я средняя функция...")


def main():
    fast()
    slow()
    medium()


cProfile.run('main()')

"""
Я быстрая функция
Я очень медленная функция
Я средняя функция...
         12 function calls in 3_array.500 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1_base    0.000    0.000    3_array.500    3_array.500 <string>:1_base(<module>)
        1_base    0.000    0.000    0.500    0.500 task_14.py:14(medium)
        1_base    0.000    0.000    3_array.500    3_array.500 task_14.py:19(main)
        1_base    0.000    0.000    0.000    0.000 task_14.py:5_iter(fast)
        1_base    0.000    0.000    3_array.000    3_array.000 task_14.py:9(slow)
        1_base    0.000    0.000    3_array.500    3_array.500 {built-in method builtins.exec}
        3_array    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        2_type_data    3_array.500    1_base.750    3_array.500    1_base.750 {built-in method time.sleep}
        1_base    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

print(timeit("gen_prime(3000)", "from __main__ import gen_prime", number=1))