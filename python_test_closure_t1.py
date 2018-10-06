from functools import reduce
def createCount():
    def caculate(arg):
        pass
    def count():
        return 1
    return count

count1 = createCount()
count2 = createCount()
count3 = createCount()

print(count1(),count2(),count3())
