# -*- coding = utf-8 -*-
# @Time : 2021/5/18 16:31
# @Author : xuncheng
# @File : IPProxySpider.py
# @Software : PyCharm

from bs4 import BeautifulSoup
import requests
import xlwt
import xlrd
import threading
import time
import json

# 1.获取代理IP链接
api_url = "http://dev.qydailiip.com/api/?apikey=842777adcff6449ea9aae70ff2199dd0930aa5af&num=300&type=text&line=win&proxy_type=putong&sort=1&model=all&protocol=https&address=&kill_address=&port=&kill_port=&today=true&abroad=&isp=&anonymity=2"
# 2.抓取的目标网址
target_BaseUrl = "https://www.walletexplorer.com/wallet/BTC-e.com-output/addresses?page="
# 3.结果保存路径
sheetBookPath = r'.\AddressResult\BTCeOutput.xls'
# 4.伪装请求头信息
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}


# (1).获取API接口返回的代理IP列表
def getIPProxys(api_url, printMark):
    proxy_ip = ""
    while proxy_ip == "":
        try:
            proxy_ip = requests.get(api_url, timeout=3).text
        except Exception as e:
            print("\n获取IP代理失败!!!", end="")
    ipProxyList = proxy_ip.split("\r\n")
    del ipProxyList[len(ipProxyList) - 1]
    if printMark == True:
        print(ipProxyList)
    return ipProxyList


# (2).获取一个页面的地址
def getAddressForOnePage(html):
    tempAddressList = []
    soup = BeautifulSoup(html, "html.parser")
    for item in soup.select("tr>td>a"):
        tempAddressList.append(item.getText())
    return tempAddressList


# (3).获取调用一次API代理接口得到的页面地址数据
def getData(threadName, nextPage, lastPage):
    ipProxyList = getIPProxys(api_url, False)
    print("\n" + threadName + ":代理数量:" + str(len(ipProxyList)), end="")
    tempAddressList = []
    page = nextPage
    count = 0
    for proxy_ip in ipProxyList:
        count += 1
        proxies = {
            # "http": "http://%(proxy)s" % {"proxy": proxy_ip},
            "https": "https://%(proxy)s" % {"proxy": proxy_ip}
        }
        try:
            response = requests.get(target_BaseUrl + str(page), proxies=proxies, headers=head,
                                    timeout=3)  # , timeout=(30, 70)
            if response.status_code == 200:
                print("\n" + threadName + ":代理" + str(count) + ":" + proxies['https'] + ",获取第" + str(page) + "页数据成功!!!",
                      end="")
                print("\n" + threadName + ":状态码:" + str(response.status_code) + "\t响应时间:" + str(response.elapsed),
                      end="")
                html = response.text
                tempAddressList += getAddressForOnePage(html)
                page += 1
            else:
                print("\n" + threadName + ":代理" + str(count) + ":" + proxies['https'] + ",获取第" + str(page) + "页数据失败!!!",
                      end="")
                print("\n" + threadName + ":状态码:" + str(response.status_code) + "\t响应时间:" + str(response.elapsed),
                      end="")
        except Exception as e:  # 捕获请求walletexplorer异常(超时和429)
            print("\n" + threadName + ":代理" + str(count) + ":" + proxies['https'] + ",获取第" + str(
                page) + "页数据失败!!!访问网页超时......", end="")
        if page > lastPage:
            break
    return tempAddressList, page


# (4).获取指定页面范围的地址数据
def getDataFromRangePage(threadName, firstPage, lastPage):
    addressList = []
    startPage = firstPage
    while startPage <= lastPage:
        tempAddressList, page = getData(threadName, startPage, lastPage)
        if page > startPage:
            addressList += tempAddressList
            startPage = page
    return addressList


# (5).保存数据
def saveData(dataList, sheetbook, sheetName):
    sheet = sheetbook.add_sheet(sheetName, cell_overwrite_ok=True)
    dataAmount = len(dataList)
    for i in range(0, dataAmount):
        sheet.write(i, 0, dataList[i])
    return sheetbook


# (6).获取并保存一定范围页面的地址数据
def getDataAndSaveForRangePages(threadName, firstPage, lastPage, sheetBook, sheetName):
    tempAddressList = getDataFromRangePage(threadName, firstPage, lastPage)
    print("\n" + threadName + ":开始保存数据......", end="")
    sheetBook = saveData(tempAddressList, sheetBook, sheetName)
    sheetBook.save(sheetBookPath)
    print("\n" + threadName + ":" + sheetName + "保存成功。", end="")


# (7).定义线程类
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, firstPage, lastPage, sheetBook, sheetName):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.firstPage = firstPage
        self.lastPage = lastPage
        self.sheetBook = sheetBook
        self.sheetName = sheetName

    def run(self):
        print("\n" + "开始线程：" + self.name, end="")
        getDataAndSaveForRangePages(self.name, self.firstPage, self.lastPage, self.sheetBook, self.sheetName, )
        print("\n" + "退出线程：" + self.name, end="")


# (8).多线程抓取网页数据1
def getDataForMultiThread(pageAmount, threadAmount):
    sheetBook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    threadList = []
    threadNameList = []
    pagesOfThreadList = []
    pageAmountForOneThread = (int)(pageAmount / threadAmount)
    for i in range(0, threadAmount):
        threadNameList.append("Thread-" + str(i + 1))
        pagesOfThreadList.append(pageAmountForOneThread)
    restPages = pageAmount - (threadAmount * pageAmountForOneThread)
    for i in range(0, restPages):
        pagesOfThreadList[i] += 1
    startPage = 1
    for t in range(0, threadAmount):
        lastPage = startPage + pagesOfThreadList[t] - 1
        sheetName = "Page" + str(startPage) + "-" + str(lastPage)
        threadNum = t + 1
        threadList.append(
            myThread(threadNum, "Thread-" + str(threadNum), threadNum, startPage, lastPage, sheetBook, sheetName))
        # print(str(startPage)+","+str(lastPage)+","+str(pagesOfThreadList[t])+","+sheetName)
        startPage += pagesOfThreadList[t]
    # 开启新线程
    for i in range(0, threadAmount):
        threadList[i].start()
    for i in range(0, threadAmount):
        threadList[i].join()
    print("\n退出主线程", end="")


# (9).(*****多线程抓取网页数据2*****)
def getDataForMutiThreadTwo(startPage, finishPage, threadAmount):
    sheetBook = xlwt.Workbook(encoding="utf-8", style_compression=0)
    threadList = []
    threadNameList = []
    pagesOfThreadList = []
    pageAmount = finishPage - startPage + 1
    pageAmountForOneThread = (int)(pageAmount / threadAmount)
    for i in range(0, threadAmount):
        threadNameList.append("Thread-" + str(i + 1))
        pagesOfThreadList.append(pageAmountForOneThread)
    restPages = pageAmount - (threadAmount * pageAmountForOneThread)
    for i in range(0, restPages):
        pagesOfThreadList[i] += 1
    for t in range(0, threadAmount):
        lastPage = startPage + pagesOfThreadList[t] - 1
        sheetName = "Page" + str(startPage) + "-" + str(lastPage)
        threadNum = t + 1
        threadList.append(
            myThread(threadNum, "Thread-" + str(threadNum), threadNum, startPage, lastPage, sheetBook, sheetName))
        # print(str(startPage)+","+str(lastPage)+","+str(pagesOfThreadList[t])+","+sheetName)
        startPage += pagesOfThreadList[t]
    # 开启新线程
    for i in range(0, threadAmount):
        threadList[i].start()
        time.sleep(5)
    for i in range(0, threadAmount):
        threadList[i].join()
    print("\n退出主线程", end="")
    pass


# (10).顺序获取xls中的sheet表名
def getSheetNameFromxls_Sorted(xlsPath):
    xls_file = xlrd.open_workbook(xlsPath)
    sheetNameList = xls_file.sheet_names()
    sheetNameListBackup = xls_file.sheet_names()
    for i in range(0, len(sheetNameList)):
        sheetNameList[i] = sheetNameList[i].split("-")[0]
        sheetNameList[i] = int(sheetNameList[i][4:len(sheetNameList[i])])
    sheetNameList.sort()
    for s in range(0, len(sheetNameList)):
        sheetNameList[s] = str(sheetNameList[s])
    finalSheetNameList = []
    for index in sheetNameList:
        for name in sheetNameListBackup:
            nameBackup = name
            name = name.split("-")[0]
            name = name[4:len(name)]
            if name == index:
                finalSheetNameList.append(nameBackup)
                continue
    return finalSheetNameList


# (11).(*****从xls中获取数据*****)
def getDataFromxls(xlsPath):
    addressSet = set()
    xls_file = xlrd.open_workbook(xlsPath)
    sortedSheetNameList = getSheetNameFromxls_Sorted(xlsPath)
    for sheetName in sortedSheetNameList:
        sheet = xls_file.sheet_by_name(sheetName)
        for i in range(sheet.nrows):
            addressSet.add(sheet.cell(i, 0).value)
    return addressSet


# (12).将数据序列化保存
def saveAddressSetAsJsonFomat(addressSet, filePath):
    addressListFromSet = []
    for address in addressSet:
        addressListFromSet.append(address)
    with open(filePath, 'w') as pf:
        json.dump(addressListFromSet, pf, indent=2, sort_keys=True)
        pf.close()


# (13).将xls中的数据按json格式序列化为txt文件
def changeToTxtFileAsJson(xlsPath, txtFilePath):
    addressSet = getDataFromxls(xlsPath)
    saveAddressSetAsJsonFomat(addressSet, txtFilePath)


if __name__ == "__main__":
    # 1.多线程爬取网页数据
    # 使用爬取网页功能时请修改:(1)抓取网页URL   (2)结果保存路径(保存结果为xls格式)   (3)IP代理池获取地址(购买后使用)
    # IP代理池生成推荐选择:(1)一次300个 (2)不指定运营商和过滤条件(国内外都可以)   (3)高匿  (4)代理协议根据爬取的目标网址选择
    # (5)代理模式不限 (6)验证时间从近到远 (7)当天过滤 ON  (8)返回格式 txt
    # getDataForMultiThread(777, 10)
    # getDataForMutiThreadTwo(157, 234, 10)
    # getDataForMutiThreadTwo(1, 34, 15)
    # 2.将爬去的网页数据从xls文件中提取出来并序列化保存
    # xlsPath = r'.\AddressResult\BTCeOutput.xls'
    # txtFilePath = r'.\AddressResult\BTCeOutput.txt'
    # changeToTxtFileAsJson(xlsPath, txtFilePath)
    pass
