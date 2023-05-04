import threading
import time
import random
num_philosophers = 5

# tạo một danh sách semaphore biểu thi cho các đũa
chopsticks = [threading.Semaphore(1) for _ in range(num_philosophers)]

def philosopher(id):
    while True:
        # Để tránh xung đột đã sử dụng 2 semaphore liên tiếp
        # biểu thi cho đũa bên trái
        chopsticks[id].acquire()
        # biểu thi cho đũa bên phải
        chopsticks[(id + 1) % num_philosophers].acquire()
        # -------
        print("Philosopher", id, "is eating")
        time.sleep(random.randint(1, 3))
        # -------
        chopsticks[id].release()
        chopsticks[(id + 1) % num_philosophers].release()
        # -------
        print("Philosopher", id, "is thinking")
        time.sleep(random.randint(1, 3))
        # -------
        time.sleep(random.randint(1, 2))

# tạo ra danh sách thread
philosopher_threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(num_philosophers)]
#vòng lặp duyệt qua danh sách các thread
for thread in philosopher_threads:
    thread.start()
