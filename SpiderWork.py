import time 
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from HtmlDownLoader  import HtmlDownLoader
from  HtmlParser  import HtmlParser

class QueueManager(BaseManager):
    pass
class SpiderWork(object):
    def __init__(self):
        QueueManager.register('get_task_queue')
        QueueManager.register('get_result_queue')

        server_addr='127.0.0.1'
        print('Connect to server %s...' % server_addr)
        self.m=QueueManager(address=(server_addr,8001),authkey='baike'.encode('utf-8'))
        #从网络连接
        self.m.connect()
        self.task=self.m.get_task_queue()

        print("task queue size: %s" %self.task.qsize())
        self.result=self.m.get_result_queue()
        self.downloader=HtmlDownLoader()
        self.parser=HtmlParser()
        print('init finish')


    def crawl(self):
        while(True):
            try:
                if not self.task.empty():
                    url=self.task.get()

                    if url=='end':
                        print('控制节点通知爬虫节点停止工作')
                        self.result.put({'new_urls':'end','data':'end'})
                        return
                    print('爬虫节点正在解析：%s' %url.encode('utf-8'))
                    content=self.downloader.download(url)
                    new_urls,data=self.parser.parser(url,content)
                    self.result.put({"new_urls":new_urls,"data":data})

            except EOFError:
                print('连接工作节点失败')
                return
            except Exception:
                print('crawl fail')

if __name__ == "__main__":
    spider=SpiderWork()
    spider.crawl()
