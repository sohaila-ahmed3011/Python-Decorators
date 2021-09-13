import time

def fourth_decorator(func):
    def wrapper(*args,**kwarg):
        try:
            func(*args,**kwarg)
        except Exception as err:
            with open('logfile.txt','a') as f:
                f.write(str(err) +'\n')                             
                f.write(time.strftime("%Y-%m-%d %H:%M:%S")+'\n')             
    return wrapper