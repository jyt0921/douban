# -*- coding = utf-8 -*-
# @Time :2022/10/17 15:07
# @Author :江银涛
# @File :testre.py
# @Software: PyCharm
import re

str = "33规则这个字符串是否匹配"
print(re.findall("^33", str))  # 字符串开始位置与匹配规则符合就匹配且打印匹配内容，否则不匹配，返回值是list

