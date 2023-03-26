# 方法一
import requests
from lxml import etree

def url_complete(host, url):
    if 'http' not in url:
        return host+url
    return url

url = 'https://cs.pku.edu.cn/szdw1/jyxl{}.htm'
urls = []

for i in range(1, 14):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64\
               ) AppleWebKit/537.36 (KHTML, like Gecko)\
               Chrome/93.0.4577.63 Safari/537.36'}
    response = requests.get(url.format('/'+str(i)), headers=headers)
    response.encoding = 'utf-8'

    tree = etree.HTML(response.text)
    temp = tree.xpath('//li/div[@class="txt"]/h4/a/@href')
    urls.extend([url_complete("https://cs.pku.edu.cn", html.split('..')[-1]) for html in temp])
else:
    response = requests.get(url.format(''), headers=headers)
    response.encoding = 'utf-8'

    tree = etree.HTML(response.text)
    temp = tree.xpath('//li/div[@class="txt"]/h4/a/@href')
    urls.extend([url_complete("https://cs.pku.edu.cn", html.split('..')[-1]) for html in temp])


###########################################################################################################

# 方法二
import requests
from lxml import etree

def url_complete(host, url):
    if 'http' not in url:
        return host+url
    return url

url = 'https://cs.pku.edu.cn/szdw1/jyxl{}.htm'
urls = []


def request(start_url, urls, headers):
    response = requests.get(start_url, headers=headers)
    response.encoding = 'utf-8'
    tree = etree.HTML(response.text)
    response_urls = tree.xpath('//li/div[@class="txt"]/h4/a/@href')
    urls.extend([url_complete("https://cs.pku.edu.cn", html.split('..')[-1]) for html in response_urls])
    next_page = tree.xpath('//span[@class="p_next p_fun"]/a/@href')
    if next_page:
        if 'jyxl/' in next_page[0]:
            next_page = url_complete("https://cs.pku.edu.cn/szdw1/", next_page[0])
        else:
            next_page = url_complete("https://cs.pku.edu.cn/szdw1/jyxl/", next_page[0])
        request(next_page, urls, headers)
    else:
        return 0
    
start_url = "https://cs.pku.edu.cn/szdw1/jyxl.htm"
url_list = []
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64\
           ) AppleWebKit/537.36 (KHTML, like Gecko)\
           Chrome/93.0.4577.63 Safari/537.36'}
request(start_url, url_list, headers)