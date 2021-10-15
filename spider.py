# -*- coding = utf-8 -*-
# @Time : 2021/5/16 22:01
# @Author : xuncheng
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import time
import sqlite3


def main():
    # 1.爬去网页
    baseUrl = "https://movie.douban.com/top250?start="
    dataList = getData(baseUrl)
    # 3.保存数据
    savePath = ".\\豆瓣电影Top250.xls"
    saveData(dataList, savePath)


# 匹配影片详情链接正则
findLink = re.compile(r'<a href="(.*?)">')
# 匹配影片图片正则
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# 匹配影片名正则
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 匹配影片评分正则
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 匹配评价人数正则
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 匹配影片概况正则
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 匹配影片相关内容正则
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = askURL(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)
            # print(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                otitle = re.sub('\xa0', "", otitle)
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            rating = re.findall(findRating, item)[0]
            data.append(rating)
            judgeNum = re.findall(findJudge, item)[0]
            data.append(judgeNum)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(" ")
            bd = re.findall(findBd, item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?', " ", bd)
            bd = re.sub('/', " ", bd)
            bd = re.sub('\xa0', "", bd)
            data.append(bd.strip())
            dataList.append(data)
    return dataList


# 得到指定一个URL的网页内容
def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def saveData(dataList, savePath):
    print("save......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接", "图片链接", "影片中文名", "影片外国名", "评分", "评价数", "概况", "相关信息")
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = dataList[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    book.save('豆瓣Top250.xls')


if __name__ == "__main__":
    main()
