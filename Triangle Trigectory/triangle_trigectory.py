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

    print("taking off at" + takeoffDist)
    drone.take_off(takeoffDist) # takeoff the drone

    print("Moving in a Triangle")
    drone.position_set(0, 0, 0, yaw = 1.0472, tolerance=0.5, yaw_valid=True,  body_frame=True) # yaw = 1.0472 (60 degrees in radians)
    drone.position_set(10, 0, 0, relative=True) # move forward by 10m
    drone.position_set(0, 0, 0, yaw = 1.0472, tolerance=0.5, yaw_valid=True,  body_frame=True) # Yaw 60 degree
    drone.position_set(10, 0, 0, relative=True) # move forward by 10m
    drone.position_set(0, 0, 0, yaw = 1.0472, tolerance=0.5, yaw_valid=True,  body_frame=True) # Yaw gain 60 degree
    drone.position_set(10, 0, 0, relative=True) # move forward by 10m

    print ("Landing The Drone")
    drone.land() # Land the drone
    time.sleep(1) # wait for 1 sec 
    drone.disarm() # Disarm the drone 
    drone.disconnect() 
else:
    print("Aborting script Battery too Low: " + bat.voltage )