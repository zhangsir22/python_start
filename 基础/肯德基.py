import  requests
import json

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
param = {"cname": "" , "pid": "", "keyword": "长沙" , "pageIndex": "1" ,"pageSize": "10"}
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36 Edg/85.0.564.70"}
respone = requests.post(url=url,data=param,headers=ua)
t = respone.text
print(t)
with open("./kfc.json","w",encoding="utf-8") as fp :
    fp.write(t)
json.dump(t,fp=fp,ensure_ascii=False)
