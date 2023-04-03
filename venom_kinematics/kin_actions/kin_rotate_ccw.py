import time
from kin_positions import sym
from kin_config import *
#---------------------------

def rotate_ccw(speed):
    sym()
    # move leg odds up
    L6(110, 30, 40)
    L5(90, 60, 40)
    L4(70, 30, 40)
    L3(70, 60, 40)
    L2(90, 30, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(110, 20, 40)
    L5(90, 60, 40)
    L4(70, 20, 40)
    L3(70, 60, 40)
    L2(90, 20, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(110, 15, 40)
    L5(90, 60, 40)
    L4(70, 15, 40)
    L3(70, 60, 40)
    L2(90, 15, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(110, 12.5, 40)
    L5(90, 60, 40)
    L4(70, 12.5, 40)
    L3(70, 60, 40)
    L2(90, 12.5, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(110, 11.75, 40)
    L5(90, 60, 40)
    L4(70, 11.75, 40)
    L3(70, 60, 40)
    L2(90, 11.75, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(110, 10, 40)
    L5(90, 60, 40)
    L4(70, 10, 40)
    L3(70, 60, 40)
    L2(90, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)

    # odds swing cw
    time.sleep(speed)
    L6(90, 10, 40)
    L5(90, 60, 40)
    L4(50, 10, 40)
    L3(70, 60, 40)
    L2(110, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(80, 10, 40)
    L5(90, 60, 40)
    L4(40, 10, 40)
    L3(70, 60, 40)
    L2(120, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(75, 10, 40)
    L5(90, 60, 40)
    L4(35, 10, 40)
    L3(70, 60, 40)
    L2(125, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(72.5, 10, 40)
    L5(90, 60, 40)
    L4(32.5, 10, 40)
    L3(70, 60, 40)
    L2(127.5, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(71.25, 10, 40)
    L5(90, 60, 40)
    L4(31.25, 10, 40)
    L3(70, 60, 40)
    L2(128.75, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 10, 40)
    L5(90, 60, 40)
    L4(30, 10, 40)
    L3(70, 60, 40)
    L2(130, 10, 40)
    L1(110, 60, 40)
    time.sleep(speed)

    # move odds down
    L6(70, 35, 40) 
    L5(90, 60, 40)
    L4(30, 35, 40)
    L3(70, 60, 40)
    L2(130, 35, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 47.5, 40) 
    L5(90, 60, 40)
    L4(30, 47.5, 40)
    L3(70, 60, 40)
    L2(130, 47.5, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 53.75, 40) 
    L5(90, 60, 40)
    L4(30, 53.75, 40)
    L3(70, 60, 40)
    L2(130, 53.75, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 56.9, 40) 
    L5(90, 60, 40)
    L4(30, 56.9, 40)
    L3(70, 60, 40)
    L2(130, 56.9, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 58.5, 40) 
    L5(90, 60, 40)
    L4(30, 58.5, 40)
    L3(70, 60, 40)
    L2(130, 58.5, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 59.25, 40) 
    L5(90, 60, 40)
    L4(30, 59.25, 40)
    L3(70, 60, 40)
    L2(130, 59.25, 40)
    L1(110, 60, 40)
    time.sleep(speed)
    L6(70, 60, 40) 
    L5(90, 60, 40)
    L4(30, 60, 40)
    L3(70, 60, 40)
    L2(130, 60, 40)
    L1(110, 60, 40)
    time.sleep(speed)

    # pick up evens
    L6(70, 60, 40)
    L5(90, 40, 40)
    L4(30, 60, 40)
    L3(70, 40, 40)
    L2(130, 60, 40)
    L1(110, 40, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 25, 40)
    L4(30, 60, 40)
    L3(70, 25, 40)
    L2(130, 60, 40)
    L1(110, 25, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 25, 40)
    L4(30, 60, 40)
    L3(70, 25, 40)
    L2(130, 60, 40)
    L1(110, 25, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 17.5, 40)
    L4(30, 60, 40)
    L3(70, 17.5, 40)
    L2(130, 60, 40)
    L1(110, 17.5, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 13.75, 40)
    L4(30, 60, 40)
    L3(70, 13.75, 40)
    L2(130, 60, 40)
    L1(110, 13.75, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 11.5, 40)
    L4(30, 60, 40)
    L3(70, 11.5, 40)
    L2(130, 60, 40)
    L1(110, 11.5, 40)
    time.sleep(speed)
    L6(70, 60, 40)
    L5(90, 10, 40)
    L4(30, 60, 40)
    L3(70, 10, 40)
    L2(130, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)

    # and rotate odds home
    L6(90, 60, 40)
    L5(90, 10, 40)
    L4(50, 60, 40)
    L3(70, 10, 40)
    L2(110, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)
    L6(100, 60, 40)
    L5(90, 10, 40)
    L4(60, 60, 40)
    L3(70, 10, 40)
    L2(100, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)
    L6(105, 60, 40)
    L5(90, 10, 40)
    L4(65, 60, 40)
    L3(70, 10, 40)
    L2(95, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)
    L6(107.5, 60, 40)
    L5(90, 10, 40)
    L4(67.5, 60, 40)
    L3(70, 10, 40)
    L2(92.5, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)
    L6(108.75, 60, 40)
    L5(90, 10, 40)
    L4(68.75, 60, 40)
    L3(70, 10, 40)
    L2(90.75, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 10, 40)
    L4(70, 60, 40)
    L3(70, 10, 40)
    L2(90, 60, 40)
    L1(110, 10, 40)
    time.sleep(speed)

    # set down evens
    # and return to sym
    L6(110, 60, 40)
    L5(90, 30, 40)
    L4(70, 60, 40)
    L3(70, 30, 40)
    L2(90, 60, 40)
    L1(110, 30, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 40, 40)
    L4(70, 60, 40)
    L3(70, 40, 40)
    L2(90, 60, 40)
    L1(110, 40, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 45, 40)
    L4(70, 60, 40)
    L3(70, 45, 40)
    L2(90, 60, 40)
    L1(110, 45, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 45, 40)
    L4(70, 60, 40)
    L3(70, 45, 40)
    L2(90, 60, 40)
    L1(110, 45, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 47.5, 40)
    L4(70, 60, 40)
    L3(70, 47.5, 40)
    L2(90, 60, 40)
    L1(110, 47.5, 40)
    time.sleep(speed)
    L6(110, 60, 40)
    L5(90, 49, 40)
    L4(70, 60, 40)
    L3(70, 49, 40)
    L2(90, 60, 40)
    L1(110, 49, 40)
    time.sleep(speed)
    sym()