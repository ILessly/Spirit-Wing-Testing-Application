#----------# Parameter Storage Module #----------#
#
#   This module stores the test parameters and test status information from the GUI
#   and sensor inputs and stores them in this class for simplicity
#
#----------# Imports #----------#

class Parameters:

    def __init__(self, parent, GUI):
        self.parent = parent
        self.update(GUI)

    def update(self, GUI):

        self.cycletime = GUI.cycletime()
        self.targethi = int(GUI.Target_High_Entry.text())
        self.targetlow = int(GUI.Target_Low_Entry.text())
        self.cycletarget = int(GUI.Cycle_Target_Entry.text())
        self.samplerate = int(GUI.Sample_Rate_Entry.text())
