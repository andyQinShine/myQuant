#coding=utf-8
import multiprocessing
from multiprocessing import Pool
import time


def do(n):
    name = multiprocessing.current_process().name
    print(name,'starting')
    print("worker ", n)
    return

def run(fn):
    time.sleep(1)
    print(fn * fn)

if __name__ == '__main__' :
    # numlist = []
    # for i in range(5):
    #     p = multiprocessing.Process(target=do, args=(i,))
    #     numlist.append(p)
    #     p.start()
    #     p.join()
    #     print("Process end")

    testFL = [1,2,3,4,5,6]
    print("order is:")
    s = time.time()
    for fn in testFL:
        run(fn)
    t1 = time.time()
    print("exec time:", int(t1 - s))

    print('multipe threading')
    pool = Pool(10)
    pool.map(run,testFL)
    # pool.colse()
    # pool.join()
    t2 = time.time();
    print("并行执行时间:", int(t2 - t1))