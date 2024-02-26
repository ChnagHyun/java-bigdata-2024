# file: p32_review.py

#01
class Calculator:
    def __init__(self):
        self.calue = 0

    def add(self,val):
        self.value +=val

    def minus(self,val):
        self.value -=val    

cal = UpgradeCalculator(Calculator)
cal.add(10)
cal.minus(7)

print(cal.value)

#02
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self,val):
        self.value +=val

#06
def ttime(x):
    return x*3

print(list(map(ttime,[1,2,3,4])))

#07
print(max([-8, 2, 7,5, -3, 5, 0, 1]))
print(min([-8, 2, 7,5, -3, 5, 0, 1]))

#11
import datetime

curr = datetime.datetime.now()
print(f'{curr.year}/{curr.month:02d}/{curr.day:02d} {curr.hour}:{curr.minute}:{curr.second}')

#12