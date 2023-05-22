from kin_config import *
import time
#-----------------------

def headscan_x(speed):
    for x in range(90, 110, 1):
        head_angle_no(x)
        time.sleep(speed)
    for x in range(110, 70, -1):
        head_angle_no(x)
        time.sleep(speed)
    for x in range(70, 90, 1):
        head_angle_no(x)
        time.sleep(speed)