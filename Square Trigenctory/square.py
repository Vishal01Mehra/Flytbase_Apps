#!/usr/bin/env python
import time
from flyt_python import api

drone = api.navigation(timeout=120000)

takeoffDist = 5.0 # takeoff Altitude
ThrehBatt = 12.2 # Threshold Battery level

time.sleep(5) 

bat = drone.get_battery_status()
if bat.voltage > ThrehBatt:
    drone.arm() # Arm the done
    print("taking off at" + str(takeoffDist) + "m")
    drone.take_off(takeoffDist) # takeoff the drone

    print("Moving in a square")
    drone.position_set(6.5, 0, 0, relative=True)
    drone.position_set(0, 6.5, 0, relative=True)
    drone.position_set(-6.5, 0, 0, relative=True)
    drone.position_set(0, -6.5, 0, relative=True)

    print ("Landing The Drone")
    drone.land() # Land the drone
    time.sleep(1) # wait for 1 sec 
    drone.disarm() # Disarm the drone 
    drone.disconnect()
else:
    print("Aborting script Battery too Low: " + str(bat.voltage) + "V" )
