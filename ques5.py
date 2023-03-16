
from threading import *
class Num(Thread):
    def run(self):
        sum = 0
        for i in range(1,100):
            sum = sum + i
            print(sum)
            

            
class Add(Thread):
    def run(self):
        sum = 0
        for i in range(1,100):
            sum = sum + i
            print(sum)
            
            
            
obj1=Num()
obj2=Add()

obj1.start()
obj2.start()