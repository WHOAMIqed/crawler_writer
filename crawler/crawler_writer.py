import json
import pymysql



def prem(db):
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)  # 结果表明已经连接成功
    cursor.execute("DROP TABLE IF EXISTS moviebiao")
    sql = """create table moviebiao(
    题目 varchar(100) not null, 
    分类排名 varchar(255) not null,
    链接 varchar(255) not null,
    电影类别 varchar(255) not null,
    评分 varchar(255) not null,
    国家 varchar(255) not null,
    海报链接 varchar(255) not null)
    """
    cursor.execute(sql)


def reviewdata_insert(db):

    with open(r'E:\abchomewrk\dict\Movie1.json', encoding='utf-8') as f:
        # demjson.decode(f)
        while True:

            try:
                print(u'开始载入数据......')
                lines = f.read()  # 不使用逐行读取的方法，逐行读取会出现问题
                review_text = json.loads(lines)
                for i in range(len(review_text["题目"])):
                    result = []
                    result.append((review_text["题目"][i], review_text["分类排名"][i], review_text["链接"][i], review_text["电影类别"][i],review_text["评分"][i],review_text["国家"][i],review_text["海报链接"][i]))
                    print(result)

                    inesrt_re = "insert into moviebiao(题目,分类排名,链接,电影类别,评分,国家,海报链接) values(%s,%s,%s,%s,%s,%s,%s)"
                    cursor = db.cursor()
                    cursor.executemany(inesrt_re, result)
                    db.commit()
            except Exception as e:
                db.rollback()
                print(str(e))
                print("载入完成")
                break


if __name__ == "__main__":  # 起到一个初始化或者调用函数的作用
    db = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123',
                       charset='utf8mb4',
                       database = "movie01")
    cursor = db.cursor()
    prem(db)
    reviewdata_insert(db)
    cursor.close()

















