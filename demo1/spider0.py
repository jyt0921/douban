# -*- coding = utf-8 -*-
# @Time :2022/10/17 15:33
# @Author :江银涛
# @File :spider0.py
# @Software: PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import pymysql.cursors
#爬取知乎热点事件
def main():
    baseurl="https://www.zhihu.com/billboard"
    datalist=getDatad(baseurl)
    savepath = "知乎.xls"
    saveData(datalist,savepath)
    # conn(datalist,len(datalist))
    # askURL("https://www.zhihu.com/")#用于测试是否能爬取到页面

findnum = re.compile(r'<div class="HotList-itemIndex HotList-itemIndexHot">(.*?)</div>')
findnum0 = re.compile(r'<div class="HotList-itemIndex">(.*?)</div>')
findname=re.compile(r'<div class="HotList-itemTitle">(.*?)</div>')
findredu=re.compile(r'<div class="HotList-itemMetrics">(.*?)</div>')
findimgsrc=re.compile(r'src="(.*?)"')
def getDatad(baseurl):
    datalist=[]
    # print("333")
    html=askURL(baseurl)
    # print(html)
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('a',class_="HotList-item"):
        data=[]
        item=str(item)
        # print("1111")
        num=re.findall(findnum,item)
        if(len(num)==0):
            print(num)
            num = re.findall(findnum0, item)
        # print(num)
        data.append(num)
        name=re.findall(findname,item)
        data.append(name)
        redu=re.findall(findredu,item)
        data.append(redu)
        imgsrc=re.findall(findimgsrc,item)
        data.append(imgsrc)
        datalist.append(data)

    print(datalist)
    return datalist

#保存数据
def saveData(dataList,savepath):

    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('知乎热度',cell_overwrite_ok=True)  # 创建工作者
    col=("序号","主题","热度","图片链接")
    for i in range(0,4):
        worksheet.write(0,i,col[i]) #列名字
    for i in range(0,49):
        print("第%d条数据"%i)
        data =dataList[i]
        for j in range(0,4):
            worksheet.write(i+1,j,data[j])
    #数据
    workbook.save(savepath)  # 保存数据表

#修改Agent
def askURL(url):
    head={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__=="__main__":
    main()