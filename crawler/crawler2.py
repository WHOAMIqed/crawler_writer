import pymysql
import json


# 打开数据库连接
path = open(r"E:\abchomewrk\dict\Movie1.json","r",encoding="utf-8")
dictoutput = path.read()
dictjson = json.loads(dictoutput)
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123',
                       charset='utf8mb4',
                       database = "movie01"
                       )
# sql = "CREATE TABLE experiment ('name' VARCHAR(255) NOT NULL,'engname' VARCHAR(255) DEFAULT NULL)CHARSET = utf8"
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
KEY = [i for i in dictjson.keys()]
value = [i for i in dictjson.values()]
lent = len(dictjson)
name,engname = zip(*dictjson.items())
datall = []
for i in range(lent):
    datall.append([KEY[i],value[i]])
table = "moviebiao"
cursor.executemany("INSERT INTO moviebiao(题目,分类排名) VALUES(%s,%s)",datall)
conn.commit()
cursor.close()