# first what is threading in general ?  
# the threading module provides a way to run multiple threads (smaller units of a process) concurrently within a 
# single process. It allows for the creation and management of threads, making it possible to execute tasks in par 
# allel, sharing memory space. Threads are particularly useful when tasks are I/O bound, such as file operations or 
# making network requests, where much of the time is spent waiting for external resources.
import threading
import time

def first_name():
    for i in range(10):
        print("oualid")
        time.sleep(0.1)  # small delay

def last_name():
    for i in range(10):
        print("aazab")
        time.sleep(0.1)  # small delayszqD

TR1 = threading.Thread(target=first_name)
TR2 = threading.Thread(target=last_name)

TR1.start()
TR2.start()


