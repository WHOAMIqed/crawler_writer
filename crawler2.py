import pymysql
import json
# 打开数据库连接
path = open(r"E:\abchomewrk\dict\jsonDataFile.josn","r",encoding="utf-8")
dictoutput = path.read()
dictjson = json.loads(dictoutput)
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123',
                       charset='utf8mb4',
                       database = "data"
                       )
sql = "CREATE TABLE experiment ('name' VARCHAR(255) NOT NULL,'engname' VARCHAR(255) DEFAULT NULL)CHARSET = utf8"
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
KEY = [i for i in dictjson.keys()]
value = [i for i in dictjson.values()]
lent = len(dictjson)
name,engname = zip(*dictjson.items())
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("show data;")
# cursor.execute("use data;")
# cursor.execute("show datanew1")
# cursor.execute("select 1 from datanew1")
datall = []
for i in range(lent):
    datall.append([KEY[i],value[i]])
table = "datanew2"
cursor.executemany("INSERT INTO datanew2(name,engname) VALUES(%s,%s)",datall)
# # 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
# data = cursor.fetchall()
# for item in data:
#     print(item)

# 关闭数据库连接
conn.commit()
cursor.close()