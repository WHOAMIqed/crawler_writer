import json
import requests
from lxml import etree

def get_aff(url, headers, n):
    data = {"limit": 24,
            "timeout": 3000,
            "filterTags": [],
            "tagId": 76572,
            "fromLemma": 'false',
            "contentLength": 40,
            "page": n}

    response = requests.post(url, headers=headers, data=data)
    # 返回的是json编码的二进制流，我们先用json类将其解码
    jdata = json.loads(response.content)
    # 将字典里面的机构名和url读取出来
    urlsson = [[i['lemmaTitle'], i['lemmaUrl']] for i in jdata['lemmaList']]
    urls.extend(urlsson)
    # print(urls)
    return urls

# 获取不同地区对应的id
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
           'Referer': 'https://baike.baidu.com/wikitag/taglist?tagId=\
           76572&fromLemma=true'}
data = {'tagId': 76572, 'fromLemma': 'true'}
response = requests.get('https://baike.baidu.com/wikitag/taglist?tagId=76572', headers=headers, params=data)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
ids = tree.xpath('//*[@id="waterFall"]/div[1]/a/div/div[2]/div[1]')
print(ids)
# 遍历这些选项，取得每一个选项框内的机构url

urls1 = []
dict1 = {}
# for n in range(211):
# for i in range(0,5):
# urls.extend(get_aff('https://baike.baidu.com/wikitag/api/getlemmas', headers, 211))
for j in range(10):
    urls = []
    urls = get_aff('https://baike.baidu.com/wikitag/api/getlemmas', headers, j)
    list(urls)
    print(urls)
    lent = len(urls)
    print(lent)

    for i in range(lent):
        response5 = requests.get(urls[i][1], headers=headers)
        response5.encoding = 'utf-8'

        data5 = requests.get(urls[i][1], headers=headers)
        tree = etree.HTML(response5.text)
        ids = tree.xpath('//dd [@class="lemmaWgt-lemmaTitle-title J-lemma-title"]/span/h1/text()')
        engori = tree.xpath('//dt[text()="外文名"]/following-sibling::*[1]/text()')
        eng = []
        eng.extend(html.split() for html in engori)
        if eng != []:
            eng0 = eng[0]
            eng1 = " ".join(str(i) for i in eng0)
        else:
            eng1 = 'empty'
        dict1[ids[0]] = eng1
        print(ids)
        print(eng1)
    urls1.extend(html.split() for html in ids)
    urls =[]
print(urls1)
print(dict1)
with open("E:/abchomewrk/dict/jsonDataFile.josn",'w',encoding='utf-8')as json_file:
    json_file.write(json.dumps(dict1,ensure_ascii=False,indent=4))
# print(ids)

#
# with open('result1.txt', 'a') as f:
#     f.write(json.dumps(urls1) + '\n')
#     f.close()


    #//*[@id="waterFall"]/div[6]/a/div/div[2]/div[1]
    #//*[@id="waterFall"]/div[12]/a/div/div[2]/div[1]
    #//*[@id="waterFall"]/div[16]/a/div/div[2]/div[1]

    # for i in range(1,24):
    #     urls.extend(get_aff('https://baike.baidu.com/wikitag/taglist?tagId=76572', headers, n))