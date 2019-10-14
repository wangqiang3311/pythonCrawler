# coding:utf-8
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number=10
#定义收发队列
task_queue=queue.Queue(task_number)
result_queue=queue.Queue(task_number)
def get_task():
    return task_queue
def get_result():
    return result_queue

class QueueManager(BaseManager):
    pass

def win_run():
    QueueManager.register('get_task_queue',callable=get_task)
    QueueManager.register('get_result_queue',callable=get_result)
    manager= QueueManager(address=('127.0.0.1',8001),authkey='qive'.encode('utf-8'))
    manager.start()
    try:
        task=manager.get_task_queue()
        result=manager.get_result_queue()
        #添加任务
        for url in ["ImageUrl_"+str(i) for i in range(10)]:
            print('put task %s...' %url)
            task.put(url)
        print('try get result')
        for i in range(10):
            print('result is %s' %result.get(timeout=1000000))
    except:
        print('manager error')
    finally:
        manager.shutdown()

if __name__ == "__main__":

    freeze_support()
    win_run()