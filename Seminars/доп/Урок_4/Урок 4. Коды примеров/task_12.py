from cProfile import run
from time import sleep


def func_2():
    sleep(10)
    print("Я очень медленная функция")


run('func_2()')

"""
Я очень медленная функция
         6 function calls in 10.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1_base    0.000    0.000   10.000   10.000 <string>:1_base(<module>)
        1_base    0.000    0.000   10.000   10.000 task_12.py:5_iter(func_2)
        1_base    0.000    0.000   10.000   10.000 {built-in method builtins.exec}
        1_base    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1_base   10.000   10.000   10.000   10.000 {built-in method time.sleep}
        1_base    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

