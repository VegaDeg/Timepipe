import src.timepipe.event as ti
import time

event1 = ti.event("cjb")
event1.check()
time.sleep(1)
event1.check()
time.sleep(2)
event1.check()

event1.eventHistory()
print(event1.framerate())
