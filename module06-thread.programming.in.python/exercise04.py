from concurrent.futures import ThreadPoolExecutor
from random import randint
from threading import Thread


def draw_lottery_numbers(max, size):
    numbers = set()
    while len(numbers) < size:
        numbers.add(randint(1, max))
    numbers = list(numbers)
    numbers.sort()
    return numbers


lottery_numbers = []
with ThreadPoolExecutor(max_workers=8) as my_thread_pool:
    futures = []
    for i in range(0, 10000):
        future = my_thread_pool.submit(draw_lottery_numbers, 60, 6)
        futures.append(future)
    for future in futures:
        lottery_numbers.append(future.result())

for numbers in lottery_numbers:
    print(numbers)
