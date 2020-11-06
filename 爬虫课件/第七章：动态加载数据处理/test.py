# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('headless')
# chrome_options.add_argument('--disable-gpu')
#
# option = webdriver.ChromeOptions()
# option.add_experimental_option('excludeSwitches',['enable-automation'])
#
# bro = webdriver.Chrome(executable_path='./chromedriver',chrome_options=chrome_options,options=option)
#
# bro.get('https://www.baidu.com')
# sleep(2)
# bro.quit()
from selenium import webdriver
bro = webdriver.Chrome()