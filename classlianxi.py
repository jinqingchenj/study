# 求100内质数
# def jia(x):
#     for i in range(2,x):
#         if x%i ==0:
#             return False
#     return True
# for i in range(2,101):
#     if jia(i):
#         print(i)
# f = open('mypackage/wenjian.txt')
# lines = f.readlines()
# count = {}
# for line in lines:
#     words = line.strip().split(' ')
#     for word in words:
#         if word not in count:
#             count[word]=0
#         count[word]+=1
# for aaa in count:
#     print(aaa,count[aaa])
# a = {'aaa':'111','bbb':'222','ccc':'333'}
# b = 'aaa'
# if b in a.values() :
#     print('有')
# else:
#     print('无')
'''
class animal:
    def __init__(self):
        print('动物初始化')
        self.color='红色'
    def eat(self):
        print('吃饭')
    def sleep(self):
        print('睡觉')
class dog(animal):
    def __init__(self,name):
        super().__init__()
        print('狗初始化')
        self.name=name
    def eat(self):
        super().eat()
        print('狗狗吃饭')
    def shut(self):
        print('汪汪汪')
class cat(animal):
    def __init__(self):
        print('猫初始化')
    def tiao(self):
        print('跳跃')
class zang(dog):
    def fight(self):
        print('战斗')
gou = dog('黑')
print(gou.name)
'''
'''
class F1(object):
    def show(self):
        print('F1')
class S1(F1):
    def show(self):
        print('S1')
class S2(F1):
    def show(self):
        print('S2')
def fun(obj):
    print(obj.show())
s1 = S1()
fun(s1)
s2 = S2()
fun(s2)
'''
# class admin(object):
#     name='jin'
#     __password='12345'
#     def __init__(self,sex,username):
#         self.sex = sex
#         self.name = username
# class oicq(admin):
#     pass
# u = admin('nan','jiiiii')
# print(u.name)

# class A(object):
#     name='ss'
#     def test1(self):
#         print('aaa11111')
#     @classmethod
#     def test2(cls):
#         cls.name='xxxx'
#         print('aaaa222222')
# a = A()
# a.test2()
# A.test2()
# print(a.name)