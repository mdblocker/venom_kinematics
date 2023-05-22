from kin_config import *
from kin_positions import *
import time
#-----------------------

def wake_up(angle, interval, speed):
    rest()
    for x in range(0, angle, interval):
        L1(90, x, 0)
        L2(90, x, 0)
        L3(90, x, 0)
        L4(90, x, 0)
        L5(90, x, 0)
        L6(90, x, 0)
    
        time.sleep(speed)


