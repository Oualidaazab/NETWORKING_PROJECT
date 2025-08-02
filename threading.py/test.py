import threading 
import time 
def first_name() : 
    for  i  in range(10) : 
        print("oualidé")  
        time.sleep(0.1)
def last_name() : 
    for i in range(10) : 
        print("aazab")
        time.sleep(0.1) 
TR1=threading.Thread(target=first_name) 
TR2=threading.Thread(target=last_name) 
TR1.start() 
TR2.start() 