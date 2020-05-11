# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
#
# 程序分析：请抓住分子与分母的变化规律。

from functools import reduce

# 方法一:菲波那切数列
def fib(n):
    re = 0
    if n == 1 or n == 2:
        re = 1
    elif n > 2:
        re = fib(n-1)+fib(n-2)
    return re

def sum_head(x):
    headx = 0
    for i in range(1,x+1):
        headx += fib(i+2)/fib(i+1)
    return headx

# 方法二:reduce()函数结合 lambda 表达式
def sum_head2(x):
    a = 2.0
    b = 1.0
    l = []
    l.append(a / b)
    for n in range(1,x):
        b,a = a,a + b
        l.append(a / b)
    return reduce(lambda x,y: x + y,l)

if __name__ == '__main__':
    while True:
        try:
            insert = int(input('请输入累加的项数(正整数):'))
            res = sum_head(insert)
            res2 = sum_head2(insert)
            print('(方法一)累加前%d项之和为%.10f' % (insert,res))
            print('(方法二)累加前%d项之和为%.10f' % (insert,res2))
            break
        except ValueError:
            print('格式有误,请重新输入!')


