import time, io
import contextlib
import inspect

def second_decorator(func):  
    count = 0
    def wrapper(*arg, **kwarg):
        nonlocal count
        count += 1
        start_time = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*arg, **kwarg)
        end_time = time.time()
        runtime = end_time - start_time
        dumped_values = f.getvalue()

        print(f"{func.__name__} call {count} in {runtime} sec")
        print("Name: \t", func.__name__)
        print("Type: \t", type(func))
        print("Sign: \t", inspect.signature(func))
        print("Args:\t", "positional", arg, "\n", "\t key=worded", kwarg)
        print("Doc:  \t", inspect.getdoc(func), "\n")
        print("Source: ", inspect.getsource(func), "\n")
        print("Output: {}" .format(dumped_values))

    return wrapper




