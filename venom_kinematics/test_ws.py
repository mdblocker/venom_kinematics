from venom_kinematics_lib import *
#----------------------------------

speed = .02

wake_up(speed)

headscan_x(speed)
headscan_y(speed)

for x in range(50, 0, -1):
    L1(90, x, 0)
    time.sleep(.02)

for y in range(0, 50, 1):
    L1(90, y, 0)
    time.sleep(.02)
