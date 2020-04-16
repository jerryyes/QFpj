# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
#
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。


kl = []
while True:
    try:
        inum = int(input('请输入一个正整数:'))
        print('%d = ' % inum)
        if inum <= 0:
            print('格式有误,请重新输入!')
            exit(0)
        elif inum in [1] :
            print('%d' % inum)
        while inum not in [1] : # 循环保证递归
            for k in range(2, inum + 1) :
                if inum % k == 0:
                    inum = int(inum/k)
                    kl.append(k)
                    break
        print('*'.join(map(str,kl)))
        break
    except ValueError:
        print('格式有误,请重新输入!')
