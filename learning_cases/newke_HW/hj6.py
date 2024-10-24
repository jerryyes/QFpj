# HJ6 质数因子
#
# 描述
# 功能: 输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#
# 输入描述：
# 输入一个整数
#
# 输出描述：
# 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
#
# 示例1
# 输入：
# 180
# 输出：2 2 3 3 5

def find_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

num = int(input("请输入一个正整数："))
factors = find_prime_factors(num)
print(" ".join(map(str, factors)))
