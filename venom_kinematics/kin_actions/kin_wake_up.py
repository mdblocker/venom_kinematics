from kin_config import *
from kin_positions import *
import time
#-----------------------

def wake_up(speed):
   
    L1(90, 50, 0)
    L2(90, 50, 0)
    L3(90, 50, 0)
    L4(90, 50, 0)
    L5(90, 50, 0)
    L6(90, 50, 0)
    time.sleep(speed)

    for x in range(50, 0, 2):
        L1(90, x, 0)
        time.sleep(speed)
    time.sleep(speed)
    for x in range(0, 50, 2):
        L1(90, x, 0)
        time.sleep(speed)
    time.sleep(speed)
        
      
