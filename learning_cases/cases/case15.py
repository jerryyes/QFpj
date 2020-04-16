# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
#
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。


while True:
    try:
        score = int(input('请输入分数:'))
        if score >= 90:
            level = 'A'
        elif score >= 60:
            level = 'B'
        else:
            level = 'C'
        print('%d 属于 %s' % (score,level))
        break
    except ValueError:
        print('格式有误,请重新输入!')