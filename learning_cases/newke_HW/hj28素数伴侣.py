# HJ28 素数伴侣
#
# 描述
# 题目描述
# 若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6
# 和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的N （ N为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6
# 和13编组将得到两组“素数伴侣”，能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。
#
# 输入:
# 有一个正偶数n ，表示待挑选的自然数的个数。后面给出n个具体的数字。
#
# 输出:
# 输出一个整数K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
#
# 输出描述：
# 求得的“最佳方案”组成“素数伴侣”的对数。
#
# 示例1
# 输入：4
# 2 5 6 13
# 输出：2
#
# 示例2
# 输入：2
# 3 6
# 输出：0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def find_partners(nums):
    even_nums = [num for num in nums if num % 2 == 0]
    odd_nums = [num for num in nums if num % 2 == 1]

    def find_match(even_num):
        for odd_num in odd_nums:
            if is_prime(even_num + odd_num):
                return odd_num
        return None

    matches = {}
    for even_num in even_nums:
        odd_match = find_match(even_num)
        if odd_match is not None:
            matches[even_num] = odd_match
            odd_nums.remove(odd_match)

    return len(matches)

n = int(input())
nums = list(map(int, input().split()))
result = find_partners(nums)
print(result)

