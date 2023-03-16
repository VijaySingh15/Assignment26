from datetime import datetime
from time import sleep
from threading import *
class Current(Thread):
    def run(self):
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        print("Current time =",current_time)
        
class Delay(Thread):
    def run(self):
        print("1 Minute completed")
        
        
obj1 = Current()
obj2 = Delay()

obj1.start()
sleep(60)
obj2.start()
        
        