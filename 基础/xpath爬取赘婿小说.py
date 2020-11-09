from lxml import etree
import requests
import time
url = "http://www.xbiquge.la/19/885"
sy_url = "http://www.xbiquge.la"
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
respone = requests.get(url=url,headers=ua)
page_text = bytes(respone.text,respone.encoding).decode('utf-8','ignore')
tree = etree.HTML(page_text)
title_list = tree.xpath('//div[@id="list"]/dl/dd')
fp = open('./zx.txt','w',encoding='utf-8')
for t in title_list:
    title = t.xpath('./a/text()')[0]
    txt_url = t.xpath('./a/@href')[0]
    txt_url = sy_url+txt_url
    #print(title,txt_url)
    respone2 = requests.get(url=txt_url,headers=ua)
    page_text2 = bytes(respone2.text,respone2.encoding).decode('utf-8','ignore')
    tree2 = etree.HTML(page_text2)
    txt = tree2.xpath('//div[@id="content"]/text()')
    txt = str(txt)
    print(txt)
    txt = txt.replace(r'\xa0',' ').replace(r'\r','').replace(r'，','').replace(r'[','').replace(r']','').replace(r"', '",'')
    print('正在爬取'+title)
    fp.write(title+'\n'+txt+'\n')
    time.sleep(1)
