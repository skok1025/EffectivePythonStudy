import time


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'총 {delta:.3} 초 걸렸습니다.')  # 0.21


# multi thread 구현
from threading import Thread

class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()

threads = [] # 쓰레드를 담을 리스트
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()  # 쓰레드가 끝날 때까지 기다립니다.

end = time.time()
delta = end - start
print(f'총 {delta:.3} 초 걸렸습니다.')  # 0.209