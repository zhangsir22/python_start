from selenium import webdriver
import time
from lxml import etree
bro = webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('http://www.xbiquge.la/19/885/')
btn = bro.find_element_by_link_text().help()
btn.click()
page_text = bro.page_source
# page_sour = etree.HTML(page_text)
# tatil_list = page_sour.xpath('//div[@id="list"]/dl/dd')
# for title in tatil_list:
#     print(title.xpath('./a/text()'))
time.sleep(2)
bro.quit()