import urllib.request

def download(url):
    try:
        html=urllib.request.urlopen(url).read().decode('utf-8')
    except  urllib.error.URLError as e:
        html=e.reason
    return html


url='http://baidu.com'
url='http://landing.zhaopin.com/register?utm_source=baidupcpz&utm_medium=cpt&utm_provider=partner&sid=121113803&site=null'
result=download(url)
print(result)