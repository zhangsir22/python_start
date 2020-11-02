import time
# import requests
# from lxml import etree
# url = "http://sc.chinaz.com/jianli/free.html"
# ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
#
# respone = requests.get(url=url, headers=ua).text
# tree = etree.HTML(respone)
# jianli_page = tree.xpath('//div[@id="main"]/div')
# print(jianli_page)
# for i in jianli_page:
#     jianli_url = i.xpath('./div/a/@href')
#     print(jianli_url)
#     jianli_name = i.xpath('./div/a/img/@alt')
#     print(jianli_name)
time1= time.time()
time.sleep(1)
time2=time.time()
print("耗时%d",time2-time1)