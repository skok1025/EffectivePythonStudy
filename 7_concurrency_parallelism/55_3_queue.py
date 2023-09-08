from queue import Queue
from threading import Thread

in_queue = Queue()

def consumer():
    print('Consumer waiting\n')
    work = in_queue.get()
    print('Consumer working\n')
    # Doing work
    print('Consumer done\n')
    in_queue.task_done()

thread = Thread(target=consumer)
thread.start()

print('Producer putting\n')
in_queue.put(object())
print('Producer waiting\n')
in_queue.join()
print('Producer done\n')
thread.join()

