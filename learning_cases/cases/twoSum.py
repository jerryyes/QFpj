# 两数之和
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

if __name__ == '__main__':
    res = two_sum([2,7,11,15],22)
    print(res)