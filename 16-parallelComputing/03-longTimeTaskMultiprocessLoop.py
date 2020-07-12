import time
import os
import multiprocessing as mp

def longTime(i):
    print('PID: {}, Task: {} .'.format(os.getpid(), i))
    time.sleep(2)
    result = 10 ** 30
    print('Result: {}'.format(result))

if __name__ == '__main__':
    # 開始時間
    start_time = time.time()

    print('母程序PID : ', os.getpid())

    mpList = []
    for i in range(1, 5):
        mpList.append(mp.Process(target=longTime, args=(i, )))

    for i in range(0, 4):
        mpList[i].start()

    for i in range(0, 4):
        mpList[i].join()

    end_time = time.time()
    print('總共花費 {} 秒'.format(end_time - start_time))