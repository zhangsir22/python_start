import requests
from lxml import etree
url = "http://sc.chinaz.com/jianli/free.html"
ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}

respone = requests.get(url=url,headers=ua)
jianli_page = bytes(respone.text,respone.encoding).decode('utf-8','ignore')

tree = etree.HTML(jianli_page)
jianli_list = tree.xpath('//div[@id="main"]/div/div')
for jianli in jianli_list:
    jl_url = jianli.xpath('./a/@href')[0]
    jl_name = jianli.xpath('./a/img/@alt')[0]
    respone2 = requests.get(url=jl_url,headers=ua)
    jianli2_page = bytes(respone2.text,respone2.encoding).decode('utf-8','ignore')
    tree2 = etree.HTML(jianli2_page)
    dow_line = tree2.xpath('//div[@class="down_wrap"]/div/ul')
    for i in dow_line:
        dow_line2 = i.xpath('./li/a/@href')[0]
        print(dow_line2)
        jianli_name = i.xpath('//div[@class="ppt_tit clearfix"]/h1/text()')[0]
        jianli3 = requests.get(url=dow_line2,headers=ua).content
        with open('./'+jianli_name+'.rar' ,'wb') as fp :
            fp.write(jianli3)
            print(jianli_name+"下载完成！")
            ###






