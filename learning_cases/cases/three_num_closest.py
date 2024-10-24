def three_sum_closest(nums, target):
    nums.sort()
    min_diff = float('inf')
    result = None

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            diff = abs(cur_sum - target)

            if diff < min_diff:
                min_diff = diff
                result = ([nums[i], nums[left], nums[right]], [nums.index(nums[i]), nums.index(nums[left]), nums.index(nums[right])], cur_sum)

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return ([nums[i], nums[left], nums[right]], [nums.index(nums[i]), nums.index(nums[left]), nums.index(nums[right])], cur_sum)

    return result

if __name__ == '__main__':
    res = three_sum_closest([-1,0,1,2,7,5],9)
    print(res)