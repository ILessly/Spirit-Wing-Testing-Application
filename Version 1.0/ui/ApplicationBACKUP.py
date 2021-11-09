#---------# Main Application File #---------#

import DebugWindow as debug
import MainWindow as main
import os, sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import TimekeepingModule as tkm
import DataModule as dm

class Application:

    def __init__(self):

        self.printing = False #Turns printing on or off for the application

        #----------- Creating Variables -----------#
        self.debugmode = False
        self.currentreading = 0

        app = QtWidgets.QApplication(sys.argv)
        self.GUI = main.Window()
        self.debug = debug.DebugWindow()
        self.getvalues()
        #self.stopwatch = tkm.Stopwatch(self.GUI.Elapsed_Time_Count)
        self.stopwatch = tkm.Stopwatch()
        self.countdown = tkm.Countdown(self.cycletarget, self.cycletime, self.GUI.Time_Left_Count)


        self.connectfunctions()
        self.getvalues()

        self.GUI.show()
        sys.exit(app.exec_())

    def getvalues(self):

        self.cycletime = self.GUI.getvalue("cycletime")
        self.targethi = self.GUI.getvalue("targethi")
        self.targetlow = self.GUI.getvalue("targetlow")
        self.cycletarget = self.GUI.getvalue("cycletarget")
        self.samplerate = self.GUI.getvalue("samplerate")

    def connectfunctions(self):

        self.GUI.Start_Button.clicked.connect(self.start)
        self.GUI.Stop_Button.clicked.connect(self.stop)
        self.GUI.Reset_Button.clicked.connect(self.reset)
        self.GUI.Cycle_Time_Entry.editingFinished.connect(self.checkvalues)
        self.GUI.Target_High_Entry.editingFinished.connect(self.checkvalues)
        self.GUI.Target_Low_Entry.editingFinished.connect(self.checkvalues)
        self.GUI.Cycle_Target_Entry.editingFinished.connect(self.checkvalues)
        self.GUI.Sample_Rate_Entry.editingFinished.connect(self.checkvalues)
        self.GUI.Open_Debug_Window.triggered.connect(self.open_debug)
        self.GUI.destroyed.connect(self.debug.close)
        self.debug.Debug_Toggle_Box.stateChanged.connect(lambda: self.toggledebugmode(self.debug.Debug_Toggle_Box.isChecked()))
        self.debug.Slider_Toggle_Box.stateChanged.connect(lambda: self.toggledebugslider(self.debug.Slider_Toggle_Box.isChecked()))

    def open_debug(self):

        self.debug.show()

    def toggledebugmode(self, debugmode):

        self.debugmode = debugmode
        self.GUI.Debug_Active_Label.setHidden(not debugmode)
        self.debug.Slider_Toggle_Box.setChecked(False)

    def toggledebugslider(self, state):

        slidermode = state
        reading = self.GUI.Current_Reading_Label
        slider = self.debug.horizontalSlider
        data = self.currentreading

        if slidermode:
            reading.display(slider.value())
            slider.valueChanged.connect(reading.display)
            #self.GUI.Live_Plot_Widget.addItem(slider.value())

        else:
            reading.display(data)

    def checkvalues(self):

        self.getvalues()
        if ([self.cycletime, self.targethi, self.targetlow, self.cycletarget, self.samplerate] > [0]) and (self.targethi > self.targetlow) :
            if self.printing: print("Valid Entry")
            self.GUI.Invalid_Entry_Label.setHidden(True)
            self.GUI.Start_Button.setEnabled(True)
            self.countdown.reset(self.GUI.Cycle_Target_Entry.text(), self.GUI.Cycle_Time_Entry.text())

        else:
            if self.printing: print("Invalid Entry")
            self.GUI.Invalid_Entry_Label.setHidden(False)
            self.GUI.Start_Button.setEnabled(False)

        if self.printing: print(self.cycletime, self.targethi, self.targetlow, self.cycletarget, self.samplerate)

    def start(self):

        self.getvalues()
        self.test = dm.Test(self, self.debugmode)
        self.togglecontrols(self.test.running)

    def stop(self):

        self.test.stop()
        self.togglecontrols(self.test.running)

    def reset(self):

        self.stopwatch.reset()
        self.countdown.reset(self.GUI.Cycle_Target_Entry.text(), self.GUI.Cycle_Time_Entry.text())

    def togglecontrols(self, state):

        self.GUI.Start_Button.setEnabled(not state)
        self.GUI.Stop_Button.setEnabled(state)
        self.GUI.Reset_Button.setEnabled(not state)
        self.GUI.Stop_Button.toggle() if state else self.GUI.Start_Button.toggle()
        self.GUI.Cycle_Time_Entry.setEnabled(not state)
        self.GUI.Target_High_Entry.setEnabled(not state)
        self.GUI.Target_Low_Entry.setEnabled(not state)
        self.GUI.Cycle_Target_Entry.setEnabled(not state)
        self.GUI.Sample_Rate_Entry.setEnabled(not state)
        self.debug.Debug_Toggle_Box.setEnabled(not state)
        self.debug.Slider_Toggle_Box.setEnabled(not state)
        self.debug.horizontalSlider.setEnabled(not state)

#-------------------------------------#
a = Application()
