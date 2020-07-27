from threading import Thread
from threading import Lock
import time


def thread_a(lockA,lockB):
    lockA.acquire()
    print('Thread a -- Lock A')
    time.sleep(2)
    lockB.acquire()
    print('Thread a -- Lock b')


def thread_b(lockA,lockB):
    lockB.acquire()
    print('Thread b -- Lock B')
    time.sleep(2)
    lockA.acquire()
    print('Thread b -- Lock A')


if __name__ == "__main__":
    a = Lock()
    b = Lock()

    Thread(target = thread_a, args = (a,b)).start()
    Thread(target = thread_b, args = (a,b)).start()