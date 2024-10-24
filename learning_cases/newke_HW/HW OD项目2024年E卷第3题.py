# 输入：一个整数区间，找出该区间中二进制转换后不包含101的数字
# 输出：不包含101的数字个数

nm = input("请输入整数区间（以空格分隔）：")
n = int(nm.split()[0])
m = int(nm.split()[1])

def int_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

count = 0
for num in range(n,m+1):
    if "101" not in int_to_binary(num):
        count += 1
print("区间内不包含101的数字个数为：" + str(count))

