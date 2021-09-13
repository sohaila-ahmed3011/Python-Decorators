import time, io
import contextlib

def first_decorator(func):
    count = 0
    def wrapper(*arg, **kwarg):
        nonlocal count
        count += 1
        start_time = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*arg, **kwarg)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"{func.__name__} call {count} in {runtime} sec")
        
    return wrapper


