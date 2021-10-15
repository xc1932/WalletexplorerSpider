# -*- coding = utf-8 -*-
# @Time : 2021/5/15 17:36
# @Author : xuncheng
# @File : pythonbase.py
# @Software : PyCharm

import keyword
import random
import time
import os
import xlwt

# 1.语法基础
# 1.1注释
# 第一个python程序
'''
多行注释
多行注释
多行注释
'''

# 1.2关键字
# print(keyword.kwlist)

# 1.3输出
# 1.3.1标准输出
# print("标准化输出字符串")
# a = 10
# print("这是变量：", a)
# 1.3.2格式化输出
# age = 18
# print("我的年纪是：%d岁" % age)
# print("我的名字是%s,我的国籍是%s" % ("小张", "中国"))
# 1.3.3字符串连接
# print("www", "baidu", "com")
# print("www", "baidu", "com", sep=".")
# print("www", "baidu", "com", sep="")
# print("hello", end="")
# print("world", end="\t")
# print("python", end="\n")
# print("end")
# print("123456789\n")

# 1.4输入
# password = input("请输入密码:")
# print("您刚刚输入的密码是：", password)

# 1.5类型
# print("输入的类型：", type(password))
# aa = int("123")
# print("类型：", type(aa))
# b = aa + 100
# print(b)

# 1.6条件判断
# 1.6.1注意缩进
# if True:
#     print("true")
#     print("answer")
# else:
#     print("False")
# print("end")
# 1.6.2 elif使用
# score = 67
# if score >= 90 and score <= 100:
#     print("本次考试，等级A")
# elif score >= 80 and score < 90:
#     print("本次考试，等级为B")
# else:
#     print("本次考试，等级为C")
# 1.6.3嵌套
# sex = "woman"
# marryState = "single"
# if sex == "man":
#     print("男生")
#     if marryState == "single":
#         print("给你介绍一个")
#     else:
#         print("恭喜恭喜")
# else:
#     print("女生")

# 1.7for循环
# 1.7.1循环数字
# 最普通
# for i in range(10):
#     print(i)
# 带步进值
# for i in range(0, 13, 3):
#     print(i)
# 反向
# for i in range(-10,-101,-30):
#     print(i)
# 1.7.2循环字符串
# name = "xuncheng"
# for x in name:
#     print(x, end="\t")
# 1.7.3循环列表
# 带索引
# a = ["aa", "bb", "cc", "dd"]
# for i in range(len(a)):
#     print(i, a[i])
# 不带索引
# a = ["aa", "bb", "cc", "dd"]
# for i in a:
#     print(i)

# 1.8while循环
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count += 1
# else:
#     print(count, "大于或等于5")

# 1.9break、continue
# 1.9.1break
# i = 0
# while i < 10:
#     i = i + 1
#     print("-" * 30)
#     if i == 5:
#         break
#     print(i)
# 1.9.2continue
# i = 0
# while i < 10:
#     i = i + 1
#     print("-" * 30)
#     if i == 5:
#         continue
#     print(i)

# 1.10引入随机库
# x = random.randint(0, 2)
# print(x)

# 1.11字符串
# 1.11.1
# word='字符串'
# sentence="这是一个句子"
# paragraph="""
#         这是一个段落
#         可以由多行组成
# """
# print(word)
# print(sentence)
# print(paragraph)
# print("123")
# 1.11.2
# my_str1="I'm a student"
# my_str2='I\'m a student'
# my_str3="Jason said \"I like you\""
# my_str4='Jason said "I like you"'
# print(my_str1)
# print(my_str2)
# print(my_str3)
# print(my_str4)
# 1.11.3
# str = "chengdu"
# print(str[2])
# print(str[0:5])
# print(str[1:7:2])
# print(str[:5])
# print(str[5:])
# print(str+",你好")
# print(str*3)
# print("hello\nchengdu")
# print(r"hello\nchengdu")

# 1.12列表
# 1.12.1列表定义
# namelist = []  # 定义空列表
# namelist = ["小张", "小王", "小李"]
# testlist = [1, "测试"]
# print(type(testlist[0]))
# print(type(testlist[1]))
# print(namelist[0])
# print(namelist[1])
# print(namelist[2])
# 1.12.2列表操作
# namelist = ["小张", "小王", "小李"]
# print("列表增加前：")
# for name in namelist:
#     print(name,end="\t")
# a.长度
# print("长度：%d"%len(namelist))
# b.增加
# （1）
# print("列表增加后：")
# namelist.append("小刘")
# for name in namelist:
#     print(name,end="\t")
# （2）
# a=[1,2]
# b=[3,4]
# a.append(b)
# print(a)
# a.extend(b)
# print(a)
# （3）
# a=[0,1,2]
# a.insert(1,3)
# print(a)
# c.删除
# moiveName=["加勒比海盗","黑客帝国","第一滴血","指环王","速度与激情","指环王"]
# print("列表删除前：")
# for name in moiveName:
#     print(name,end="\t")
# print("\n")
# （1）
# del moiveName[2]
# （2）
# moiveName.pop()
# （3）
# moiveName.remove("指环王")
# print("列表删除后：")
# for name in moiveName:
#     print(name,end="\t")
# print("\n")
# d.改
# namelist = ["小张", "小王", "小李"]
# print("列表修改前：")
# for name in namelist:
#     print(name, end="\t")
# print("\n")
# namelist[1] = "小红"
# print("列表修改后：")
# for name in namelist:
#     print(name, end="\t")
# print("\n")
# e.查
# （1）
# namelist = ["小张", "小王", "小李"]
# if "小王" in namelist:
#     print("找到")
# else:
#     print("没找到")
# （2）
# a = ["a", "b", "c", "a", "b"]
# print(a.index("a", 0, 4))
# print(a.index("a", 1, 4))
# （3）
# a = ["a", "b", "c", "a", "b"]
# print(a.count("a"))
# f.反转和排序
# namelist = ["小张", "小王", "小李"]
# namelist.reverse()
# print(namelist)
# namelist.sort()
# print(namelist)
# namelist.sort(reverse=True)
# print(namelist)
# 1.12.3多维列表
# number = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(number[1][2])

# 1.13元组
# 1.13.1元组创建
# tup1=()         #创建空元组
# tup2=(50)
# tup3=(50,)
# tup4=(50,60,70)
# print(type(tup1))
# print(type(tup2))
# print(type(tup3))
# print(type(tup4))
# 1.13.2元组操作
# a.基本操作
# tup1 = ("abc", "def", 2000, 2020, 333, 444, 555, 666)
# print(tup1[0])
# print(tup1[-1])
# print(tup1[1:5])
# b.增
# tup1 = (12, 34, 56)
# tup2 = ("abc", "xyz")
# tup = tup1 + tup2
# print(tup)
# c.删
# tup1 = (12, 34, 56)
# print(tup1)
# del tup1  # 删除整个元组

# 1.14字典
# 1.14.1字典创建和访问
# info = {"name": "吴彦祖", "age": 18}
# print(info["name"])
# print(info["age"])
# print(info.get("gender"))
# print(info.get("gender", "m"))
# print(info.get("age", 20))
# 1.14.2字典操作
# a.增
# info = {"name": "吴彦祖", "age": 18}
# info["id"]="123"
# print(info["id"])
# print(info)
# b.删
# info = {"name": "吴彦祖", "age": 18}
# del info["name"]
# print(info)
# del info
# c.清空
# info = {"name": "吴彦祖", "age": 18}
# info.clear()
# print(info)
# d.改
# info = {"name": "吴彦祖", "age": 18}
# info["age"] = 20
# print(info["age"])
# e.查
# info = {"name": "吴彦祖", "age": 18}
# print(info.keys())
# print(info.values())
# print(info.items())
# f.遍历
# （1）
# info = {"name": "吴彦祖", "age": 18}
# for key in info.keys():
#     print(key)
# for value in info.values():
#     print(value)
# for key, value in info.items():
#     print("key=%s,value=%s" % (key, value))
# （2）
# mylist = ["a", "b", "c", "d"]
# for i, x in enumerate(mylist):
#     print(i, x)

# 1.15集合

# 1.16函数
# 1.16.1函数的定义和调用
# （1）无参
# def printinfo():
#     print("-" * 30)
#     print("     人生苦短，别用python       ")
#     print("-" * 30)
# printinfo()
# （2）带参
# def add2Num(a, b):
#     c = a + b
#     print(c)
# add2Num(11, 22)
# （3）带返回值
# def add2Num(a, b):
#     return a + b
# print(add2Num(11, 33))
# （4）带多个返回值
# def divid(a, b):
#     shang = a / b
#     yushu = a % b
#     return shang, yushu
# sh, yu = divid(5, 2)
# print("商：%d,余数：%d" % (sh, yu))

# 1.17全局变量和局部变量
# 1.17.1局部变量
# def test1():
#     a = 300
#     print("test1----修改前：a=%d" % a)
#     a = 100
#     print("test1----修改后：a=%d" % a)
#
# def test2():
#     a = 500
#     print("test2----a=%d" % a)
#
# test1()
# test2()
# 1.17.2全局变量
# a=100
# def test1():
#     global a
#     print("test1----修改前：a=%d" % a)
#     a = 200
#     print("test1----修改后：a=%d" % a)
#
# def test2():
#     print("test2----a=%d" % a)
#
# test1()
# test2()

# 1.18文件操作
# 1.18.1写文件
# f = open("test.txt", "w")
# f.write("hello world,i am here!")
# f.close()
# 1.18.2读文件
# （1）
# f = open("test.txt", "r")
# content = f.read(5)
# print(content)
# content = f.read(10)
# print(content)
# f.close()
# （2）
# f = open("test.txt", "r")
# content = f.readlines()
# print(content)
# i = 1
# for temp in content:
#     print("%d:%s" % (i, temp),end="")
#     i = i + 1
# f.close()
# （3）
# f = open("test.txt", "r")
# content = f.readline()
# print("1:%s"%content)
# content = f.readline()
# print("2:%s"%content)
# f.close()
# 1.18.3文件重命名
# os.rename("test.txt", "test1.txt")

# 1.19错误与异常
# 1.19.1    try...except...
# （1）
# try:
#     print("-----test-----1---")
#     f = open("123.txt", "r")
#     print("-----test-----2---")
#     print(num)
# except (NameError, IOError) as result:
#     print("产生了错误")
#     print(result)
#     pass
# （2）
# try:
#     print("-----test-----1---")
#     f = open("123.txt", "r")
#     print("-----test-----2---")
#     print(num)
# except Exception as result:
#     print("产生了错误")
#     print(result)
#     pass
# 1.19.2    try...except...finally
# try:
#     f = open("test1.txt", "r")
#     try:
#         while True:
#             content=f.readline()
#             if len(content)==0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
#         print("文件关闭")
# except Exception as result:
#     print("产生了错误")
#     print(result)
#     pass

# list=["1","2","3"]
# print(list)
# list=[1,2,3,4]
# print(list)
#
# del list[len(list)-1]
# # print(list)
# list1=["1","2","3"]
# print(list1)
# list2=[1,2,3,4]
# print(list2)
# list2.append(5)
# # print(list2)
# # list2.append(list1)
# # print(list2)
# list2+=list1
# print(list2)

# book = xlwt.Workbook(encoding="utf-8", style_compression=0)
# sheet = book.add_sheet('豆瓣电影', cell_overwrite_ok=True)
# # book.save('../walletexplorer1.xls')
# book.save(r'.\AddressResult\address.xls')
# ip_proxy=""
# print(ip_proxy=="")
set1=set()
print(set1)
set1.add("123")
set1.add("123456")
set1.add("123456")
print(set1)
set2=set('abcd')
print(set2)#{'b', 'a', 'd', 'c'}
