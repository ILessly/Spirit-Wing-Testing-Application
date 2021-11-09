#----------# Timekeeping Module #----------#
#
#   This module defines the stopwatch and countdown timer classes
#
#----------# Imports #----------#

import os
import sys
import time
import threading

class Stopwatch:

    def __init__(self, rtoutput):

        self.printing = False

        self.rtoutput = rtoutput
        self.running = False
        self.reset()

        self.runtime = "{hrs}h {mins}m {secs}s".format(hrs=self.rh, mins=self.rm, secs=self.rs)
        self.rtoutput.setText(self.runtime)

    def reset(self):

        self.r_master = 0 #Running master
        self.rs = 0 #Running seconds
        self.rm = 0 #Running minutes
        self.rh = 0 #Running hours

        self.runtime = "{hrs}h {mins}m {secs}s".format(hrs=self.rh, mins=self.rm, secs=self.rs)
        self.rtoutput.setText(self.runtime)

    def start(self):

        self.stopwatch_thread = threading.Thread(target=self.timer, daemon=False)
        self.running = True
        self.stopwatch_thread.start()


    def stop(self):

        self.running = False

    def timer(self):

        time.sleep(1)

        while self.running:

            self.r_master += 1
            self.rs += 1

            if self.rs==60:
                self.rm += 1
                self.rs = 0

            if self.rm==60:
                self.rh += 1
                self.rm = 0

            self.runtime = "{hrs}h {mins}m {secs}s".format(hrs=self.rh, mins=self.rm, secs=self.rs)
            self.rtoutput.setText(self.runtime)
            if self.printing: print(self.runtime)
            time.sleep(1)

            # if __name__ == "__main__":
            #      print(self.runtime)

class Countdown:

    def __init__(self, cycletarget, cycletime, output):

        self.output = output
        self.running = False

        self.reset(cycletarget, cycletime)

    def reset(self, cycletarget, cycletime):

        self.ctarget = int(cycletarget)
        self.ctime = int(cycletime)

        self.ert = self.ctarget * self.ctime #ert is estimated time remaining (in seconds)
        self.tlh = self.ert // 3600
        self.tlm = (self.ert - (self.tlh*3600)) // 60
        self.tls = self.ert % 60

        self.timeleft = "{hrs}h {mins}m {secs}s".format(hrs=self.tlh, mins=self.tlm, secs=self.tls)
        self.output.setText(self.timeleft)

    def start(self):

        self.countdown_thread = threading.Thread(target=self.timer, daemon=False)
        self.running = True
        self.countdown_thread.start()

    def stop(self):

        self.running = False

    def timer(self):

        time.sleep(1)

        while self.running:

            self.tls += -1

            if self.tls==-1:
                self.tlm += -1
                self.tls = 59

            if self.tlm==-1:
                self.tlh += -1
                self.tlm = 59

            if self.tlh==-1:
                self.tlh = 0
                self.tlm = 0
                self.tls = 0
                self.stop(False)

            self.timeleft = "{hrs}h {mins}m {secs}s".format(hrs=self.tlh, mins=self.tlm, secs=self.tls)
            self.output.setText(self.timeleft)
            time.sleep(1)


if __name__ == "__main__":
    sw_test = Stopwatch()
    sw_test.start()
    while sw_test.running:
#        print(sw_test.runtime)
        if sw_test.r_master == 15:
            sw_test.stop()
