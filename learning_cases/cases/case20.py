# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
#
# 程序分析：无

def ball_tour(start_height,times):
    tour = []
    height = []

    for i in range(1, times + 1):
        # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
        if i == 1:
            tour.append(start_height)
        else:
            tour.append(2*start_height)
        start_height /= 2
        height.append(start_height)

    print('总高度：tour = {0}'.format(sum(tour)))
    print('第10次反弹高度：height = {0}'.format(height[-1]))


if __name__ == '__main__':
    ball_tour(100,10)
