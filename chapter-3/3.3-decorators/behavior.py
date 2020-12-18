import time
import random

def log(func):
    def wrapper():
        print(f'start = {time.time()}')
        func()
        print(f'end = {time.time()}')
    return wrapper

@log
def sort():
    nums = [random.randint(0,100) for _ in range(1,100)]
    nums.sort()
    print(nums)

sort()