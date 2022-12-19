from datetime import date
from time import sleep
from threading import Thread
import os


def create_file_if_not_exist(file, on_create=''):
    out = False
    if not os.path.exists(file):
        csv = open(file, 'w')
        csv.write(on_create)
        csv.close()
        out = True

    return out        


def today() -> str:
    return date.today().strftime("%d/%m/%Y")


def execute(func, args=None, prev_wait=0, for_wait=0, thread=True) -> None:
    sleep(prev_wait)
    if thread:
        arg = args if type(args) == list or args == None else [args] 
        Thread(target=func, args=arg).start() 
    else:
        if type(args) == list:
            func(*args)
        else:
            func() if args == None else func(args)
    
    sleep(for_wait)