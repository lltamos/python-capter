class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_score(self):
        print('%s: %s' % (self.name, self.age))


def print_age(stu):
    print('%s:%s' % (stu.name, stu.age))
    print('{}:{}'.format(stu.name, stu.age))


stud = Student('tao', 30)
stud.print_score()


class Animal(object):
    def run(self):
        print('animal run ...')


class Dog(Animal):
    def run(self):
        print('dog run ...')

    pass


class Cat(Animal):
    def __init__(self, name):
        self.name = name


dog = Dog()

isinstance(dog, Animal)

print(isinstance(dog, Cat))

cat = Cat('name')


def run_animal(animal):
    animal.run()


run_animal(dog)

print(type(dog))

print(type(Dog))
#
# print(dir(Animal))

print(hasattr(cat, 'name'))


class Person:

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


person = Person()
person.name = 'person'
print(person.name)


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for n in Fib():
    print(n)

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(len(Month.__members__))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)


# @unique
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# print(Weekday.Sun.value)

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)


def deco(func):
    def d_deco():
        print("before myfunc() called.")
        func()
        print("after myfunc() called.")
        # 不需要返回func，实际上应返回原函数的返回值

    return d_deco


@deco
def myfunc():
    print(" myfunc() called.")
    return 'ok'


myfunc()
myfunc()

