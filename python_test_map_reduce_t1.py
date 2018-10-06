import sys
name_s = ['adam', 'LISA', 'barT']

# 方法1 耗时0.085s
# def normalize(name):
#    return name.capitalize()

#name_r = list(map(normalize, name_s))4

# 方法2 0.091s
def normalize_2(name):
    firstChar = name[0:1].upper()
    elseChar = name[1:].lower()
    fullName = firstChar + elseChar
    return fullName


name_r = list(map(normalize_2, name_s))
print('typeB is :',name_r)
