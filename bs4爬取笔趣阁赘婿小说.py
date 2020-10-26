
import requests
from bs4 import BeautifulSoup

ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
url ="http://www.xbiquge.la/0/885/"
sy_url = "http://www.xbiquge.la"
page_text = requests.get(url=url,headers=ua)
respone = bytes(page_text.text,page_text.encoding).decode('utf-8','ignore')
soup = BeautifulSoup(respone,'lxml')
title_list = soup.select('.box_con > div > dl > dd  ')
# print(type(title_list))
# print(title_list.dd.a['href'])
#fp = open('./xx.txt','w',encoding='utf-8')
for i in title_list:
    title = i.string
    text_url = i.a['href']
    text_url = sy_url+text_url
    print(text_url)
    respone2 = requests.get(url=text_url,headers=ua)
    txt = bytes(respone2.text,respone2.encoding).decode('utf-8','ignore')
    soup2 = BeautifulSoup(txt,'lxml')
    #print(soup2)
    text = soup2.select('.box_con > div')
    print(text)
    #fp.write(title + '\n' + text +'\n')


