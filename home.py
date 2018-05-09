# set交集
# girl1 = set(['lili','mimi'])
# girl2 = set(['liuliu','mimi'])
# print(girl1 | girl2)
# print(girl1 & girl2)
# 函数与函数暂存
# def pr_hello(s,*arg):
#     print(s)
#     for a in arg:
#         print(a)
# pr_hello('hello')
# pr_hello('haha','hehe','heihei')
# python类
# class people:
#     # 定义基本属性
#     name = ''
#     age = 0
#     # 定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
# 实例化类
# p = people('runoob', 10, 30)
# p.speak()
# end用法
# print('111',end=',,,')
# print('222',end='')
# print('333')
# 输出最后一位
# a = 'qwertyuio'
# print(a[len(a)-1]
# 1-100总和循环
# i = 100
# n = 0
# c = 1
# while c<=i:
#     n = c+n
#     c+=1
# print('1至100总和为{0}'.format(n))
# a = 0
# for i in range(101):
#     a = a+i
# print(a)
# format引用字典
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}
# print("网站名：{name}, 地址 {url}".format(**site))
# 生成器
# def fib(na):
#     l = ['teacher','miss','man']
#     for x in l:
#         yield na+x
#     return 'done'
# f = fib('ss')
# next(f)
# print(f.send('dd'))




