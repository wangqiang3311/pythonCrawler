from urllib.request import urlretrieve
import requests
from bs4 import BeautifulSoup

def Schedule(blocknum,blocksize,totalsize):
    per=100.0*blocknum*blocksize/totalsize
    if per>100:
        per=100
    print("当前下载进度：%d" %per)

user_agent='Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
r=requests.get('https://www.ivsky.com/tupian/ziranfengguang/',headers= headers)
#使用beautifulsoup解析
soup=BeautifulSoup(r.text,'html.parser')
imgs=soup.find_all("img")

i=0
for img in imgs:
    url=img['src']
    urlretrieve('https:'+url,'img'+str(i)+'.jpg',Schedule)
    i+=1