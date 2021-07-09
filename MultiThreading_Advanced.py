import concurrent.futures
import threading
import time

start = time.perf_counter()


def task(second):
    print(f'Sleeping for {second} second')
    time.sleep(second)
    return f'Done sleeping for {second}\n'


with concurrent.futures.ThreadPoolExecutor() as executor:
    seconds = [1, 2, 3, 4, 5]
    seconds.reverse()
    future = [executor.submit(task, second) for second in seconds]
    for thread in concurrent.futures.as_completed(future):
        print(thread.result())

# threads = []
#
# for _ in range(10):
#     thread = threading.Thread(target=task, args=[2])
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Time taken {finish - start} seconds')
