from kin_config import *
import time
#-----------------------

def headscan_y(speed):
    for y in range(50, 90, 1):
        head_angle_yes(y)
        time.sleep(speed)
    for y in range(90,0,-1):
        head_angle_yes(y)
        time.sleep(speed)
    for y in range(0, 50, 1):
        head_angle_yes(y)
        time.sleep(speed)

