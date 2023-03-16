from time import sleep
from threading import *
class First(Thread):
    def run(self):
        for i in range(1,20):
            print(i)
            sleep(1)
    
class Second(Thread):
    def run(self):
        for i in range(21,40):
            print(i)
            sleep(1)

class Third(Thread):
    def run(self):
        for i in range(41,60):
            print(i)
            sleep(1)
            
class Fourth(Thread):
    def run(self):
        for i in range(61,80):
            print(i)
            sleep(1)
            
class Fifth(Thread):
    def run(self):
        for i in range(81,101):
            print(i)
            sleep(1)
            
first=First()
sec=Second()
third=Third()
four=Fourth()
five=Fifth()

first.start()
sec.start()
third.start()
four.start()
five.start()
