# -*- coding = utf-8 -*-
# @Time :2022/10/7 22:17
# @Author :江银涛
# @File :spider.py
# @Software: PyCharm

from bs4 import BeautifulSoup          #页面解析，获取数据
import re           #正则表达式，进行文字匹配
import urllib.request,urllib.error          #指定URL，获取网页数据
import xlwt         #进行excel操作
import sqlite3      #进行sqllite数据库操作
import pymysql.cursors  #连接mysql数据库
#爬取豆瓣视频top250

def main():
    baseurl="https://movie.douban.com/top250?start="#网址
    #1、爬起网页
    datalist = getData(baseurl)
    savepath="豆瓣电影.xls"
    dbpath="movie.db"
    #3、保存数据
    # saveData(datalist,savepath)
    # conn(datalist,len(datalist))
    # askURL("https://movie.douban.com/top250?start=1")
#获取影片的超链接
findLink =re.compile(r'<a href="(.*?)">')   #compile()创建正则表达式对象，表示规则（字符串的模式）模板
#获取图片超链接
findImgSrc=re.compile(r'<img.*src="(.*?)" width="100"/>',re.S)  #re.S 让换行符包含在字符串中
#获取影片的片名
findtitle=re.compile(r'<span class="title">(.*?)</span>')
#影片的评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#影片的评价
findJudge =re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq =re.compile(r'<span class="inq">(.*)</span>')
#找到影片的内容
findBd =re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        print(url)
        print("******************88")
        html=askURL(url)#将要爬取页面全部设置
    # 2、解析数据
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item) #测试：查看电影item
            data=[] #保存一部电影的全部信息
            item=str(item)
            #获取影片的超链接
            link=re.findall(findLink,item)[0]  #re库通过正则表达式查找指定字符串 findLink 模板   item 表示电影  [0]表示出现的第几个这个案例中可能出现多个自己定义
            data.append(link)       #添加图片
            imgSrc=re.findall(findImgSrc,item)[0]
            data.append(imgSrc)     #添加链接
            title=re.findall(findtitle,item)
            if(len(title) == 2):
                ctitle=title[0]
                data.append(ctitle)         #添加中文名
                otitle=title[1].replace("/","")  #去掉无关的符号
                data.append(otitle)         #添加英文名
            else:
                data.append(title[0])   #中文名
                data.append(' ')        #外文名留空
            rating=re.findall(findRating,item)[0]
            data.append(rating)     #添加评分

            judge=re.findall(findJudge,item)[0]
            data.append(judge)      #添加评价人数

            inq=re.findall(findInq,item)
            if len(inq) != 0:
                inq=inq[0].replace("。"," ")
                data.append(inq)        #添加概述
            else:
                data.append(" ")

            bd=re.findall(findBd,item)[0]
            bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            data.append(bd.strip())  #去掉前后空格
            datalist.append(data)
    print("正在爬取第%d条",)
    return datalist

#得到指定一个url的网页内容
def askURL(url):
    head={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.34"
    }
    request =urllib.request.Request(url,headers=head)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

import xlwt
#保存数据到文件
def saveData(dataList,savepath):

    workbook = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    worksheet = workbook.add_sheet('豆瓣电影top250',cell_overwrite_ok=True)  # 创建工作者
    col=("影片链接","图片链接","影片中文名","影片英文名","评分","评价人数","概况","相关信息")
    for i in range(0,8):
        worksheet.write(0,i,col[i]) #列名字
    for i in range(0,250):
        print("第%d条数据"%i)
        data =dataList[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    #数据
    workbook.save(savepath)  # 保存数据表

#保存数据到数据库
def conn(datalist,num):           #改成自己的数据库信息即可
    conn = pymysql.connect(host='localhost',user='root',password='jiang123456',database='paperdata',cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    for i in range(0, num):
        print(f"--------------正在保存第{i + 1}条--------------")
        list = datalist[i]
        data1 = tuple(list)
        sql = 'insert into movie250(info_link,pic_link,cname,ename,score,rated,instroduction,info) values(%s,%s,%s,%s,%s,%s,%s,%s)' #五个字符串对应MySQL的列名
        try:
            cursor.execute(sql,data1)
            conn.commit()
        except Exception as e:
            print('插入数据失败', e)
            conn.rollback()  # 回滚
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()



if __name__ == "__main__":
    main()