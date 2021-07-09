import threading
import time

start = time.perf_counter()


def task(seconds):
    print(f'Sleeping for {seconds} second')
    time.sleep(seconds)
    print('Done sleeping \n')


threads = []

for _ in range(10):
    thread = threading.Thread(target=task, args=[2])
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Time taken {finish - start} seconds')
