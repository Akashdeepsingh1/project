import threading
import time


'''
class Solution:
    def addstartandend(self,start,end ):
        count = 0
        for i in range(start,end):
            count+=i
        print(count)
        time.sleep(2)

start_time = time.perf_counter()

obj1 = Solution()
th1 = threading.Thread(target=obj1.addstartandend, args=[0,500000])

obj2 = Solution()
th2 = threading.Thread(target=obj2.addstartandend, args=[500000,1000000])


th1.start()
th2.start()
th1.join()
time.sleep(1)
th2.join()

finish_time = time.perf_counter()
print(finish_time-start_time)
'''

def do_something(num):
    print(f'Thread is Sleeping for {num}')
    time.sleep(num)
    print('Done Sleeping')

st_time = time.perf_counter()
thread = []
for _ in range(10):
    th = threading.Thread(target=do_something, args = [_])
    thread.append(_)
    th.start()

fnsh_time = time.perf_counter()

print(fnsh_time- st_time)
