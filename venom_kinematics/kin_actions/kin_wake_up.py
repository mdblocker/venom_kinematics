from kin_config import *
from kin_positions import *
import time
#-----------------------

def wake_up(speed):


    L1(90, 0, 0)
    L2(90, 0, 0)
    L3(90, 0, 0)
    L4(90, 0, 0)
    L5(90, 0, 0)
    L6(90, 0, 0)
    time.sleep(speed)
   
    L1(90, 50, 30)
    L2(90, 50, 30)
    L3(90, 50, 30)
    L4(90, 50, 30)
    L5(90, 50, 30)
    L6(90, 50, 30)
    time.sleep(speed)

       
   