
#1.引入pymysql
import pymysql
#2.连接数据库
mydb=pymysql.connect(
    host='172.16.2.210',
    port=3306,
    user='root',
    passwd='Moore@2019',
    db='eom',
    charset='utf8')
#3..创建游标对象
cur=mydb.cursor()

#5.获取数据
str="select * from enterprise_code_data"
cur.execute(str)
data=cur.fetchone()
print(data)#这里就是获取的数据

#6.关闭数据库
mydb.close()

