import functools
from functools import partial

csy = functools.partial(int,base = 2)

a=csy('100')
print(a)
b=csy('78',base = 10)
print(b)
