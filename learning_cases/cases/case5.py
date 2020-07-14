# 题目：输入三个整数x,y,z，请把这三个数由小到大输出。
#
# 程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。


numbers = input('请输入三个整数(以逗号分隔):')

num_list = list(map(int,numbers.split(','))) #python3.x 中 map 函数返回值类型为迭代器,此处需要转换为 list 类型
print(num_list)

# 方法一:可用list排序函数实现(返回值类型为 list,改变原list 本身)
num_list.sort()
print(num_list)

# 相关知识:list 的倒序函数(返回值类型为迭代器,不改变原list 本身)
num_list_reversed = num_list.__reversed__()
print(list(num_list_reversed))
print(num_list)

# 相关知识:list 的倒序函数(改变 原list 本身)
num_list.reverse()
print(num_list)

# 方法二:冒泡排序算法
for i in range(len(num_list)):
    for j in range(len(num_list)-i-1):
        if num_list[j] > num_list[j+1]:
            num_list[j],num_list[j+1] = num_list[j+1],num_list[j]
print(num_list)
