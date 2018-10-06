from functools import reduce
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCount():
    a = [0]
    print('type of a is',type(a))
    print('type of a[0] is',type(a[0]))
    def count():
        a[0] = a[0] + 1
        return a[0]
    return count

# def createCount():
#     a = 0
#     def count():
#         a = a + 1
#         return a
#     return count

count1 = createCount()
count2 = createCount()
count3 = createCount()

print(count1(),count1(),count1(),count2(),count3())
