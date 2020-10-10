import requests
import re

url = "http://192.168.102.253/prcnt.htm"
respone = requests.get(url=url)
p = respone.text
print(p)
