"""
--字符串处理
按要求实现类Solution中以solution开头的静态方法;
"""
import time
import datetime
import json

GLOBAL_JSON_STRING_LIST = ["{'time_index_1':'time.time()'}", "{'time_index_2':time.time()}", "{'bool_index_1':True}", "{'bool_index_2':true}"]

ERROR_NAMESPACE = {'time': datetime, 'true': False}
FULL_NAMESPACE = {'time': time, 'true': True}


class Solution:
    @staticmethod
    def solution1_string_to_python_object_by_json_modules():
        """
        遍历GLOBAL_JSON_STRING_LIST,利用json库将其中json格式的字符串转化为Python对象，组成新列表；将非json字符串组成另一个列表，
        以元组的形式输出两个新列表
        :return:Json_format_list,others_list
        """
        Json_format_list = []
        others_list = []
        for s in GLOBAL_JSON_STRING_LIST:
            try:
                trans_result = json.loads(s)
                Json_format_list.append(trans_result)
            except json.JSONDecodeError:
                others_list.append(s)
        return Json_format_list,others_list
        pass

    @staticmethod
    def solution2_string_to_python_object_by_eval():
        """
        了解(百度)Python内置方法eval，利用eval方法，分别将ERROR_NAMESPACE与FULL_NAMESPACE作为局部命名空间，
        遍历GLOBAL_JSON_STRING_LIST,将其中字符串转为Python对象，
        以元组的形式输出，比较两者异同
        :return:ERROR_NAMESPACE_LIST,FULL_NAMESPACE_LIST
        """
        pass

    @staticmethod
    def solution3_eval():
        """
        执行本方法，保留执行结果，了解eval方法滥用的危害性，尤其是未规定局部命名空间，直接使用前端用户填写的内容作为入参执行时
        :return:
        """
        content_dir = []
        utf_dir_list = [b'\xe6\x88\x91\xe7\x88\xb1\xe5\x90\x83\xe5\xb1\x8e', b'\xe5\x90\x83\xe5\xb1\x8e\xe4\xbd\xbf\xe6\x88\x91\xe5\xbf\xab\xe4\xb9\x90']
        dir_list = map(lambda x: x.decode(), utf_dir_list)
        create_template = "__import__('os').mkdir('{dir}')".format
        for node in dir_list:
            content_dir.append(node)
            final_dir = '/'.join(content_dir)
            eval(create_template(dir=final_dir))
        pass


if __name__ == '__main__':
    r = Solution.solution1_string_to_python_object_by_json_modules()
    print(r)