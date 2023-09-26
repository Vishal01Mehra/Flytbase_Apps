#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)

takeoffDist = 10.0
ThrehBatt = 12.2 # Threshold Battery level

time.sleep(5)
bat = drone.get_battery_status()
if bat.voltage > ThrehBatt:
    drone.arm() # Arm the done
    print("taking off at" + str(takeoffDist) + "m")
    drone.take_off(takeoffDist) # takeoff the drone

    print("Moving in a Triangle")
    drone.position_set(-8, 6, 0, relative=True) # Basic Pythagorean theorem (a2 + b2 = c2) for the hypotenus of 10m
    drone.position_set(8, 6, 0, relative=True) 
    drone.position_set(0, -10, 0,relative=True) # Move back to the origin 

    print ("Landing The Drone")
    drone.land() # Land the drone
    time.sleep(1) # wait for 1 sec 
    drone.disarm() # Disarm the drone 
    drone.disconnect() 
else:
    print("Aborting script Battery too Low: " + str(bat.voltage) + "V" )