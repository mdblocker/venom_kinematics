import time
from kin_positions import *
#---------------------------

def sym_to_rest(speed):
    sym()
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

    # Move leg 4 to forward position
    # pick leg up
    L4(70, 50, 40)
    time.sleep(speed)
    L4(70, 25, 38)
    time.sleep(speed)
    L4(70, 12.5, 36)
    time.sleep(speed)
    L4(70, 6.25, 34)
    time.sleep(speed)
    L4(70, 3.13, 32)
    time.sleep(speed)
    L4(70, 1.55, 31)
    time.sleep(speed)
    L4(70, 1, 30)
    time.sleep(speed)
    
    # set leg down
    L4(70, 50, 70)
    time.sleep(speed)
    L4(70, 75, 90)
    time.sleep(speed)
    L4(70, 87.5, 100)
    time.sleep(speed)
    L4(70, 94, 105)
    time.sleep(speed)
    L4(70, 97, 107.5)
    time.sleep(speed)
    L4(70, 98.5, 109)
    time.sleep(speed)
    L4(70, 100, 110)
    time.sleep(speed)

    #target rest
    L1(110, 50, 40)
    L2(90, 50, 40)
    L3(70, 100, 110)

    L4(70, 100, 110)
    L5(90, 50, 40)
    L6(110, 50, 40)
    time.sleep(speed)
    
