import threading
import random
import time


class SemaphoreThread(threading.Thread):
    """Class using semaphores"""
    # class variable
    availableTables = ["A", "B", "C", "D", "E"]

    def __init__(self, threadName, semaphore):
        """Initialize thread using a semaphore variable and creates an attribute"""
        threading.Thread.__init__(self, name=threadName)
        self.sleepTime = random.randrange(1, 6)

        # set the semaphore as a data attribute of the class
        # all threads will shared the same semaphore
        self.threadSemaphore = semaphore

    def run(self):
        """Print message and release semaphore"""

        # acquire the semaphore
        self.threadSemaphore.acquire()
        threadLock.acquire()
        # remove a table from the list
        table = SemaphoreThread.availableTables.pop()
        print "%s entered; seated at table %s." % (self.getName(), table),
        print SemaphoreThread.availableTables
        threadLock.release()
        time.sleep(self.sleepTime)  # enjoy a meal

        # free a table
        threadLock.acquire()
        print "   %s exiting; freeing table %s." % (self.getName(), table)
        SemaphoreThread.availableTables.append(table)
        print SemaphoreThread.availableTables
        threadLock.release()
        # release the semaphore after execution finishes
        self.threadSemaphore.release()


threadLock = threading.Lock()
threads = []  # list of threads

# semaphore allows five threads to enter critical section
# treading.Semaphore is the semaphore method, returning a threadSemaphore variable
threadSemaphore = threading.Semaphore(len(SemaphoreThread.availableTables))

# create ten threads
for i in range(1, 11):
    threads.append(SemaphoreThread("thread" + str(i), threadSemaphore))

# start each thread
for thread in threads:
    thread.start()
