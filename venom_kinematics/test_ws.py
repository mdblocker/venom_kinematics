from venom_kinematics_lib import *
#----------------------------------

speed = .02

wake_up(speed)

headscan_x(speed)
headscan_y(speed)

#1
for x in range(90, 0, -2):
    L1(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L1(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#6
for x in range(90, 0, -2):
    L6(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L6(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#3
for x in range(90, 0, -2):
    L3(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L3(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#4
for x in range(90, 0, -2):
    L4(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L4(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#2
for x in range(90, 0, -2):
    L2(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L2(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
#5
for x in range(90, 0, -2):
    L5(90, x, 30)
    time.sleep(.02)
time.sleep(speed)
for y in range(0, 90, 2):
    L5(90, y, 30)
    time.sleep(.02)
time.sleep(speed)
