# 题目：将一个列表的数据复制到另一个列表中。
#
# 程序分析：使用列表[:]。


a = [1,2,3,4]

# 利用列表的切片方法实现
b = a[:]
c = a[0:2] #半开半闭区间,包含左边的值,但不包含右边的值

print(b)
print(c)