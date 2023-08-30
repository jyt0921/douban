# -*- coding = utf-8 -*-
# @Time :2022/10/22 19:08
# @Author :江银涛
# @File :test2.py
# @Software: PyCharm
import hashlib
import pprint
import re
from datetime import time
import subprocess
import requests
from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import json

url="https://www.bilibili.com/video/BV1T8411t7FF"
headers={
    'referer': 'https://www.bilibili.com/video/BV1T8411t7FF/?vd_source=6107ab45f572ee0819e6c78e0e6e0469',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52'
}
#1、通过requests这个模块里面的get方法，对url发送请求  并且携带上headers请求头伪装，最后用定义变量的response接受数据
response=requests.get(url=url,headers=headers)
# html = response.read().decode("utf-8")
# print(response)

#2、获取数据，获取响应体的文本数据，response.text 网页源代码
# print(response.text)
'''
response.json()#获取json字典数据
response.content()#获取二进制数据
'''
#3、解析数据，提取我们想要的数据   视频url/标题/...
# 用re正则表达...
title=re.findall('<h1 title="(.*?)"',response.text)[0]
play_info=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]
# print(title)
print(play_info)#{"code":0,"message":双引号
print(type(play_info))#<class 'str'>


json_data=json.loads(play_info)#转成json
# print(json_data)#{'code': 0, 'message': 单引号
# print(type(json_data))#<class 'dict'>

pprint.pprint(json_data)   #格式化输出
aduio_url=json_data['data']['dash']['audio'][0]['baseUrl']
video_url=json_data['data']['dash']['video'][0]['baseUrl']

#解决403错误没有访问权限，加防盗链 20行： 'referer': 'https://www.bilibili.com/video/BV1T8411t7FF/?vd_source=6107ab45f572ee0819e6c78e0e6e0469',
# print(aduio_url)/
# print(video_url)
audio_content=requests.get(url=aduio_url,headers=headers).content
video_content=requests.get(url=video_url,headers=headers).content

with open('D:\\test\\'+title+'.mp3',mode='wb') as f:
    f.write(audio_content)
with open('D:\\test\\' + title + '.mp4', mode='wb') as f:
    f.write(video_content)
    # 视频链接
COMMAND=f'ffmpeg -i D:\\test\\{title}.mp4 -i D:\\test\\{title}.mp3 -c:v copy -c:a aac -strict experimental D:\\test\\{title}output.mp4'
subprocess.run(COMMAND,shell=True)