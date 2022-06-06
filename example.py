import src.timepipe.event as ti
import time

event1 = ti.event()
print(event1.eventName)
event2 = ti.event("gjby")
print(event2.eventName)

event1.check()
time.sleep(1)
event1.check()
time.sleep(2)
event1.check()

event1.eventHistory()
print("all shown: ", event1.timeInterval())
print("all shown: ", event1.timeInterval("default"))
print("average: ", event1.timeInterval("average"))
print("max: ", event1.timeInterval("max"))
print("min: ", event1.timeInterval("min"))
