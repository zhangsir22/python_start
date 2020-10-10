import requests
url = "http://192.168.102.253/stat.htm"
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70"}
respone = requests.get(url=url,headers=ua)
print(respone.text)