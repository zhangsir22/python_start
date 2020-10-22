from lxml import etree
import requests
url = "http://www.xbiquge.la/19/885"
sy_url = "http://www.xbiquge.la/"
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
zx_page = requests.get(url=url,headers=ua).text
tree = etree.HTML(zx_page)
list_title = tree.xpath('//div[@id="list"]/dl/dd')
fp = open('./zx.txt','w',encoding="utf-8")
for dd in list_title:
    title_name = dd.xpath("./a/text()")[0]
    url_text = dd.xpath("./a/@href")[0]
    text_url = sy_url + url_text
    print(text_url)

    text_page = requests.get(url=text_url,headers=ua).text
    text_tree = etree.HTML(text_page)
    list_text = text_tree.xpath('//div[@id="content"]/text()')[0]
    print(list_text.encode('iso-8859-1').decode('gbk'))
    # print(list_text)
    # for text in list_text:
    #     t = text.xpath('.//text()')[0]
    #     print(t)
    #     fp.write(title_name+"\n"+t)

