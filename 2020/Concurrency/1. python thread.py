
#Test--then--act

from threading import *
import random
import time

rand_int = 0

def updater():
    global rand_int
    while 1:
        rand_int = random.randint(1,9)

def printer():
    global rand_int
    while 1:
        if rand_int % 5 ==0:
            if rand_int % 5 != 0:
                print(rand_int)


if __name__ =="__main__":
    Thread(target=updater,daemon=True).start()
    Thread(target=printer,daemon=True).start()


