# -*- coding = utf-8 -*-
# @Time :2022/10/8 8:53
# @Author :江银涛
# @File :testUrllib.py
# @Software: PyCharm

import urllib.request

#获取一个get请求
#
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))



#获取一个post请求

import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world","qq":"www"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

#超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("time out!")



# response = urllib.request.urlopen("http://www.baidu.com")
# # print(response.status)
# print(response.getheaders())#获取某些数据getgeader('Server')



#访问测试
# url="http://httpbin.org/post"
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"
# }
# data=bytes(urllib.parse.urlencode({'name':'eric'}),encoding="utf-8")
# req= urllib.request.Request(url=url,data=data,headers=headers,method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))

#访问豆瓣
#将自己封装为一个网站
url="http://www.baidu.com"
headers={
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"
}
req= urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))