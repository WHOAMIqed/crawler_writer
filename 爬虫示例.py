import requests
from lxml import etree

url = 'https://www.bilibili.com'
headers = {'Content-type': 'json', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
data = requests.get(url, headers=headers)
tree = etree.HTML(data.text)
print(tree.xpath('//a/text()'))