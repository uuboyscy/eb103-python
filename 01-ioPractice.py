print('123','456','789',sep='|')
print('123','456','789',sep='|', end='')
print('123','456','789',sep='|')

print('abcde', file=open('./test.txt', 'w'))

import time
f = open('./test.txt', 'a')
for i in range(0, 5):
    print('abcde', file=f, flush=True)
    time.sleep(5)
f.close()

