# -*- coding = utf-8 -*-
# @Time : 2021/5/18 15:30
# @Author : xuncheng
# @File : IpProxytest.py
# @Software : PyCharm

"""
使用requests请求代理服务器
请求http和https网页均适用
"""

import requests
import xlwt
import time

# 提取代理API接口，获取1个代理IP
api_url = "http://dev.qydailiip.com/api/?apikey=842777adcff6449ea9aae70ff2199dd0930aa5af&num=100&type=text&line=win&proxy_type=putong&sort=1&model=all&protocol=http&address=&kill_address=&port=3128&kill_port=&today=true&abroad=1&isp=1&anonymity=2"

# 获取API接口返回的代理IP
proxy_ip = requests.get(api_url).text
ipProxyList=proxy_ip.split("\r\n")
# print(ipProxyList)

# 用户名密码认证(私密代理/独享代理)
# username = "username"
# password = "password"
# proxies = {
#     "http": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip},
#     "https": "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy_ip}
# }
# print(proxies)

head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"
}

# 白名单方式（需提前设置白名单）
proxies = {
    "http": "http://%(proxy)s/" % {"proxy": proxy_ip},
    # "https": "http://%(proxy)s/" % {"proxy": proxy_ip}
}
print(proxies)

# 要访问的目标网页
target_url = "https://www.walletexplorer.com/wallet/Bitcoin.de/addresses?page=4"

# 使用代理IP发送请求
response = requests.get(target_url, proxies=proxies, headers=head)
print(response.status_code)
# 获取页面内容
if response.status_code == 200:
    print(response.text)
    # main()
