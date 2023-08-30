# -*- coding = utf-8 -*-
# @Time :2022/10/15 21:57
# @Author :江银涛
# @File :testzz.py
# @Software: PyCharm


#正则表达式

import re

#创建模式对象
pat =re.compile("AA") #此处的AA，是正则表达式，用来验证其它的字符串
m =pat.search("CABAABAA") #search字符串被校验的内容（但只能查找到第一次出现的地方）    显示为：<re.Match object; span=(3, 5), match='AA'>//span表示地址
print(m)


#没有模式对象
n=re.search("asd","Aasd")#前面的字符串是规则（模板样板）后面的表示被校验的对象
print(n)

print("*"*50)
print(re.findall("B","CASDBSDABB"))
print(re.findall("[A-Z]","ASVASDASD"))#['A', 'S', 'V', 'A', 'S', 'D', 'A', 'S', 'D']
print(re.findall("[A-Z]+","ASVASDASD"))#['ASVASDASD']

print("*"*50)

print(re.sub("a","A","acsacda"))#找到第一个字符串换成第二个    print : AcsAcdA

#建议在正则表达式中，被比较的字符串前加上r 不用担心转义字符问题
a=r"\aabdd-\'"
print(a)#\aabdd-\'
b="\aabdasd-\'"#abdasd-'
print(b)




