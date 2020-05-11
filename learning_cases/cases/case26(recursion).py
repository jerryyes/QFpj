# 题目：利用递归方法求5!。
#
# 程序分析：递归公式：fn=fn_1*4!


def factorial(x):
    if x == 1:
        s = x
    else:
        s = x * factorial(x-1)
    return s

if __name__=='__main__':
    while True:
        try:
            i = int(input('请输入一个正整数:'))
            r = factorial(i)
            print('%d! = %d' % (i,r))
            break
        except Exception as e:
            print(e)