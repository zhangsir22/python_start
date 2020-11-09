import requests
import re
import xlwt
import os
import time
#初始化数据

url = [{"商务发展中心":"http://192.168.101.203/prcnt.htm"},{"分析测试中心-2F":"http://192.168.102.253/prcnt.htm"},{"分析测试中心-4F":"http://192.168.104.251/prcnt.htm"},{"公共使用-6F":"http://192.168.106.251/prcnt.htm"},]
ua = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36 Edg/86.0.622.38"}
path = "./打印机统计表"
#获取总打印页数
def page(url):
    mun_list = []
    for url_new in url:
        for new_url in url_new.values():
            print_page = requests.get(url=new_url,headers=ua).text
            #print(print_page)
            ex = "var info=\['Total Printed Impressions',(.*?),.*?\];"
            print_num = re.findall(ex,print_page)
            mum = int(print_num[0])
            mun_list.append(mum)
    return mun_list
#写入数据表
def xls(path,num):  #存贮至xls表格
    # 获取当前时间
    t = time.strftime("%Y-%m-%d",time.localtime())
    if not os.path.exists(path):
        os.mkdir(path)

    #获取列名
    table_list = []
    for i in url:
        for k in i.keys():
            table_list.append(k)

    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("zhnag")
    for i in range(0,len(url)):
        worksheet.write(0,i,table_list[i])
        worksheet.write(1,i,num[i])



    workbook.save(path+"/da.xls")
    # workbook = xlwt.Workbook(encoding="utf-8")
    # workhseet = workbook.add_sheet("打印机统计")
    # workhseet.write(0,0,"2F")
    # workhseet.write(1,2,"zhang")
    # workbook.save(path+"/da.xls")

num = page(url)
xls(path,num)
