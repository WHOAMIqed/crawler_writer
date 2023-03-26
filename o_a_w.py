# import pymysql
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123', db='data',charset='utf8')
# cur = conn.cursor()
# cur.execute("insert into datanew1 values ('李华','lihua')")
# conn.commit()
# cur.close()
# conn.close()
import pymysql

# 打开数据库连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123',
                       charset='utf8'
                       )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("show data;")
cursor.execute("use data;")
cursor.execute("show datanew1")
cursor.execute("select 1 from datanew1")

# 使用 fetchone() 方法获取单条数据;使用 fetchall() 方法获取所有数据
data = cursor.fetchall()
for item in data:
    print(item)

# 关闭数据库连接
cursor.close()