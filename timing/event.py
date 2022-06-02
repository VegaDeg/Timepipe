import time

objectList = []

class event():
    def __init__(self, eventName):
        self.eventName = eventName
        self.timeList = []
        objectList.append(self)

    def check(self):
        self.timeList.append(time.time())

def displayEvent():
    print(len(objectList))
    for i in range(0, len(objectList)-1):
        print(i)
        print(objectList[i].eventName + " to " + objectList[i+1].eventName + " took " + str(objectList[i+1].timeList[0]-objectList[i].timeList[0]) + " seconds")


event1 = event("event 1")
event2 = event("event 2")
event3 = event("event 3")

event1.check()
time.sleep(1)
event2.check()
time.sleep(1)
event3.check()

displayEvent()