import requests
from requests.exceptions import RequestException
import re
import json

def get_one_page(url,headers):
   try:
        response = requests.get(url,headers = headers)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        return None
   except RequestException:
       return None

def parse_one_page(html):
# //提取网页信息的正则表达式
    pattern = re.compile('<dd>.*?board-index.*?>(\d*)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)(/p)'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5]+item[6]
        }
# //写入result.txt文件中
def write_to_file(content):
    with open('result.txt', 'a') as f:
        f.write(json.dumps(content) + '\n')
        f.close()


def main():
# //猫眼电影爬取需添加headers，从用户角度访问
    url = 'https://maoyan.com/board/4?offset=0'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    html = get_one_page(url, headers)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()

