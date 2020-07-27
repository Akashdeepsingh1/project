from threading import Thread
from threading import current_thread
from threading import Lock
import time

sharedState = [1,2,3]
mylock = Lock()

def thread_write(temp):
    print('{} is trying to acquire the lock and write the data'.format(current_thread().getName()))
    mylock.acquire()
    time.sleep(3)
    print('{} has acquired the lock  and will write the data'.format(current_thread().getName()))
    sharedState[0] = temp
    print('{} is releasing of the lock and data is written'.format(current_thread().getName()))
    mylock.release()
    print('{} has released the lock'.format(current_thread().getName()))

def thread_read():
    print('{} is trying the acquire the lock to read the data'.format(current_thread().getName()))
    mylock.acquire()
    time.sleep(3)
    print('{} has acquired the log and will try to run the data '.format(current_thread().getName()))
    print(sharedState[0])
    print('{} data has been read and releasing the lock '.format(current_thread().getName()))
    mylock.release()


if __name__ == "__main__":
    temp = '777'
    thread1 = Thread(target = thread_write, args=(temp,), kwargs={}, daemon=False)
    thread2 = Thread(target = thread_read, daemon = True)
    # try with daemon = True
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

