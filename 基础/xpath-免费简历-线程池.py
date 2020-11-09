import requests
from multiprocessing.dummy import Pool
from lxml import etree
import os
import time

url = "http://sc.chinaz.com/jianli/free.html"
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}

def get_url(jl_url):
    respone = requests.get(url=jl_url,headers=ua)
    respone_text = bytes(respone.text,respone.encoding).decode('utf-8','ignore')
    #获取免费建立首页数据
    tree = etree.HTML(respone_text)
    jianli_page = tree.xpath('//div[@id="main"]/div/div')
    url_list = []
    for i in jianli_page:
        jianli_url = i.xpath('./a/@href')[0]
        jianli_name = i.xpath('./a/img/@alt')[0]
        respone_dow = requests.get(url=jianli_url,headers=ua).text
        dow_tree  = etree.HTML(respone_dow)
        dow_url = dow_tree.xpath('//div[@class="clearfix mt20 downlist"]/ul/li[1]/a/@href')[0]
        dic = {'name':jianli_name,'url':dow_url}
        url_list.append(dic)
    return url_list
def get_jianli(dic):
    name = dic['name']
    d_url = dic['url']
    print(name+"正在下载 \n")
    jianli =  requests.get(url=d_url,headers=ua,timeout=120,proxies={"https":"49.86.179.146:9999"}).content

    with open('./jianli/'+name + '.rar' ,'wb') as fp:
        fp.write(jianli)
        print("下载完成"+name)
    # print(name)
    # print(d_url)
r = get_url(url)

pool = Pool(4)
start_time = float(time.time())
pool.map(get_jianli,r)
end_start = float(time.time())
print(end_start-start_time)
pool.close
pool.join
