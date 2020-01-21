from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue
from crawl.UrlManager import UrlManager
from crawl.DataOutput import DataOutput
import time


def get_task():
    return url_q
def get_result():
    return result_q

class QueueManager(BaseManager): 
    pass

class NodeManager:

    def start_Manager(self,url_q,result_q):
        QueueManager.register('get_task_queue',callable=get_task)
        QueueManager.register('get_result_queue',callable=get_result)
        manager=QueueManager(address=('127.0.0.1',8001),authkey='baike'.encode('utf-8'))
        return manager


    def url_manager_proc(self,url_q,conn_q,root_url):
        url_manager=UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while(url_manager.has_new_url()):
                #从url管理器获取新的url
                new_url=url_manager.get_new_url()
                url_q.put(new_url)
                print('old_url=',url_manager.old_url_size())
                if(url_manager.old_url_size()>2000):
                    #通知爬行节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知！')
                    #关闭管理节点，同时存储set状态
                    url_manager.save_progress('new_urls.txt',url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt',url_manager.old_urls)
                    return
            
            #将从result_solve_proc获取到的URL添加到URL管理器
            try:
                if not conn_q.empty():
                    urls=conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException:
                time.sleep(0.1) #延时休息

    

    def result_solve_proc(self,result_q,conn_q,store_q):
        while True:
            try:
                if not result_q.empty():
                    content=result_q.get(True)
                    if content['new_urls']=='end':
                        print('结果分析进程接收通知然后结束！')
                        store_q.put('end')
                        return
                    
                    conn_q.put(content['new_urls']) #url为set类型
                    print('conn_q size:%s' %conn_q.qsize())
                    store_q.put(content['data']) #解析出来的数据为dict类型
                else:
                    time.sleep(0.1)
            except BaseException:
                time.sleep(0.1)

    def store_proc(self,store_q):
        output=DataOutput()
        while True:
            if not store_q.empty():
                data=store_q.get()
                if data=='end':
                    print('存储进程接收通知然后结束')
                    output.output_end(output.filepath)
                    return

                output.store_data(data) 
            else:
                time.sleep(0.1)


#定义收发队列
url_q=Queue()
result_q=Queue()

if __name__ == "__main__":
  
    freeze_support()
    store_q=Queue()
    conn_q=Queue()

    #创建分布式管理器
    node=NodeManager()
    manager=node.start_Manager(url_q,result_q)
    #创建URL管理进程、数据提取进程和数据存储进程
    url='https://baike.baidu.com/view/284853.htm'
    up=Process(target=node.url_manager_proc,args=(url_q,conn_q,url))
    rp=Process(target=node.result_solve_proc,args=(result_q,conn_q,store_q))
    sp=Process(target=node.store_proc,args=(store_q,))

    #启动三个进程和分布式管理器
    up.start()
    rp.start()
    sp.start()

    manager.get_server().serve_forever()


    

