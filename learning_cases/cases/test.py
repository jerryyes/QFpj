# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import pytest
import requests


@pytest.fixture(params=[1, 2, 3])
def need_data(request):  # 传入参数request 系统封装参数
    return request.param  # 取列表中单个值，默认的取值方式


class Test_ABC:

    def setup_class(self):
        print("------->setup_class")

    def teardown_class(self):
        print("------->teardown_class")

    def test_c(self):
        res_str = ''
        test_str = 'like you.'
        list_str = list(test_str)
        for i in range(len(list_str)):
            res_str += list_str[-i - 1]
        print(res_str)
        print("------->test_c")
        assert res_str == '.uoy ekil'  # 断言res_str不等于是否倒序排列

    def test_d(self):
        test_list = [111,112,113,222,212,213,333,444,555,321,311,320]
        res_list = [int(x/100)+int(x%100/10)+x%10 for x in test_list]
        print(res_list)
        print("------->test_d")
        assert res_list == [3,4,5,6,5,6,9,12,15,6,5,5]  # 断言res_str不等于是否倒序排列

    def test_f(self):
        r = requests.get('https://www.baidu.com/')
        bd_home = r.cookies['BD_HOME']
        print(bd_home)
        print("------->test_f")
        assert bd_home == '1'

    @pytest.mark.skipif(condition=2 > 1, reason="不执行测试用例test_b")  # 跳过测试函数test_b
    def test_b(self):
        print("------->test_b")
        assert 0

    @pytest.mark.parametrize("a,b", [(1, 2), (0, 3)])  # 参数a,b均被赋予两个值，函数会运行两遍
    def test_a(self, a, b):  # 参数必须和parametrize里面的参数一致
        print("test data:a=%d,b=%d" % (a, b))
        assert a + b == 3


if __name__ == '__main__':
    pytest.main()
    # test12


