"""
--运算符重载;数据描述符的运用
"""
import time


class DictLikeObject:
    """
    应用于解决方案1
    """
    def __new__(cls, *args, **kwargs):
        cls.__my_dict = dict()
        cls.my_key = cls.__my_dict.keys
        cls.add = cls.__my_dict.__setitem__
        return super().__new__(cls)

    def __eq__(self, other):
        if isinstance(other, DictLikeObject):
            return self.__my_dict == other.__my_dict and self.my_key() == other.my_key()
        elif isinstance(other, list):
            return list(self.my_key()) == other
        pass

    def __str__(self):
        return "<DictLikeObject><Keys:%s>" % self.my_key()
    pass


class Descriptor:
    """
    应用于解决方案2
    """
    def __get__(self, instance, owner):
        return instance.get_now_time()
        pass

    def __set__(self, instance, value):
        instance.update_time()
        self.__time = instance.set_now_time(str(value) + str(instance.get_now_time()))
        pass


class DescriptorWrapper:
    data = Descriptor()
    __time = None

    def __init__(self):
        self.__time = time.time()
        print("初始化时间戳self.__time：", self.__time)

    def update_time(self):
        self.__time = time.time()
        print("自动更新了时间戳:", self.__time)

    def get_now_time(self):
        return self.__time

    def set_now_time(self, value):
        self.__time = value
        print("用户定义了新时间戳:", self.__time)


class Solution:
    @staticmethod
    def solution1_overload_eq():
        """
        重载类DictLikeObject运算符__eq__，使本方法执行时无异常抛出
        :return:
        """
        key_list = ['ak', 'bk', 'ck']
        instance_a = DictLikeObject()
        instance_b = DictLikeObject()
        instance_av_format = 'has_set_{}'.format
        instance_bv_format = 'also_has_set_{}'.format
        for key in key_list:
            instance_a.add(key, instance_av_format(key))
            instance_b.add(key, instance_bv_format(key))
        assert_error_format = '实现错误\n{}\n<= not equal =>\n{}'.format
        assert instance_a == instance_b, assert_error_format(instance_a, instance_b)
        assert instance_a == key_list, assert_error_format(instance_a, key_list)
        assert instance_b == key_list, assert_error_format(instance_b, key_list)

    @staticmethod
    def solution2_descriptor():
        """
        实现数据描述符Descriptor __get__、__set__方法，使以下代码运行时：
        1>对于类DescriptorWrapper的实例(简称DW)，使用'.'运算符获取数据描述符Descriptor的实例时，返回DW的实例方法get_now_time的结果;
        2>使用'='运算符为DW.data赋值value时，调用update_time更新当前时间戳，然后将value与当前时间拼接，调用set_now_time最终更新为str(value)+str(now_time),即：
        DW.data='what happend' ===> DW.__time='what happend' + str(DW.__time)
        :return:
        """
        des = DescriptorWrapper()
        print(des.data)
        des.data = 'what'  # 当前时间为555555时，此时更新des.__time为"what555555"
        print(des.data)


if __name__ == '__main__':
    # Solution.solution1_overload_eq()
    Solution.solution2_descriptor()
