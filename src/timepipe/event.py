import time
from typing import MappingView


class event():

    def __init__(self, eventName=None):
        if not eventName:
            self.eventName = "Event"
        else:
            self.eventName = eventName
        self.timeList = []
        self.counter = 0

    def check(self):
        self.timeList.append(time.time())
        self.counter = self.counter + 1

    def timeInterval(self, kind="default"):
        if self.counter <= 1:
            return 0
        else:
            aveI = (self.timeList[-1] - self.timeList[0]) / (self.counter - 1)
            maxI = 0
            minI = 0
            diff = []
            for i in range(len(self.timeList)-1):
                diff.append(self.timeList[i+1] - self.timeList[i])
            maxI = max(diff)
            minI = min(diff)
        if kind == "default":
            return (aveI, maxI, minI)
        if kind == "average":
            return aveI
        if kind == "max":
            return maxI
        if kind == "min":
            return minI

    def eventHistory(self):
        if self.counter == 0:
            print("No check history")
        elif self.counter == 1:
            print("Only check at: " + self.timeList[0])
        else:
            print("first check at: " + str(self.timeList[0]))
            for i in range(1, self.counter):
                line = str(i+1) + "-th check at " + \
                    str(self.timeList[i] - self.timeList[i-1]
                        ) + " seconds later"
                print(line)
