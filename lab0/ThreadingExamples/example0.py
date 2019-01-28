#!/usr/bin/python

import threading
import time

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        print_time(self.name, self.counter, 1)
        print "Exiting " + self.name


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
        # if exitFlag:
        #	 threadName.exit()


# Create new threads
thread1 = myThread(1, "Thread-1", 5)
thread2 = myThread(2, "Thread-2", 5)

# Start new Threads
thread1.start()
thread2.start()

# time.sleep(3)
# exitFlag = 1
print "Exiting Main Thread"
