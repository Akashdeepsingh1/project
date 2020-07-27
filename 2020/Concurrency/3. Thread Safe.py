from threading import Thread
from threading import Lock
import sys

class Counter:

    def __init__(self):
        self.count = 0
        self.lock = Lock()

    def increment(self):
        for _ in range(100000):
            self.lock.acquire()
            self.count+=1
            self.lock.release()



if __name__ == "__main__":
    sys.setswitchinterval(0.005)

    numThreads = 5

    threads = [0] * numThreads
    counter = Counter()

    for i in range(numThreads):
        threads[i] = Thread(target=counter.increment)

    for i in range(numThreads):
        threads[i].start()

    for i in range(numThreads):
        threads[i].join()

    if counter.count != 500000:
        print("You shouldn't get this line")

    else:
        print('count = {}'.format(counter.count))
