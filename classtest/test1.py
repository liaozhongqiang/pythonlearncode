#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


st = Student('张三', 55)
print(st.score)
print(st.name)
st.age = 18
print(st.age)


class Student2(object):
    # 限制其属性
    __slots__ = ('name', 'score')

    def __init__(self, name, score):
        self.name = name
        self.score = score


st2 = Student2('住咯iu', 60)
print(st2.score)
print(st2.name)


# st2.age = 50 ERROR
# print(st2.age)

class Student3(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    # 定义len()
    def __len__(self):
        return 100


st3 = Student3('王五', 199)
# print(st3.__name) __表示private属性

print(dir(st3))

print(len(st3))


# print(len(st))  TypeError

# 继承多态


class Animal(object):
    def jiao(self):
        print("animal jiao")


a = Animal()
a.jiao()


class Dog(Animal):
    def jiao(self):
        print("dog jiao")


dog = Dog()
dog.jiao()


# 没有强制要求是 Animal的子类，只要求是有jiao()方法即可
def duotai(animal):
    animal.jiao()


duotai(dog)
duotai(a)

# 判断类型

print(isinstance(a, Animal))
print(isinstance(dog, Animal))
print(isinstance(a, Dog))

print(type(dog))

print(type(a))


# 省略set get的做法
class Student4(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value


st4 = Student4()

st4.birth = '2016-05-15'
print(st4.birth)


class Screen(object):
    def __init__(self):
        self._width = ''

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def heigth(self):
        return 500


screen = Screen()

# screen.width = 500
# screen.heigth = 400  AttributeError  can't set attribute
print(screen.width)
print(screen.heigth)


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().users.timeline.list)
