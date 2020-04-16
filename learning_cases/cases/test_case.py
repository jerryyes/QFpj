from gevent import monkey; monkey.patch_all()
import requests
import gevent
import time


def f(url,headers):
    print(url)
    data = requests.get(url,headers,timeout=300)
    print(data)
    if data.status_code == 200:
        rejson = data.json()
        content = data.content
        text = data.text
        print(type(rejson),rejson)
        print('')
        print(type(content),content)
        print('')
        print(type(text),text)
 
start = time.time()
url = 'http://www.kuaidi100.com/query?type=shunfeng&postid=00001111'
headers = {'Accept-Language':'en-GB,en;q=0.9,ko;q=0.8,en;q=0.7'}
url_list = []
for i in range(5):
    url_list.append(gevent.spawn(f, url,headers))
gevent.joinall(url_list)
print(time.time()-start)