import requests
from lxml import etree
import os
import time
from multiprocessing.dummy import Pool
url = "http://pic.netbian.com/"
sy_url = "http://pic.netbian.com/4kmeinv/"
ua =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
if not os.path.exists('./meinv'):
    os.mkdir('./meinv')
def tp(sy_url):
    sy_page = requests.get(url=sy_url,headers=ua).text
    tree = etree.HTML(sy_page)
    tp_list = tree.xpath('//div[@class="wrap clearfix"]/div/div/ul/li')
    for i in tp_list:
        tp_url = i.xpath('./a/@href')[0]
        ztp_url = url + tp_url
        respone = requests.get(url=ztp_url,headers=ua)
        tp_page = bytes(respone.text,respone.encoding).decode('gbk','ignore')
        tp_tree  = etree.HTML(tp_page)
        ztp_img = tp_tree.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
        ztp_img_url = url + ztp_img
        ztp_name = tp_tree.xpath('//div[@class="photo-pic"]/a/img/@alt')[0] + '.jpg'
        zp = requests.get(url=ztp_img_url,headers=ua).content

        with open('./meinv/' + ztp_name,'wb') as fp:
            fp.write(zp)
        print(ztp_name + "爬取成功" )
def ran():
    url_list = []
    url = "http://pic.netbian.com/4kmeinv/"
    url_page = requests.get(url=url,headers=ua).text
    r_tree = etree.HTML(url_page)
    page = r_tree.xpath('//div[@class="page"]/a')[-2]
    page_int = int(page.xpath('./text()')[0])
    for i in range(1,page_int):
        if i == 1:
            y = "index.html"
        else:
            y = "index_" + str(i) + ".html"
        ys_url =url + y
        url_list.append(ys_url)
    return url_list
l = ran()
start_time = time.time()
pool = Pool(20)
pool.map(tp,l)
end_time =time.time()
print("耗时%d:",tart_time-end_time)
pool.close
pool.join
