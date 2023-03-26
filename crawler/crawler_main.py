import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
title_list=[]
lianjie_list=[]
rank_list=[]
leibie_list=[]
s2_list=[]
pingfen_list=[]
didian_list=[]
actors_list=[]
cover_url_list = []
types_list = ["无","纪录片","传记","犯罪","历史","动作","情色","歌舞","儿童","无","悬疑","剧情","灾难","爱情","音乐","冒险","奇幻","科幻","运动","惊悚","恐怖","无","战争","短片","喜剧","动画","同性","西部","家庭","武侠","古装","黑色电影",""]
sum=0
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
def douban(urls,i):
    response=requests.get(urls,headers=headers,proxies={'http':'http://47.100.207.26:8080'})#获取网页
    soup=BeautifulSoup(response.text,'lxml')
    s=soup.get_text()
    s2=json.loads(s)
    print(s2)
    s2_list.append(len(s2))
    for j in range(len(s2)):
        s3=s2[j]
        title=s3.get('title')
        title_list.append(title)
        rank=int(s3.get('rank'))
        rank_list.append(rank)
        lianjie=s3.get('url')
        lianjie_list.append(lianjie)
        cover_url = s3.get('cover_url')
        cover_url_list.append(cover_url)
        # leibie=s3.get('types')
        leibie=types_list[i]
        leibie_list.append(leibie)
        pingfen=float(s3.get('rating')[0])
        pingfen_list.append(pingfen)
        didian=s3.get('regions')[0]
        didian_list.append(didian)
        actors=s3.get('actors')
        actors=''.join(actors)
        actors_list.append(actors)
for i in range(32):
    # if i==31:
    #     urls='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=100'
    # else:
    #     # urls ='https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=140&limit=20'.format(i)
    #     urls ='https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=0&limit=100'.format(i)
    urls = 'https://movie.douban.com/j/chart/top_list?type={}&interval_id=100%3A90&action=&start=0&limit=100'.format(i)
    douban(urls,i)
dict={'题目':title_list,'分类排名':rank_list,'链接':lianjie_list,'电影类别':leibie_list,'评分':pingfen_list,'国家':didian_list,'海报链接':cover_url_list,'演员':actors_list}
dt=pd.DataFrame(dict)
print(dt)
dt.to_csv(r'E:\cpp\Python\123.csv',mode='a')
for k in range(len(s2_list)):
    sum+=s2_list[k]
print('总条数：',sum)
with open("E:/abchomewrk/dict/Movie1.json",'w',encoding='utf-8')as json_file:
    json_file.write(json.dumps(dict,ensure_ascii=False,indent=4))