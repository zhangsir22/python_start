from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_option = Options()
chrome_option.add_argument('--headless')
chrome_option.add_argument('--disable-gpu')

option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_option,options=option)
bro.get('https://www.baidu.com')
t = bro.page_source
print(t)