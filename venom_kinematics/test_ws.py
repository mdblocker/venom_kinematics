import time
from kin_positions import *
from kin_actions.kin_rotate_ccw import *
from kin_actions.kin_rotate_cw import *
from kin_actions.kin_sym2rest import *
from kin_actions.kin_rest2sym import *
from kin_actions.kin_spin_up import *
from kin_actions.kin_head_wakeup import *
#--------------------------------------

speed = .02

head_wakeup(speed)

head_angle_yes(35)
time.sleep(.2)
head_angle_no(90)
time.sleep(.2)
