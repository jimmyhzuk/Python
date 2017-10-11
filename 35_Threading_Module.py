import threading
from queue import Queue
import time

printlock = threading.Lock() # perform a thread lock

def threader():
    while True:
        worker = q.get() # .get() fetches a item from the queue
        time.sleep(0.5) 
        with printlock:
            print(threading.current_thread().name, worker)
        q.task_done() # indication that task was complete

q = Queue() # create a queue 

for x in range(10):
    t = threading.Thread(target=threader) # defining the thread and its target
    t.daemon = True # 
    t.start() # start the thread

start = time.time() # noting the start time

for worker in range(20):
    q.put(worker) # adding items to the queue

q.join() # blocks untill all items of the queue are returned and processed

print('entire job took:', time.time()-start)