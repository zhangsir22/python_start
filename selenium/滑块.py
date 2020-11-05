from selenium import webdriver
from selenium.webdriver import ActionChains
import time
bro = webdriver.Edge(executable_path='./msedgedriver.exe')
bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
bro.switch_to.frame('iframeResult')
btn = bro.find_element_by_id('draggable')
action = ActionChains(bro)
action.click_and_hold(btn)
for i in range(6):
    action.move_by_offset(15,0).perform()
    time.sleep(1)
action.release()
bro.quit()