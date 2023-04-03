import time
from kin_positions import *
from kin_actions.kin_rotate_ccw import *
from kin_actions.kin_rotate_cw import *
from kin_actions.kin_sym2rest import *
from kin_actions.kin_rest2sym import *
from kin_actions.kin_spin_up import *
#--------------------------------------

head_angle(0)
time.sleep(1)
head_angle(90)
time.sleep(1)
head_angle(180)
time.sleep(1)

