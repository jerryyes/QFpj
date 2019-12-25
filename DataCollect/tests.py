from django.test import TestCase

# Create your tests here.
#迭代
def getSum(x):
    sum = 0
    if x <= 5:
        sum += 20*x + 10
    else:
        sum += getSum(x-5) + 110
    return sum

#冒泡排序算法
def popsort(unsortedlist):
    sortlist = unsortedlist
    for j in range(len(sortlist)-1):
        for i in range(len(sortlist)-1-j):
            if sortlist[i] > sortlist[i + 1]:
                temp = sortlist[i]
                sortlist[i] = sortlist[i + 1]
                sortlist[i + 1] = temp
    return sortlist


if __name__=='__main__':
    print(getSum(20))
    print(popsort([2,10,4,28,44,33,22,20,1,16]))