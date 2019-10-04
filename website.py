import builtwith
import whois

def findTechnology(url):
    message=builtwith.parse(url)
    print(message)

def findOwner(url):
    print(whois.whois(url))

def testFindTec():
    
    url='http://baidu.com'
    url='http://landing.zhaopin.com/register?utm_source=baidupcpz&utm_medium=cpt&utm_provider=partner&sid=121113803&site=null'
   

    findTechnology(url)

#testFindTec()
url='51job.com/'
findOwner(url)

