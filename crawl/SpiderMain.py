from  DataOutput import DataOutput
import sys
sys.path.append("../")
from  pythonCrawler.HtmlDownLoader  import HtmlDownLoader
from  pythonCrawler.HtmlParser  import HtmlParser
from  UrlManager import UrlManager

class SpiderMain(object):
    def __init__(self):
        self.manager=UrlManager()
        self.downloader=HtmlDownLoader()
        self.parser=HtmlParser()
        self.output=DataOutput()

    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url=self.manager.get_new_url()
                html=self.downloader.download(new_url)
                new_urls,data=self.parser.parser(new_url,html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except Exception as err:
                print("crawl faild:"+str(err))
        self.output.output_html('result.html')

if __name__=="__main__":
    spider_man=SpiderMain()
    spider_man.crawl('https://baike.baidu.com/view/284853.htm')

    