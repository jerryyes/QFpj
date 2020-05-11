# 题目：斐波那契数列。
#
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。
#
# 在数学上，费波那契数列是以递归的方法来定义：
#
# F1 = 1     (n=1)
# F2 = 1    (n=2)
# Fn = F[n-1]+ F[n-2](n>2)


#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 方法一:斐波那契数列的一般实现
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

# 输出前 10 个斐波那契数列
print(fib(10))


# 方法二:斐波那契数列的递归实现
def fib_iter(n):
    i,a,b = 0,0,1
    out = []
    while i < n:
        out.append(b)
        a,b = b,a+b
        i += 1
    print(out)
    return 'done'

out = fib_iter(10)
print(out) #输出 return 的内容


# 方法三:斐波那契数列的生成器迭代
def fib_generator(n):
    i,a,b = 0,0,1
    while i < n:
        yield b
        a,b = b,a+b
        i += 1
    return 'done'

out = []
g = fib_generator(10)
while True:
    try:
        out.append(next(g))
    except StopIteration as e:
        print(out)
        print('生成器返回值:',e.value)  #输出 return 的内容
        break

