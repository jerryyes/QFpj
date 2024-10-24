# HJ4 字符串分隔
#
# 描述
# •输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 输入描述：
# 连续输入字符串(每个字符串长度小于等于100)
#
# 输出描述：
# 依次输出所有分割后的长度为8的新字符串
#
# 示例1
# 输入：abc
# 输出：abc00000

s = input("请输入随机字符串：")
temp = s
for i in range(int(len(s)/8)+1):
    ns = ""
    if len(temp) >= 8:
        for i in range(8):
            ns += temp[i]
        temp = temp[8:]
        print(ns)
    elif len(temp):
        for i in range(len(temp)):
            ns += temp[i]
        while len(ns) < 8:
            ns += "0"
        print(ns)