from threading import Thread, current_thread
from time import sleep

t = 0


def func1(a, b, c, d):
    print('thread 1 started')
    sleep(15)
    # print(a + b + c + d)
    global t
    t = current_thread().getName()
    print('thread 1 stopped')


def func2(a, b):
    print('thread 2 started')
    # sleep(5)
    # print(a + b)
    while t == 0:
        pass
    else:
        print('found t, printing t')
        sleep(5)
        print(id(t))
    print('thread 2 stopped')


thread_func1 = Thread(target=func1, args=(1, 2, 3, 4))
thread_func2 = Thread(target=func2, args=(1, 2))

thread_func1.start()
thread_func2.start()
