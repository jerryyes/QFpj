# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time

s = 'aBcD'
t_list = [1, 2, 3, 4]
t_turple = (1, 2, 3, 4)
t_dict = {1: 'a', 2: 'B', 3: 'c', 4: 'D'}
t_set = set([1, 2, 3, 4])

print(s.__iter__())
s1 = iter(s)
s2 = s.__iter__()
print(s1.__iter__())
print(s1.__next__())
print(s1.__next__())
print(s2.__next__())
# for str in s1:
#     print(str)
print(t_list.__iter__())
t_list1 = iter(t_list)
print(t_list1.__iter__())
print(t_list1.__next__())
# for l in t_list1:
#     print(l)
print(t_turple.__iter__())
t_turple1 = t_turple.__iter__()
print(t_turple1.__next__())
print(t_turple1.__next__())
print(t_dict.__iter__())
t_dict1 = t_dict.__iter__()
t_dict2 = t_dict.values()
print(t_dict2.__iter__())
print(t_dict1.__next__())
print(t_dict1.__next__())
print(t_set.__iter__())
t_set1 = t_set.__iter__()
print(t_set1.__next__())
print(t_set1.__next__())


def consumer(name):
    print("%s 准备学习啦!" % name)
    while True:
        lesson = yield

        print("开始[%s]了,[%s]老师来讲课了!" % (lesson, name))


c = consumer('Jerry')
# c.send('lesson1')
c.__next__()
c.__next__()
c.send('lesson2')

# c.__next__()



