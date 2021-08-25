import time
import random
from threading import Lock, Thread


class Flight:

    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.locker = Lock()

    def reserve(self, user_name, required_seats, wait_time):
        self.locker.acquire()
        if self.available_seats > 0:
            if self.available_seats >= required_seats:
                time.sleep(wait_time)
                print(f'{required_seats} seats allotted to {user_name}')
                self.available_seats -= required_seats
        else:
            print(f'sorry {user_name}, your we do not have {required_seats} seats')
        self.locker.release()


flight = Flight(10)
user_1 = Thread(target=flight.reserve, args=('user_1', 5, random.randint(1, 4)))
user_2 = Thread(target=flight.reserve, args=('user_2', 4, random.randint(1, 6)))
user_3 = Thread(target=flight.reserve, args=('user_3', 2, random.randint(1, 1)))
user_4 = Thread(target=flight.reserve, args=('user_4', 3, random.randint(1, 5)))
user_5 = Thread(target=flight.reserve, args=('user_5', 1, random.randint(1, 2)))
user_1.start()
user_2.start()
user_3.start()
user_4.start()
user_5.start()
user_1.join()
user_2.join()
user_3.join()
user_4.join()
user_5.join()
print('flight take off')
