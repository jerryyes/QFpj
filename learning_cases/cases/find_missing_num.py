def find_missing_number(nums):
    max_num = max(nums)
    all_nums = set(range(max_num + 1))
    present_nums = set(nums)
    print(all_nums - present_nums)
    return list(all_nums - present_nums)

if __name__ == '__main__':
    res = find_missing_number([4,9,10])
    print(res)