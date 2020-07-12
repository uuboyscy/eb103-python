import time

unix_sec = time.time()
local_time = time.localtime()
gm_time = time.gmtime()

print(unix_sec)
print(local_time)
print(gm_time)

readable_time = time.strftime('現在時間 %Y-%m-%d %H:%M:%S', local_time)
print(readable_time)