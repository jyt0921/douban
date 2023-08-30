# -*- coding = utf-8 -*-
# @Time :2022/10/16 21:51
# @Author :江银涛
# @File :testXwit.py
# @Software: PyCharm


#将数据写入xls表格
import xlwt

workbook =xlwt.Workbook(encoding="utf-8")   #创建workbook对象
worksheet= workbook.add_sheet('sheet1')    #创建工作者
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d "%((i+1),(j+1),(i+1)*(j+1)))   #写入数据，第一行参数表示行，第二行表示列第三个表示内容
workbook.save('student.xls')   #保存数据表