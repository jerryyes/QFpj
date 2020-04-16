# 题目：输出指定格式的日期。
#
# 程序分析：使用 datetime 模块。


import datetime

if __name__ == '__main__':

    # 输出今日日期，格式为 yyyy-mm-dd HH:MM:SS。更多选项可以查看 strftime() 方法
    print(datetime.date.today().strftime('%Y-%m-%d %H:%M:%S'))

    # 创建日期对象
    myBirthDate = datetime.date(1987, 8, 26)
    print(myBirthDate)
    print(myBirthDate.strftime('%Y-%m-%d %H:%M:%S'))

    # 日期算术运算
    myBirthNextDay = myBirthDate + datetime.timedelta(days=1)

    print(myBirthNextDay.strftime('%Y-%m-%d %H:%M:%S'))

    # 日期替换
    myFirstBirthday = myBirthDate.replace(year=myBirthDate.year + 1)

    print(myFirstBirthday.strftime('%Y-%m-%d %H:%M:%S'))