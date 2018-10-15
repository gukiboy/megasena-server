import time
from datetime import datetime

class Lottery:
    pickedNumber = None
    lotteryTime  = None

    def __init__(self):
        self.pickedNumber = 10
        self.lotteryTime = datetime.fromtimestamp(1539572700)

    def setPickedNumber(self,number):
        self.pickedNumber = number

    def setTime(self, lotTime):
        self.lotteryTime = lotTime
