from sys import getsizeof
from pympler.asizeof import asizeof


d = {1: '1_base', 2: '2_type_data', 3: '3_array'}
print(getsizeof(d))  # -> 240
print(asizeof(d))  # -> 504

t = (1, 2, 3)
print(getsizeof(t))  # -> 72
print(asizeof(t))  # -> 168
