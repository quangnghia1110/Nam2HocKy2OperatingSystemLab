import threading
import time
import random

NUM_READERS = 2
NUM_WRITERS = 2

mutex = threading.Semaphore(1)
rw_mutex = threading.Semaphore(1) 
read_count = 0

class writer(threading.Thread):
    def __init__(self, id):
        self.id = id
        super().__init__()
        
    def run(self):
        while True:
            rw_mutex.acquire() #khóa buffer chỉ cho luồng writer truy cập
            #------
            print(f"Writer {self.id} is writing...")
            time.sleep(random.randint(1, 3))
            print(f"Writer {self.id} write done!")
            #------
            rw_mutex.release()
            time.sleep(random.randint(1, 2))
class reader(threading.Thread):
    def __init__(self, id):
        self.id = id
        super().__init__()
        
    def run(self):
        global read_count
        while True:
            mutex.acquire()  #khóa buffer 
            read_count += 1
            if read_count == 1:
                rw_mutex.acquire() #khóa buffer chỉ cho luồng reader truy cập
            mutex.release()
            print(f"Reader {self.id} is reading... ,Reader count:{read_count}")
            time.sleep(random.randint(1, 3))
            print(f"Reader {self.id} read done!")
            mutex.acquire()
            read_count -= 1
            if read_count == 0:
                rw_mutex.release()
            mutex.release()
            time.sleep(random.randint(1, 2))
    
wr = []
rd = []
for i in range(NUM_READERS):
    a = writer(i)
    wr.append(a)
for i in range(NUM_WRITERS):
    b = reader(i)
    rd.append(b)
for i in range(NUM_READERS):
    wr[i].start()
for i in range(NUM_WRITERS):
    rd[i].start()
for i in range(NUM_READERS):
    wr[i].join()
for i in range(NUM_WRITERS):
    rd[i].join()
