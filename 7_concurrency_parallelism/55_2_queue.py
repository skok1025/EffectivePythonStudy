import time
from queue import Queue
from threading import Thread

my_queue = Queue()

def consumer():
    print('Consumer waiting')
    my_queue.get()  # Runs after put() below
    print('Consumer done')

thread = Thread(target=consumer)
thread.start()

print('Producer putting')
my_queue.put(object())  # Runs before get() above
thread.join()
print('Producer done')

my_queue = Queue(1)  # Buffer size of 1
def consumer1():
    time.sleep(0.1)  # Wait
    my_queue.get()  # Runs second
    print('Consumer got 1')
    my_queue.get()  # Runs fourth
    print('Consumer got 2')
    print('Consumer done')

thread = Thread(target=consumer1)
thread.start()

my_queue.put(object())
print('Producer put 1')

my_queue.put(object())
print('Producer put 2')