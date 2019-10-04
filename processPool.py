from multiprocessing import Pool
import os,time,random

def run_task(name):
    print('Task %s (pid=%s) is running ...' %(name,os.getpid()))
    time.sleep(random.random()*3)
    print('Task %s end.' % name)

if __name__ == "__main__":
    print('current proc  %s. ' % os.getpid())
    p=Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task,args=(i,))

    print('waiting all subprocesses done')
    p.close()
    p.join()
    print('all subprocesses done')
