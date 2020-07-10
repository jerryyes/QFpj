"""
--综合数据处理
按要求实现类Solution中以solution开头的静态方法;
"""

import requests

HOST = "http://172.16.3.203"
PORT = "8001"
CATEGORY_URI = "camp/category/"
RESULT_URI = "camp/result/"


class Solution:
    @staticmethod
    def get_node_list():
        """
        调用本方法,可以获取Solution1所需的NodeList
        :return:
        """
        r = requests.get(url="/".join((":".join((HOST, PORT)), CATEGORY_URI)))
        return r.json().get('data', []) if r.json().get('code') == 200 else []

    @staticmethod
    def get_truly_result(node_id=None):
        """
        调用本方法，可以获取Solution1的正确结果
        :param node_id: 传入的node_id
        :return:
        """
        r = requests.get(url="/".join((":".join((HOST, PORT)), RESULT_URI)), params={'node_id': node_id})
        return r.json().get('data') if r.json().get('code') == 200 else []

    @staticmethod
    def solution1_get_children_node_by_id(node_id=None):
        """
        现有一数据结构形如{id:'xxx',parent_id:'yyy',name:'zzz'}的元素(称为node)构成的集合NodeList=[node1,node2,....,node999]；
        node的特征:
            1>每个node的键id唯一地表示这个node，
            2>键parent_id表示该node元素父节点的id(即NodeList中其他某个node的id，且每个node只有一个父node),
            3>存在部分node，其parent_id为0，这种node称为一级子节点，其parent_id无法在nodeList中找到node与之对应；
            4>其他node的父节点id在NodeList中必然存在；
            5>一个node可以有多个子node，即有多个node的键parent_id指向同一个node的键id；
        观察NodeList的结构，实现本方法，当：
        ：入参node_id未给定或不存在时，返回列表全部节点；
        ：传入node_id时，从NodeList中查找出id=node_id的节点本身及其全部次级节点(次级节点即：子节点的子节点+子节点的子节点的子节点+。。。+加到没有parent_id指向该节点为止)，
        输出其id组成的列表
        :return:[id1,id2,id3,...]
        """
        # NodeList由get_node_list()方法提供
        NoteList = [{'id': '111', 'parent_id': '0', 'name': 'node111'}, {'id': '222', 'parent_id': '111', 'name': 'node222'},
                    {'id': '333', 'parent_id': '0', 'name': 'node333'}, {'id': '444', 'parent_id': '111', 'name': 'node444'},
                    {'id': '555', 'parent_id': '222', 'name': 'node555'}, {'id': '666', 'parent_id': '444', 'name': 'node666'}]
        ChildList = []
        if node_id in [node['id'] for node in NoteList]:
            ChildList.append(node_id)
            for node in NoteList:
                if node_id in node['parent_id']:
                    ChildList += Solution.solution1_get_children_node_by_id(node['id'])
        else:
            ChildList = [node['id'] for node in NoteList]

        return ChildList
        pass

    @staticmethod
    def solution2_verify_solution1_logic(your_logic=None, truly_result=None):
        """
        自写逻辑，将solution1_get_children_node_by_id的执行结果与get_truly_result方法的结果比较;
        判断solution1执行结果是否正确(即判断两个list元素是否相同,可以使用任何内置方法);
        输出bool值
        :param your_logic:
        :param truly_result:
        :return:True or False
        """
        pass


if __name__ == '__main__':
    print(Solution.solution1_get_children_node_by_id('111'))
    pass
