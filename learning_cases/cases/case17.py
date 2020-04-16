# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
#
# # 程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。


line = input('请输入一行任意字符:')

letters = 0
space = 0
number = 0
others = 0

for c in line:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        number += 1
    else:
        others += 1

print('char = %d, space = %d, number = %d, others = %d' % (letters,space,number,others))