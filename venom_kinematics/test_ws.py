from venom_kinematics_lib import *
#----------------------------------

speed = .02

wake_up(speed)

headscan_x(speed)
headscan_y(speed)

#3
for x in range(100, 0, -4):
    L3(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 100, 4):
    L3(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#4
for x in range(100, 0, -4):
    L4(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 100, 4):
    L4(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
