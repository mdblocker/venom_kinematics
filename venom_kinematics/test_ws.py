from venom_kinematics_lib import *
#----------------------------------

speed = .02

wake_up(speed)

headscan_x(speed)
headscan_y(speed)

#1
for x in range(50, 0, -1):
    L1(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L1(90, y, 0)
    time.sleep(.02)
time.sleep(speed)
#6
for x in range(50, 0, -1):
    L6(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L6(90, y, 0)
    time.sleep(.02)
time.sleep(speed)
#3
for x in range(50, 0, -1):
    L3(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L3(90, y, 0)
    time.sleep(.02)
time.sleep(speed)
#4
for x in range(50, 0, -1):
    L4(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L4(90, y, 0)
    time.sleep(.02)
time.sleep(speed)
#2
for x in range(50, 0, -1):
    L2(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L2(90, y, 0)
    time.sleep(.02)
time.sleep(speed)
#5
for x in range(50, 0, -1):
    L5(90, x, 0)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 30, 1):
    L5(90, y, 0)
    time.sleep(.02)
time.sleep(speed)