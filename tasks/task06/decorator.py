import time

def measure_elapsed_time(func):
    def wrapper(*args, **kwargs):
        print('calling', func.__name__)
        start_time = time.time()
        func(*args, **kwargs)
        # print(func.__name__, 'call took', (time.time() - start_time), 'seconds')
        print(f"{func.__name__!r} call took {(time.time() - start_time):.1f} secs")
    return wrapper

@measure_elapsed_time
def my_fn1(arg1, arg2):
   time.sleep(0.5)
   return arg1 + arg2

@measure_elapsed_time
def my_fn2():
   time.sleep(0.8)
   print("I do nothing! What a life")

@measure_elapsed_time
def my_fn3(arg1, **kwargs):
   time.sleep(0.3)
   print(f"I also do nothing, but I have arg1 = {arg1} and kwargs = {kwargs}")

my_fn1(0, 2)
my_fn2()
my_fn3(12, kwarg1='lol', kwarg2='kek')
