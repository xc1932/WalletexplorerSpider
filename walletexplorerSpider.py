# -*- coding = utf-8 -*-
# @Time : 2021/5/16 23:48
# @Author : xuncheng
# @File : walletexplorerSpider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import urllib.request, urllib.error
import xlwt
import time
import sqlite3
import re

pageAmount=293

def main():
    # 1.爬去网页
    baseUrl = "https://www.walletexplorer.com/wallet/Huobi.com/addresses?page="
    dataList = getData(baseUrl)
    # 3.保存数据
    savePath = ".\\HuobiAddresses.xls"
    saveData(dataList, savePath)

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

# 爬取网页
def getData(baseUrl):
    dataList = []
    global pageAmount
    for i in range(1, pageAmount+1):
        url = baseUrl + str(i)
        print("第%d次请求数据"%i)
        html = askURL(url)
        print(html)
        time.sleep(5)
        # print(html)
        # break
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.select("tr>td>a"):
            dataList.append(item.getText())
    return dataList


# 保存数据
def saveData(dataList, savePath):
    print("save......")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('Huobi.com', cell_overwrite_ok=True)
    amount=len(dataList)
    for i in range(0, amount):
        if i%100==0:
            print("第%d个地址" % i)
        data = dataList[i]
        sheet.write(i, 0, data)
    book.save('walletexplorer.xls')


if __name__ == "__main__":
    main()
