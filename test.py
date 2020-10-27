import requests
from lxml import etree
#url ='http://downsc.chinaz.net/Files/DownLoad/jianli/202010/jianli13852.rar'
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}

url = "http://pic.netbian.com/4kmeinv/"
url_page = requests.get(url=url, headers=ua).text
r_tree = etree.HTML(url_page)
page = r_tree.xpath('//div[@class="page"]/a')
r = page[-2]
print(str(r.xpath('./text()')[0]))


