#!/usr/bin/python
# coding: utf8
"""MMM-Switch - MagicMirror Module
Distance Measuring Script
The MIT License (MIT)

Based on work by
Paul-Vincent Roll (Copyright 2016) (MIT License)
and Tony DiCola (Copyright 2013) (MIT License)"""

#Import libraries
import RPi.GPIO as GPIO
import time
import json
import config
import sys

def to_node(type, message):
    # convert to json and print (node helper will read from stdout)
    try:
        print(json.dumps({type: message}))
    except Exception:
        pass
    # stdout has to be flushed manually to prevent delays in the node helper communication
    sys.stdout.flush()
   
def distance_right():
        
    # set Trigger to  HIGH
    GPIO.output(GPIO_TRIGGER_RIGHT, True)
 
 
    # set Tigger to LOW after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_RIGHT, False)

    # init start and stop time
    StartZeit = time.time()
    StopZeit = time.time()

    # workaround without module tends to crash
    new_reading = False
    counter = 0

    
    # save start time
    while GPIO.input(GPIO_ECHO_RIGHT) == 0:
        if counter == 50000:
            new_reading = True
            break
        StartZeit = time.time()
        counter += 1

    if new_reading:
        to_node("status", "Error occured: starting new measurement")
        return 100

    
    # save stop time
    while GPIO.input(GPIO_ECHO_RIGHT) == 1:
        StopZeit = time.time()

    
    # Calulate time difference
    TimeElapsed = StopZeit - StartZeit
    # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
    # und durch 2 teilen, da hin und zurueck
    
    distance = (TimeElapsed * 34300) / 2
    if (distance < max_distance):
        to_node("movement", "swipe_right")
 	 
    #to_node("status", "end of function")  
    return distance


   
to_node("status", "Configuring GPIOs...")
 
#GPIO Modus (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#GPIO Pins zuweisen
GPIO_TRIGGER_RIGHT = config.get("triggerRightPin") #18
GPIO_ECHO_RIGHT = config.get("echoRightPin") #24

GPIO_TRIGGER_LEFT= config.get("triggerLeftPin") #17
GPIO_ECHO_LEFT= config.get("echoLeftPin") #23
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN)
 
#Richtung der GPIO-Pins festlegen (IN / OUT)
GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN) 

max_distance = config.get("rightDistance")
 
to_node("status", "GPIOs configured...") 
 


 
 
if __name__ == '__main__':


    tsleep = config.get("intervall")

    while True:
        try:	
            measured_distance_right = distance_right()
            #to_node("status", " distance measured")
            time.sleep(tsleep)
        except KeyboardInterrupt:
            to_node("status", "Measuring stopped by user...") 
            GPIO.cleanup()
        except:
            to_node("status", "Unexpected error")
            raise
            continue
