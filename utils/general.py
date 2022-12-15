from datetime import date
from time import sleep
from threading import Thread


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