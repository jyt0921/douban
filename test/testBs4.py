# -*- coding = utf-8 -*-
# @Time :2022/10/8 9:49
# @Author :江银涛
# @File :testBs4.py
# @Software: PyCharm
import re
import typing

from bs4 import BeautifulSoup

file=open("yy.html","rb")
html=file.read()
bs=BeautifulSoup(html,"html.parser")#解析器


print(bs.title)
print(bs.a)#只能拿到第一个值
#1.tag 标签及其内容：拿到他所找到的第一个内容

# print(bs.title.string)
# print(type(bs.title.string))
#2.string    标签里的内容（字符串）

# print(bs.a.attrs)


print(type(bs))
#3.BeautifulSoup   表示整个文档

print(bs.name)
# print(bs.attrs)
print(bs.input.String)



#文档的遍历
print(bs.head.contents)
#https://beautifulsoup.cn/
#遍历文档树
print("*"*50)

#文档的搜索
# t_list=bs.find_all("input")
# print(t_list)
# for name in t_list:
#     print(name)

import re
#正则表达式搜索：使用search（）方法匹配内容"标签的任意东西"
t_list=bs.find_all(re.compile("in"))#"a"    "某个标签的一部分"
# print(t_list)


#方法 ：传入一个函数（方法），根据函数的要求来搜索(了解)自己定义函数查询
# def name_is_exists(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# print(t_list)



#2、kwargs   参数
'''
t_list=bs.find_all(id="username")#id可以
for item in t_list:
    print(item)


t_list=bs.find_all(name="username")#name不行
for item in t_list:
    print(item)

t_list=bs.find_all(class_=True)#搜索带class
for item in t_list:
    print(item)

t_list=bs.find_all(href="http://news.baidu.com")
for item in t_list:
    print(item)
'''


#3、text参数

# t_list=bs.find_all(text="hao123")
# t_list =bs.find_all(text=re.compile("\d"))#应用正则表达式来查找包含特定文本的内容（标签里的字符串）即\d表示数字


#4、limit参数
'''
t_list=bs.find_all("a",limit=3)#限制能获得多少个

for item in t_list:
    print(item)
'''
#css选择器
print(bs.select('title'))#通过标签查找
print(bs.select('id'))#通过id查找
print(bs.select())

for item in t_list:
    print(item)