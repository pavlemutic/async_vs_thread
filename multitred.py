import threading
from time import sleep
from datetime import datetime


def deep_sleep(num, time):
    print(f"{num} - pre: {time}")
    sleep(time)
    print(f"{num} - post: {time}")


def first():
    t1 = threading.Thread(target=deep_sleep, args=("11", 1, ))
    t2 = threading.Thread(target=deep_sleep, args=("12", 2, ))
    t3 = threading.Thread(target=deep_sleep, args=("13", 0, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def second():
    t1 = threading.Thread(target=deep_sleep, args=("21", 2,))
    t2 = threading.Thread(target=deep_sleep, args=("22", 1,))
    t3 = threading.Thread(target=deep_sleep, args=("23", 0,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def third():
    t1 = threading.Thread(target=deep_sleep, args=("31", 2,))
    t2 = threading.Thread(target=deep_sleep, args=("32", 0,))
    t3 = threading.Thread(target=deep_sleep, args=("33", 1,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


def loop():
    tf = threading.Thread(target=first, args=())
    ts = threading.Thread(target=second, args=())
    tt = threading.Thread(target=third, args=())

    tf.start()
    ts.start()
    tt.start()

    tf.join()
    ts.join()
    tt.join()


if __name__ == '__main__':
    start = datetime.now()
    loop()
    print(f"total: {datetime.now() - start}")


# results:
# 11 - pre: 1
# 21 - pre: 2
# 12 - pre: 2
# 22 - pre: 1
# 13 - pre: 0
# 31 - pre: 2
# 23 - pre: 0
# 13 - post: 0
# 23 - post: 0
# 32 - pre: 0
# 32 - post: 0
# 33 - pre: 1
# 11 - post: 1
# 22 - post: 1
# 33 - post: 1
# 21 - post: 2
# 12 - post: 2
# 31 - post: 2
# total: 0:00:02.005883
