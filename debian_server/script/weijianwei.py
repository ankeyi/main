#!/bin/python3
import requests
from bs4 import BeautifulSoup
from urllib import parse
import os

#先获取导航页的URL及标题
url="http://wjw.shanxi.gov.cn/xwzx/wjyw/"
r=requests.get(url)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'lxml')
_,path1,_,path2,*_=soup.select('.demo-right li a')
new_url1=parse.urljoin(url,path1['href'])

#获取新网页
r=requests.get(new_url1)
r.encoding=r.apparent_encoding
soup=BeautifulSoup(r.text,'lxml')
for line in soup.select('.view'):
        print(line.get_text())
        line_text=line.get_text()
        os.system(f"echo '{line_text}' | mail -s '山西疫情报告' 121@gmail.com")
