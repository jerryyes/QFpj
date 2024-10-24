def all_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    # 测试
    print(all_unique("hello"))
    print(all_unique("world"))