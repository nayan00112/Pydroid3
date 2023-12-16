# 13 August, 2023
from threading import *
from time import sleep

class a(Thread):
    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)
    
o1=a()
o2=a()
print(id(o1), id(o2))

o1.start()
o2.start()