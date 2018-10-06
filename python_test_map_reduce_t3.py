from functools import reduce


def s2f(str):
    def spl(a, b):
        res = a * 10 + b
        return res
    point = str.index('.')
    intPart = list(map(int, [x for x in str[0:point]]))
    deciPart = list(map(int, [x for x in str[point + 1:]]))
    print(intPart)
    print(deciPart)
    result = float(reduce(spl, intPart)) + \
        reduce(spl, deciPart) / 10**len(deciPart)
    return result


a = s2f('3.1415926')
print(type(a))
print(a)

# str_1 = '3.1415926'
# flag = str_1.index('.')
# print(type(flag))
# print(flag)
