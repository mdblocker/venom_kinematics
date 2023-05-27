from venom_kinematics_lib import *
#----------------------------------

speed = .02

wake_up(speed)

for x in range(50, 5, -2):
    L1(90, x, 0)
    time.sleep(speed) 
for x in range(5, 50, 2):
    L1(90, x, 0)
    time.sleep(speed)
    