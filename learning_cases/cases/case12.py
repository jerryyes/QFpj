# 题目：判断101-200之间有多少个素数，并输出所有素数。
#
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。


import math

# 用 leap做素数标记,当 leap=1时标记该数为素数,否则设置 leap=0
leap = 1
result = []
for i in range(101,201):
    for j in range(2,int(math.sqrt(i+1))+1):
        if i%j == 0:
            leap = 0
            break
    if leap == 1:
        result.append(i)
    leap = 1 #把素数加入列表后,重置标记

print(result)
print('一共有:%d个素数' % len(result) )

