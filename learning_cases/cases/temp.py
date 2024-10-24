nm = input("请输入n*m的矩阵：")
n = int(nm.split()[0])
m = int(nm.split()[1])
l = []

for i in range(1,n+1):
    line = input("请输入矩阵的第%d行对应的%d个值：" % (i,m))
    l.append(line.split())
max_sum = float('-inf')
for row in range(n):
    column_sums = [0] * m
    for i in range(row, n):
        for j in range(m):
            column_sums[j] += int(l[i][j])
        current_sum = 0
        max_local_sum = float('-inf')
        for s in column_sums:
            current_sum = max(s, current_sum + s)
            max_local_sum = max(max_local_sum, current_sum)
        max_sum = max(max_sum, max_local_sum)
print("和最大的子矩阵求和结果为：" + str(max_sum))