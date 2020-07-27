from threading import Thread
from threading import Condition
from threading import Lock
from threading import current_thread
from collections import deque
import time
import random

class Solution:
    def __init__(self, n):
        self.cond = Condition()
        self.list_item = deque()
        self.curr = 0
        self.int_max = n
        self.lock = Lock()


    def dequeue(self):
        self.cond.acquire()
        while self.curr == 0:
            self.cond.wait()

        item = self.list_item.pop()
        self.curr -= 1
        self.cond.notify_all()
        self.cond.release()

        return item

    def enqueue(self,n):
        self.cond.acquire()

        while self.int_max == self.curr:
            self.cond.wait()

        self.list_item.append(n)
        self.curr +=1
        self.cond.notify_all()
        self.cond.release()


    def consumer_thread(self):
        while 1:
            item = self.dequeue()
            print('{}  consumer thread  - consumed {}'.format(current_thread().getName(),item))
            time.sleep(random.randint(1,3))

    def producer_thread(self,q):
        while 1:
            #item = random.randint(1,100)
            item = q
            self.enqueue(item)
            print('{}  producer thread - is producing {} '.format(current_thread().getName(),item))
            time.sleep(random.randint(1,3))


    def main(self):
        producer1 = Thread(target = self.producer_thread, name = "Producer1", args=(1,), daemon=True)
        producer2 = Thread(target = self.producer_thread,name = "Producer2", args= (100,),  daemon=True)
        consumer1 = Thread(target = self.consumer_thread, name = "Consumer1", daemon=True)
        consumer2 = Thread(target = self.consumer_thread, name = "Consumer2", daemon = True)

        consumer1.start ()
        consumer2.start ()
        producer1.start()
        producer2.start()

        time.sleep(15)



obj = Solution(5)
obj.main()