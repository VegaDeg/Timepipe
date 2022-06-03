import time

class event():
    def __init__(self):
        self.eventName = "Event"
        self.timeList = []
        self.counter = 0

    def __init__(self, eventName):
        self.eventName = eventName
        self.timeList = []
        self.counter = 0

    def check(self):
        self.timeList.append(time.time())
        self.counter = self.counter + 1
        
    def framerate(self):
        if self.counter <= 1:
            return 0
        else:
            return (self.timeList[-1] - self.timeList[0]) / (self.counter - 1)

    def eventHistory(self):
        if self.counter == 0:
            print("No check history")
        elif self.counter == 1:
            print("Only check at: " + self.timeList[0])
        else:
            print("first check at: " + str(self.timeList[0]))
            for i in range(1, self.counter):
                line = str(i+1) + "-th check at " + str(self.timeList[i] - self.timeList[i-1]) + " seconds later"
                print(line)
