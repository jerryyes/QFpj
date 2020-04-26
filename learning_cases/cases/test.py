import grequests
import requests
import bs4

def err_handler(request, exception):
    print("请求出错")

headers = {'Accept-Language':'en-GB,en;q=0.9,ko;q=0.8,en;q=0.7'}
session = requests.session()

req_list = [
    grequests.get('http://httpbin.org/delay/1', timeout=0.001),   # 超时异常
    grequests.get('http://fakedomain/'),   # 该域名不存在
    grequests.get('http://www.kuaidi100.com/query?type=shunfeng&postid=00001111',headers=headers,timeout=300)    #  正常返回500的请求
]

rs = requests.session()
re = rs.get('http://www.kuaidi100.com/query?type=shunfeng&postid=00001111',headers=headers,timeout=300)
if re.status_code == 200:
    rejson = re.json()
print(rejson)

r_list = []
gs = grequests.request('get','http://www.kuaidi100.com/query?type=shunfeng&postid=00001111',headers=headers).response
print(gs)
r_list.append(gs)
res_list = grequests.map(r_list, exception_handler=err_handler)
print(res_list)

