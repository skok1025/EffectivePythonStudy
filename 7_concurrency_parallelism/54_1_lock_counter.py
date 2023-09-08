class Counter:
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        # 센서 번호에 해당하는 카운터를 1 증가시킵니다.
        counter.increment(1)


from threading import Thread

how_many = 10**5
counter = Counter()
threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f'카운터 값은 {expected} 이어야 하는데, 실제로는 {found} 입니다.')  # 500000
