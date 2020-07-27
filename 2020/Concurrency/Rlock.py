from threading import RLock
from threading import Thread
sharedData = 22
mylock = RLock()

def thread_read():
    mylock.acquire()
    print(sharedData)
    mylock.release()

mylock.acquire()
mylock.acquire()

mylock.release()
mylock.release()

thread= Thread(target =thread_read)
thread.start()
thread.join()