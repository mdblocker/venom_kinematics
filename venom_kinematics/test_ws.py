import time
from kin_positions import *
from kin_actions.kin_rotate_ccw import *
from kin_actions.kin_rotate_cw import *
from kin_actions.kin_sym2rest import *
from kin_actions.kin_rest2sym import *
from kin_actions.kin_spin_up import *
from kin_actions.kin_head_wakeup import *
#--------------------------------------

speed = .2

head_wakeup(speed)
rotate_cw(speed)
rotate_cw(speed)
rotate_cw(speed)
rotate_ccw(speed)
rotate_ccw(speed)
rotate_ccw(speed)

