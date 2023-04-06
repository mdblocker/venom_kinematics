from kin_config import *
from kin_actions.kin_nod import *
from kin_actions.kin_sup import *
import time
#-----------------------

def headscan_y(speed):

    head_nod(speed)
    head_angle_yes(50)
    time.sleep(speed)
    head_sup(speed)
    head_angle_yes(50)
    time.sleep(speed)
