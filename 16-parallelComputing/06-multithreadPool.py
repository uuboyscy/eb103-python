import time
import os
import threading
from multiprocessing.dummy import Pool

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))

if __name__ == '__main__':
    # 開始時間
    start_time = time.time()

    print('母程序PID : ', os.getpid())

    p = Pool(4)

    for i in range(0, 12):
        p.apply_async(longTime, args=(i, ))

    p.close()
    p.join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))