from functools import reduce
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# LL = [[[a],[1,2,3]],[[b],[4,5,6]]]
# print(L[0])
# print(L[1])
# python中sorted函数的key参数更像是map，会被排列顺序映射到列表的每一个值上。
# 不需要考虑如何从外层进入到内层的逻辑处理
def byname(t):
    print('type of t was:')
    print(type(t))
    print('type of t[] was:')
    print(type(t[0]))
    print(t[0])
    return t[0]
def byscore(t):
    print('type of t was:')
    print(type(t))
    print('type of t[] was:')
    print(type(t[1]))
    print(t[1])
    return t[1]

# r1 = byname(L)
# r2 = sorted(L,key=byname)
# print(r2)

print('============')
r1 = byscore(L)
print('============')
r2 = sorted(L,key=byscore)
print(r2)
