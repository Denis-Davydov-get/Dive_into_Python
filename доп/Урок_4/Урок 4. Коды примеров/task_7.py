from time import sleep
from timeit import repeat, default_timer


class TestClass:

    @staticmethod
    def some_slow_method(loop_count):
        for i in range(loop_count):
            sleep(1)

    @staticmethod
    def some_quick_method(loop_count):
        for i in range(loop_count):
            sleep(0.1)


if __name__ == '__main__':

    setup = """
from __main__ import TestClass
test = TestClass()
    """
    statements = ['TestClass.some_slow_method(5_iter)',
                  'test.some_slow_method(3_array)',
                  'test.some_quick_method(5_iter)',
                  'test.some_quick_method(3_array)']

    for st in statements:
        print(f'{st}, {min(repeat(st, setup, default_timer, 3, 1))}')

"""
test.some_slow_method(5_iter), 5_iter.002561600000001
test.some_slow_method(3_array), 3_array.000246899999997
test.some_quick_method(5_iter), 0.5015900000000002
test.some_quick_method(3_array), 0.30135129999999677
"""

# если нет необходимости создавать объект класса
'''
    setup = "from __main__ import TestClass"
    statements = ['TestClass.some_slow_method(5_iter)',
                  'TestClass.some_slow_method(3_array)',
                  'TestClass.some_quick_method(5_iter)',
                  'TestClass.some_quick_method(3_array)']
'''