import time
from kin_positions import sym
from kin_config import *
#---------------------------

# Leg 1 package

def L1_fstep(speed):
    L1()
    time.sleep(speed)
    L1()
    time.sleep(speed)

def L1_fpush(speed):
    L1()
    time.sleep(speed)
    L1()
    time.sleep(speed)

def L1_bstep(speed):
    L1()
    time.sleep(speed)
    L1()
    time.sleep(speed)

def L1_bpush(speed):
    L1()
    time.sleep(speed)
    L1()
    time.sleep(speed)

#----------------------------

# Leg 2 package

def L2_fstep(speed):
    L2()
    time.sleep(speed)
    L2()
    time.sleep(speed)

def L2_fpush(speed):
    L2()
    time.sleep(speed)
    L2()
    time.sleep(speed)

def L2_bstep(speed):
    L2()
    time.sleep(speed)
    L2()
    time.sleep(speed)

def L2_bpush(speed):
    L2()
    time.sleep(speed)
    L2()
    time.sleep(speed)

#----------------------------

# Leg 3 package

def L3_fstep(speed):
    ## Move leg 3 to forward position
    # pick leg up
    L3(70, 50, 40)
    time.sleep(speed)
    L3(70, 25, 38)
    time.sleep(speed)
    L3(70, 12.5, 36)
    time.sleep(speed)
    L3(70, 6.25, 34)
    time.sleep(speed)
    L3(70, 3.13, 32)
    time.sleep(speed)
    L3(70, 1.55, 31)
    time.sleep(speed)
    L3(70, 1, 30)
    time.sleep(speed)
    
    # set leg down
    L3(70, 50, 70)
    time.sleep(speed)
    L3(70, 75, 90)
    time.sleep(speed)
    L3(70, 87.5, 100)
    time.sleep(speed)
    L3(70, 94, 105)
    time.sleep(speed)
    L3(70, 97, 107.5)
    time.sleep(speed)
    L3(70, 98.5, 109)
    time.sleep(speed)
    L3(70, 100, 110)
    time.sleep(speed)

def L3_fpush(speed):
    L3()
    time.sleep(speed)
    L3()
    time.sleep(speed)

def L3_bstep(speed):
    ## Move leg 3 to sym position
    # pick leg up
    L3(70, 100, 110)
    time.sleep(speed)
    L3(70, 50, 55)
    time.sleep(speed)
    L3(70, 25, 27.5)
    time.sleep(speed)
    L3(70, 12.5, 13.75)
    time.sleep(speed)
    L3(70, 6.25, 6.88)
    time.sleep(speed)
    L3(70, 3.125, 3.4)
    time.sleep(speed)
    L3(70, 1.5, 1.7)
    time.sleep(speed)
    # set leg down
    L3(70, 25, 20)
    time.sleep(speed)
    L3(70, 37.5, 30)
    time.sleep(speed)
    L3(70, 43.75, 35)
    time.sleep(speed)
    L3(70, 46.875, 37.5)
    time.sleep(speed)
    L3(70, 48.45, 38.75)
    time.sleep(speed)
    L3(70, 49.5, 39.5)
    time.sleep(speed)
    L3(70, 50, 40)
    time.sleep(speed)

def L3_bpush(speed):
    L3()
    time.sleep(speed)
    L3()
    time.sleep(speed)

#---------------------------------

# Leg 4 package

def L4_fstep(speed):
    L4()
    time.sleep(speed)
    L4()
    time.sleep(speed)

def L4_fpush(speed):
    L4()
    time.sleep(speed)
    L4()
    time.sleep(speed)

def L4_bstep(speed):
    L4()
    time.sleep(speed)
    L4()
    time.sleep(speed)

def L4_bpush(speed):
    L4()
    time.sleep(speed)
    L4()
    time.sleep(speed)

#----------------------------

# Leg 5 package

def L5_fstep(speed):
    L5()
    time.sleep(speed)
    L5()
    time.sleep(speed)

def L5_fpush(speed):
    L5()
    time.sleep(speed)
    L5()
    time.sleep(speed)

def L5_bstep(speed):
    L5()
    time.sleep(speed)
    L5()
    time.sleep(speed)

def L5_bpush(speed):
    L5()
    time.sleep(speed)
    L5()
    time.sleep(speed)

#----------------------------

# Leg 6 package

def L6_fstep(speed):
    L6()
    time.sleep(speed)
    L6()
    time.sleep(speed)

def L6_fpush(speed):
    L6()
    time.sleep(speed)
    L6()
    time.sleep(speed)

def L6_bstep(speed):
    L6()
    time.sleep(speed)
    L6()
    time.sleep(speed)

def L6_bpush(speed):
    L6()
    time.sleep(speed)
    L6()
    time.sleep(speed)

#----------------------------
