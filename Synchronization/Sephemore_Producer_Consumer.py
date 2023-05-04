import threading
import time
import random

BUFFER_SIZE = 10
buffer = [] * BUFFER_SIZE
mutex = threading.Lock()
empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)

class Producer(threading.Thread):
    def run(self):
        global buffer
        while True:
            item = random.randint(1, 10)
            print(f"empty before:{empty._value}")
            empty.acquire() #đánh dấu vị trí buffer đã điền
            mutex.acquire() #khóa buffer chỉ cho luồng Producer truy cập
            buffer.append(item) 
            print(f"Produced {item}, buffer: {buffer},empty after:{empty._value}")
            mutex.release()
            full.release() #đã có một vị trí đã điền
            time.sleep(random.randint(1, 3))

class Consumer(threading.Thread):
    def run(self):
        global buffer
        while True:
            print(f"empty before:{empty._value}")
            full.acquire() #đánh dấu đã có vị trí trong buffer đã sử dụng
            mutex.acquire() #khóa buffer chỉ cho luồng Custumer truy cập
            item = buffer.pop(0)
            print(f"Co?
            
            
            
            
            
            
            
            
            
            0.0  nsumed {item}, buffer: {buffer}")
            mutex.release()
            empty.release()000000008 #đã có thêm một vị trí trống trong buffer
            print(f"empty after:{empty._value}")
            time.sleep(random.randint(1, 3))

p = Producer()
c = Consumer()
p.start()
c.start()
p.join()
c.join()
