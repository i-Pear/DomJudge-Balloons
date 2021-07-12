import queue
import threading
import time

q = queue.Queue()


class T1(threading.Thread):

    def run(self) -> None:
        while True:
            cnt = q.get()
            print(cnt)


class T2(threading.Thread):

    def run(self) -> None:
        for i in range(10):
            q.put(i)
            time.sleep(5)


if __name__ == '__main__':
    t1 = T1()
    t2 = T2()
    t1.start()
    t2.start()
