from functools import reduce
import sys
def log(fn):
    print('i am decorator!')
    def wrp(*a,**b):
        print('this is func deco\'s wrp')
        print(fn.__name__)
    return wrp

@log
def getDate(a):
    print('i am function')
    return a

kk = getDate(a=10)
print(kk)
# 装饰器里面的函数为什么没有被执行呢？没想明白。。。
