import requests
from lxml import etree
url ='http://downsc.chinaz.net/Files/DownLoad/jianli/202010/jianli13852.rar'
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}


txt = requests.get(url=url,headers=ua).content
with open('./jianli.rar','wb') as fp :
    fp.write(txt)



