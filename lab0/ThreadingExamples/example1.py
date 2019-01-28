#!/usr/bin/python

import threading
import random
import time


class PrintThread(threading.Thread):
    """Subclass of threading.Thread"""

    def __init__(self, threadName):
        """Initialize thread, set sleep time, print data"""

        threading.Thread.__init__(self, name=threadName)
        self.sleepTime = random.randrange(1, 6)
        print "Name: %s; sleep: %d" % (self.getName(), self.sleepTime)

    # overridden Thread run method
    def run(self):
        """Sleep for 1-5 seconds"""

        print "%s going to sleep for %s second(s)" % (self.getName(), self.sleepTime)
        time.sleep(self.sleepTime)
        print self.getName(), "done sleeping"


thread1 = PrintThread("thread1")
thread2 = PrintThread("thread2")
thread3 = PrintThread("thread3")

print "\nStarting threads"

thread1.start()  # invokes run method of thread1
thread2.start()  # invokes run method of thread2
thread3.start()  # invokes run method of thread3

print "Threads started\n"
