import requests
from lxml import etree
url ='http://www.xbiquge.la/0/885/742710.html'
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}


txt = requests.get(url=url,headers=ua).text

tree = etree.HTML(txt)
text = tree.xpath('//div[@id="content"]')
print(text[0].xpath('string(.)').encode('gbk'))

