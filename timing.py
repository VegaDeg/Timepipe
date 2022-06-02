import time

def check(nodeName):
    checkList.append(nodeName)
    timeList.append(time.time())

def displayNode():
    for i in range(len(checkList)-1):
        print(checkList[i] + " to " + checkList[i+1] + " took " + str(timeList[i+1]-timeList[i]) + " seconds")

checkList = []
timeList = []

check("node 1")
time.sleep(0.03)
check("node 2")
time.sleep(0.7)
check("node 3")

displayNode()