import threading
import time

N = 100_000_000


def count(n):
    while n > 0:
        n -= 1


def run():
    t1 = time.time()
    count(N)
    t2 = time.time()
    print("singe time", t2 - t1)


    n_threads = 10

    threads = [
        threading.Thread(target=count, args=(N // n_threads,))
        for i in range(n_threads)
    ]
    t1 = time.time()
    for th in threads:
        th.start()
    for th in threads:
        th.join()

    t2 = time.time()
    print("thread time", t2 - t1)


if __name__ == "__main__":
    run()
