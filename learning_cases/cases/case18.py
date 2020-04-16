# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
#
# 程序分析：关键是计算出每一项的值。

from functools import reduce

# 一:生成器的运用,通过生成器生成用于计算各相加项的值的序列
# 二:reduce 函数的运用,函数会对参数序列中元素进行累积。函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
# 用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
# 得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

add_num = int(input('请输入相加项的个数:'))
num = int(input('请输入0-9中的一个数字作为公式基础元素:'))
generator = (num*pow(10,x) for x in range(add_num))
cs = 0
s = 0
slist = []
while True:
    try:
        cs += next(generator)
        slist.append(cs)
    except StopIteration as e:
        break

s = reduce(lambda x,y : x+y,slist)
# 等价于:
# for i in range(len(slist)):
#     s += slist[i]

formula = ' + '.join(map(str,slist))
print('s = %s = %d' % (formula,s))

