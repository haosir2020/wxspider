# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import socket
import urllib.request

def get_request_test():
    req = urllib.request.Request('http://www.baidu.com')
    res = urllib.request.urlopen(req)
    html = res.read()
    soup = BeautifulSoup(html)
    body = soup.get_text
    print(body)

def get_request(url):
    socket.setdefaulttimeout(5)
    params = {"wd":"a", "b":2}
    i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", "Accept": "text/plain"}
    req = urllib.request.Request(url, headers=i_headers)
    try:
        page = urllib.request.urlopen(req)
        html = page.read()
        print (len(html))
    except urllib.request.HTTPError as e:
        print ("Error code:", e.code)
    except urllib.request.URLError as e:
        print ("Error code:", e.reason)
    return html
#---------------------#
turl = "http://www.baidu.com"
bhtml = get_request(turl)
thtml = bhtml
fo = open("data/out1.txt", "wb+")
fo.write(thtml)
print (thtml)
