import pymysql


conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123',
                       charset='utf8',
                       database = "data"
                       )
cursor = conn.cursor()
name_to_search = str(input("the name to search:"))
sql = "SELECT * FROM datanew2 WHERE name = '%s';"%name_to_search
try:
    cursor.excute(sql)
    response = cursor.fetchall()
    print(response[1])
except:
    print("SORRY! No result!")
conn.close()
