#----------# Data Handling Module #----------#
#
#   This module handles the data, both real and simulated and
#   feeds it to the main program
#
#----------# Imports #----------#

import os
import time
import threading

#---------# RPi ONLY Imports #----------#
#import board
#import busio
#import RPi.GPIO as gpio
#import adafruit_ads1x15.ads1115 as ADS
#from adafruit_ads1x15.analog_in import AnalogIn

class Test:

    def __init__(self, parent, debugmode):

        self.parent = parent
        self.stopwatch = self.parent.stopwatch
        self.countdown = self.parent.countdown

        self.running = False

        self.getvalues()

        try:
            gpio.setmode(gpio.BCM)
        except:
            print("Error no gpio board detected")
            self.gpioError = True
        else:
            self.setupIO

        if self.gpioError and not debugmode: print("GPIO Error: Cannot start test")
        else: self.start(debugmode)

    def getvalues(self):
        self.parent.getvalues()

    def start(self, debugmode):
        if debugmode: print("Starting Debug test")
        else: print("starting Test")
        self.stopwatch.start()
        self.countdown.start()
        self.running = True
        self.test_thread = threading.Thread(target=self.RunTest(debugmode), daemon=False)

    def stop(self):
        print("Test stopped")
        self.stopwatch.stop()
        self.countdown.stop()
        self.running = False

    def RunTest(self, debugmode):
        self.reading = 0

        if debugmode:
            pass
