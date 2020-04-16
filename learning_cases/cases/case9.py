# 题目：暂停一秒输出。
#
# 程序分析：使用 time 模块的 sleep() 函数。

import time

mylist = ['a','b']
mydict = {1:'a',2:'b'}

for k,v in enumerate(mylist):
    print(k,v)
    time.sleep(5) #暂停 5 秒

for k,v in enumerate(dict.items(mydict)):
    print(k,v)
    time.sleep(1)
