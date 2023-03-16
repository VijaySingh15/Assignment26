from time import sleep
from threading import *
class Even(Thread):
    def run(self):
        for i in range(2,101,2):
            print(i)
            sleep(1)
            

            
class Odd(Thread):
    def run(self):
        for i in range(1,100,2):
            print(i)
            sleep(1)
            
            
            
obj1=Even()
obj2=Odd()

obj1.start()
obj2.start()