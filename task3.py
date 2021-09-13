import time,  io
import contextlib
import inspect

global dic
dic = {}
class third_decorator:
    def __init__(self, func):
        self.func = func
        self.count = 0
        #global dict
        #dict ={}

    def __call__(self, *arg, **kwarg):
        self.count += 1
        start_time = time.time()
        with contextlib.redirect_stdout(io.StringIO()) as file:
            self.func(*arg, **kwarg)
        end_time = time.time()
        runtime = end_time - start_time 
        dumped_values = file.getvalue()

        dic[self.func.__name__] = time.time() - start_time 
        if len(dic)==4:   
            L = sorted(dic.items(), key = lambda x: (x[1],x[0]))
            print("PROGRAM  |  RANK  |  TIME ELAPSED")
            i = 1
            for item in L:
                print (item[0], '       ',i,'      ',item[1])   
                i += 1

        with open('t3.txt', 'a') as f:
            f.write(f"{self.func.__name__} call {self.count} in {runtime} sec" + '\n')
            f.write(("Name: \t"+ self.func.__name__) + '\n')
            f.write("Type: \t" + str(type(self.func)) + '\n')
            f.write("Sign: \t" + str(inspect.signature(self.func)) + '\n')
            f.write("Args:\t" + "positional" + str(arg) + "\n" + "\t key=worded" + str(kwarg) + '\n')
            f.write("Doc:  \t" + str(inspect.getdoc(self.func)) + "\n")
            f.write("Source: " + str(inspect.getsource(self.func)) + "\n")
            f.write("Output: {}" .format(dumped_values))

        # return self.func(*arg, **kwarg)


