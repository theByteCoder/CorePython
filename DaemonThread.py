from threading import Thread


def func(limit):
    for x in range(limit):
        print(x)


t1 = Thread(target=func, args=(100000,), name="func")
t1.setDaemon(True)
t1.start()
t1.join()
print(t1.isDaemon())
