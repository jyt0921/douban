# -*- coding = utf-8 -*-
# @Time :2022/10/7 23:21
# @Author :江银涛
# @File :test1.py
# @Software: PyCharm
import re
import time
import requests
from bs4 import BeautifulSoup
import os

# m = 'https://tse2-mm.cn.bing.net/th/id/OIP-C.uihwmxDdgfK4FlCIXx-3jgHaPc?w=115&amp;h=183&amp;c=7&amp;r=0&amp;o=5&amp;pid=1.7'
'''
resp = requests.get(m)
byte = resp.content
print(os.getcwd())
img_path = os.path.join(m)
'''

#爬取照片
def main():
    baseurl = 'https://www.bing.com/images/search?q=%E5%85%AC%E4%BA%A4%E8%BD%A6&go=%E6%90%9C%E7%B4%A2&qs=ds&form=QBIR&first=1'
    datalist = getdata(baseurl)


def getdata(baseurl):
    Img = re.compile(r'img.*src="(.*?)"')  # 正则表达式匹配图片
    datalist = []
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.41"}
    response = requests.get(baseurl, headers=head)  # 获取网页信息
    html = response.text  # 将网页信息转化为text形式
    soup = BeautifulSoup(html, "html.parser")  # BeautifulSoup解析html
    i = 0  # 计数器初始值
    data = []  # 存储图片超链接的列表
    for item in soup.find_all('img', src=""):  # soup.find_all对网页中的img—src进行迭代
        item = str(item)  # 转换为str类型
        Picture = re.findall(Img, item)  # 结合re正则表达式和BeautifulSoup, 仅返回超链接
        for b in Picture:  # 遍历列表，取最后一次结果
            data.append(b)
            i = i + 1
            datalist.append(data[-1])
    return datalist  # 返回一个包含超链接的新列表
    print(i)


'''
with open("img_path.jpg","wb") as f:
    f.write(byte)
'''

if __name__ == '__main__':
    os.chdir("D://testphonte")

    main()
    i = 0  # 图片名递增
    for m in getdata(
        baseurl='https://www.bing.com/images/search?q=%E5%85%AC%E4%BA%A4%E8%BD%A6&go=%E6%90%9C%E7%B4%A2&qs=ds&form=QBIR&first=1'):
        print(m)
        resp = requests.get(m)  # 获取网页信息
        byte = resp.content  # 转化为content二进制
        print(os.getcwd())  # os库中输出当前的路径
        i = i + 1  # 递增
        # img_path = os.path.join(m)
        with open("path{}.jpg".format(i), "wb") as f:  # 文件写入
            f.write(byte)
            time.sleep(0.1)  # 每隔0.1秒下载一张图片放入D://情绪图片测试
        print("第{}张图片爬取成功!".format(i))