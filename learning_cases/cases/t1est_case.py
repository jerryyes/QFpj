# !/usr/bin/python
# -*- coding: UTF-8 -*-

# from gevent import monkey; monkey.patch_all()
import requests
import gevent
import time


# def f(url,headers):
#     print(url)
#     data = requests.get(url,headers,timeout=300)
#     print(data)
#     if data.status_code == 200:
#         rejson = data.json()
#         content = data.content
#         text = data.text
#         print(type(rejson),rejson)
#         print('')
#         print(type(content),content)
#         print('')
#         print(type(text),text)
#     return rejson
 
# start = time.time()
# url = 'http://www.kuaidi100.com/query?type=shunfeng&postid=00001111'
# headers = {'Accept-Language':'en-GB,en;q=0.9,ko;q=0.8,en;q=0.7'}
# url_list = []
# for i in range(5):
#     url_list.append(gevent.spawn(f, url,headers))
# gevent.joinall(url_list)
# print(time.time()-start)

def test_f():
    r = requests.get('https://www.baidu.com/')
    cookies = r.cookies
    print(cookies)
    bd_orz = cookies['BDORZ']
    print(bd_orz)
    items = cookies.get_dict()
    print(items)
    test_list = ['abcde','efghi','adk']
    print(test_list)
    test_list.sort()
    print(test_list)
    # bd_home = r.cookies['BD_HOME']
    # print(bd_home)
    # assert bd_home == '1'


if __name__ == '__main__':
    # test_f()