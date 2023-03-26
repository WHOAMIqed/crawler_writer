import json
import requests
from lxml import etree

def get_aff(url, headers, id):
    data = {"limit": 30,
            "timeout": 3000,
            "filterTags": [id, 0, 0, 0, 0, 0, 0],
            "tagId": 60826,
            "fromLemma": 'true',
            "contentLength": 38,
            "page": 0}

    response = requests.post(url, headers=headers, data=data)
    # 返回的是json编码的二进制流，我们先用json类将其解码
    jdata = json.loads(response.content)
    # 将字典里面的机构名和url读取出来
    urls = [[i['lemmaTitle'], i['lemmaUrl']] for i in jdata['lemmaList']]
    print(urls)
    return urls

# 获取不同地区对应的id
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35',
           'Referer': 'https://baike.baidu.com/wikitag/taglist?tagId=\
           60826&fromLemma=true'}
data = {'tagId': 60826, 'fromLemma': 'true'}
response = requests.get('https://baike.baidu.com/wikitag/api/getlemmas', headers=headers, params=data)
response.encoding = 'utf-8'
tree = etree.HTML(response.text)
ids = tree.xpath('//div[@class="params_cont"]')[0].xpath('./span/@data-value')
# 遍历这些选项，取得每一个选项框内的机构url
urls = []
for id in ids:
    urls.extend(get_aff('https://baike.baidu.com/wikitag/api/getlemmas', headers, id))



    with open('result.txt', 'a') as f:
        f.write(json.dumps(urls) + '\n')
        f.close()