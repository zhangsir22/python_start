from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.shicimingju.com/book/sanguoyanyi.html"
url2 = "https://www.shicimingju.com/"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}
page_text = requests.get(url=url,headers=ua).text
soup = BeautifulSoup(page_text,'lxml')
li_list = soup.select('.book-mulu > ul > li')
fp = open('./sanguo.txt','w',encoding='utf-8')
for li in li_list:
    title = li.a.string
    detail_url = url2+li.a['href']
    print(detail_url)
    detail_page_text = requests.get(url=detail_url,headers=ua).text
    detail_soup= BeautifulSoup(detail_page_text,'lxml')
    div_tag = detail_soup.find('div',class_="chapter_content")
    content = div_tag.text
    print(div_tag)
    fp.write(title+':'+content+'\n')
    print(title,'爬取成功')