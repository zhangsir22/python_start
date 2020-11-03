from selenium import webdriver
from lxml import etree
import time
bro = webdriver.Edge('msedgedriver.exe')
bro.get('https://www.taobao.com')
search_input = bro.find_element_by_id('q')
search_input.send_keys('iphone')
btn = bro.find_element_by_class_name('btn-search')
btn.click()
u = bro.find_element_by_id('fm-login-id')
u.send_keys('1139287223@qq.com')
p = bro.find_element_by_id('fm-login-password')
p.send_keys('zz7251611')
btn_login = bro.find_element_by_class_name('fm-button')
btn_login.click()
time.sleep(1)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)
bro.quit()