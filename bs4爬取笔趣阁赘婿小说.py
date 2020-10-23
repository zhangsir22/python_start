import lxml
import requests
from bs4 import BeautifulSoup

ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.48'}
url ="http://www.xbiquge.la/0/885/"
page_text = requests.get(url=url,headers=ua)
respone = bytes(page_text.text,page_text.encoding).decode('utf-8','ignore')
soup = BeautifulSoup(respone,'lxml')
print(soup.dl)

