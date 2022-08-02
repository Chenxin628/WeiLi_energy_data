import pymysql
connect = pymysql.connect(
    host='172.16.2.210/',  # 服务器名字
    port=3306,  # 端口号
    user='root',  # 登录名
    passwd='Moore@2019',  # 密码
    db='eom',  # 数据库名
    charset='utf8'
)
# 创建游标对象
cursor = connect.cursor()  # cursor当前的程序到数据之间的链接管道
# 组装sql语句，需要查询的MySQL语句
sql = "select * from enterprise_code_data a where a.stat_type = '1,2';"
# 执行sql语句
cursor.execute(sql)
# 处理结果
# 获取一条数据
one = cursor.fetchone()  # 获取当前查询结果第一条数据
print("获取一条数据:")
print(one)
# 获取多条数据 传入需要获取的数据的条数
print("获取多条数据 传入需要获取的数据的条数:")
many = cursor.fetchmany(3)  # 获取当前查询结果前3条数据
print(many)
# 获取所有数据
print("获取所有数据:")
all = cursor.fetchall()
 # 输出获取到的数据的数据类型
print(all)
print("获取所有数据1:")
print(type(all))  # <class 'tuple'>结果是数组

   # 逐条输出获取到的数据类型及数据
# print("单条数据依然是数组:")
# for each in all:
#         print(type(each), each)  # 单条数据依然是数组

#     # 获取数据库表中列的参数
# fields = cursor.description  # 取得是字段的名字的一些详细信息是元组
# print(fields)  # (('id', 3, None, 11, 11, 0, False), ('create_user_id', 3, None, 11, 11, 0, True), ('create_date', 12, None, 19, 19, 0, True)
# head = []
#     # 或取数据库中表头
# for field in fields:
#     head.append(field[0])  # 只取元组下标为零的即字段名字
# print(head)

    # 6.关闭所有的连接
    # 关闭游标
cursor.close()
    # 关闭数据库
connect.close()
