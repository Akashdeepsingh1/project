from threading import Thread
from threading import current_thread


class subThread(Thread):
    def __init__(self):
        Thread.__init__(self,name='subclassThread',args = (2,3))

    def run(self):
        print('{} is the running thread'.format(current_thread().getName()))



obj1 = subThread()
obj1.start()
obj1.run()

obj2 = subThread()
obj2.run()

