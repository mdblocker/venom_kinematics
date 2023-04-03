import time
from kin_positions import *
#---------------------------

def rest_to_sym(speed):
    rest()
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

    # Move leg 4 back
    # pick leg up
    L4(70, 100, 110)
    time.sleep(speed)
    L4(70, 50, 55)
    time.sleep(speed)
    L4(70, 25, 27.5)
    time.sleep(speed)
    L4(70, 12.5, 13.75)
    time.sleep(speed)
    L4(70, 6.25, 6.88)
    time.sleep(speed)
    L4(70, 3.125, 3.4)
    time.sleep(speed)
    L4(70, 1.5, 1.7)
    time.sleep(speed)
    # set leg down
    L4(70, 25, 20)
    time.sleep(speed)
    L4(70, 37.5, 30)
    time.sleep(speed)
    L4(70, 43.75, 35)
    time.sleep(speed)
    L4(70, 46.875, 37.5)
    time.sleep(speed)
    L4(70, 48.45, 38.75)
    time.sleep(speed)
    L4(70, 49.5, 39.5)
    time.sleep(speed)
    L4(70, 50, 40)
    time.sleep(speed)
    