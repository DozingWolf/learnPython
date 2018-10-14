class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def set_gender(self,rank):
        self.__gender = rank
        return 1
    def get_gender(self):
        return self.__gender

csy = Student('AB','male')
csy.set_gender('ABC')
print(csy.get_gender())
