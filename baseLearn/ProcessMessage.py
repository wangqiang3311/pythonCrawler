from multiprocessing import Process,Queue
import os,time,random

#写数据进程执行的代码
def pro_write(q,urls):
    print('process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        print('put %s to queue...' %url)
        time.sleep(random.random())

#读数据进程执行的代码
def pro_read(q):
    print('process(%s) is reading...' %os.getpid())
    while True:
        url=q.get(True)
        print('get %s from queue.' %url)


if __name__ == "__main__":

    q=Queue()
    #父进程创建Queue，并传给各个子进程
    proc_writer1=Process(target=pro_write,args=(q,['url_1','url_2','url_3'],))
    proc_writer2=Process(target=pro_write,args=(q,['url_4','url_5','url_6'],))
    proc_reader=Process(target=pro_read,args=(q,))
    #启动子进程
    proc_writer1.start()
    proc_writer2.start()
    proc_reader.start()
    proc_writer1.join()
    proc_writer2.join()
    proc_reader.terminate()