#GUI Module testing
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from PyQt5.uic import loadUi

def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.resize(1120, 722)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
    MainWindow.setSizePolicy(sizePolicy)
    MainWindow.setMinimumSize(QtCore.QSize(1120, 722))
    MainWindow.setMaximumSize(QtCore.QSize(1120, 722))
    MainWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    self.centralwidget = QtWidgets.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")
    self.Master_Frame = QtWidgets.QFrame(self.centralwidget)
    self.Master_Frame.setGeometry(QtCore.QRect(19, 19, 1081, 651))

#----------# Default Values and Validators #----------#
    self.cycle_time_default = "10"
    self.target_high_default = "200"
    self.target_low_default = "5"
    self.cycle_target_default = "10"
    self.sample_rate_default = "4"

    self.int_validator = QtGui.QIntValidator()
#----------# FONTS #----------#
    #Defines Calibri Font size 12
    font12 = QtGui.QFont()
    font12.setFamily("Calibri")
    font12.setPointSize(12)

    #Defines Calibri Font size 10
    font10 = QtGui.QFont()
    font10.setFamily("Calibri")
    font10.setPointSize(10)

    #Defines Calbiri Font size 20 Bold
    font20b = QtGui.QFont()
    font20b.setFamily("Calibri")
    font20b.setPointSize(20)
    font20b.setBold(True)
    font20b.setWeight(75)

    #Defines Calibri Font size 14 Bold
    font14b = QtGui.QFont()
    font14b.setFamily("Calibri")
    font14b.setPointSize(14)
    font14b.setBold(True)
    font14b.setWeight(75)

    #Defines Calibir Font size 12 italics
    font12i = QtGui.QFont()
    font12i.setFamily("Calibri")
    font12i.setPointSize(12)
    font12i.setBold(True)
    font12i.setItalic(True)
    font12i.setWeight(75)

    #Defines Calibri Font size 28 bold italic
    font28bi = QtGui.QFont()
    font28bi.setFamily("Calibri")
    font28bi.setPointSize(28)
    font28bi.setBold(True)
    font28bi.setItalic(True)
    font28bi.setWeight(75)

    #Defines Calibri Font size 20
    font20 = QtGui.QFont()
    font20.setFamily("Calibri")
    font20.setPointSize(20)

    #Defines Calibri Font 14
    font14 = QtGui.QFont()
    font14.setFamily("Calibri")
    font14.setPointSize(14)


#----------# Master Frame #----------#
    self.Master_Frame.setFont(font12)
    self.Master_Frame.setFrameShape(QtWidgets.QFrame.Box)
    self.Master_Frame.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.Master_Frame.setLineWidth(2)
    self.Master_Frame.setObjectName("Master_Frame")

#----------# Test Control Widgets #----------#
    self.Test_Controls_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Test_Controls_Box.setGeometry(QtCore.QRect(20, 490, 311, 141))
    self.Test_Controls_Box.setFont(font10)
    self.Test_Controls_Box.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    self.Test_Controls_Box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    self.Test_Controls_Box.setObjectName("Test_Controls_Box")

    self.Stop_Button = QtWidgets.QPushButton(self.Test_Controls_Box)
    self.Stop_Button.setGeometry(QtCore.QRect(190, 20, 111, 61))
    self.Stop_Button.setFont(font20b)
    self.Stop_Button.setAutoFillBackground(False)
    self.Stop_Button.setStyleSheet("background-color: rgb(255, 0, 0);")
    self.Stop_Button.setIconSize(QtCore.QSize(24, 24))
    self.Stop_Button.setCheckable(True)
    self.Stop_Button.setObjectName("Stop_Button")
    self.Stop_Button.setEnabled(False)
    self.Stop_Button.toggle()

    self.Reset_Button = QtWidgets.QPushButton(self.Test_Controls_Box)
    self.Reset_Button.setGeometry(QtCore.QRect(190, 90, 111, 41))
    self.Reset_Button.setFont(font14b)
    self.Reset_Button.setAutoFillBackground(False)
    self.Reset_Button.setStyleSheet("background-color: rgb(255, 255, 0);")
    self.Reset_Button.setIconSize(QtCore.QSize(24, 24))
    self.Reset_Button.setObjectName("Reset_Button")

    self.Start_Button = QtWidgets.QPushButton(self.Test_Controls_Box)
    self.Start_Button.setGeometry(QtCore.QRect(10, 20, 171, 61))
    self.Start_Button.setFont(font14b)
    self.Start_Button.setStyleSheet("background-color: rgb(0, 238, 0);")
    self.Start_Button.setIconSize(QtCore.QSize(24, 24))
    self.Start_Button.setCheckable(True)
    self.Start_Button.setObjectName("Start_Button")

    self.Fill_Button = QtWidgets.QPushButton(self.Test_Controls_Box)
    self.Fill_Button.setGeometry(QtCore.QRect(10, 90, 81, 41))
    self.Fill_Button.setFont(font14b)
    self.Fill_Button.setStyleSheet("background-color: rgb(0, 166, 255);")
    self.Fill_Button.setObjectName("Fill_Button")
    self.Fill_Button.setCheckable(True)

    self.Drain_Button = QtWidgets.QPushButton(self.Test_Controls_Box)
    self.Drain_Button.setGeometry(QtCore.QRect(100, 90, 81, 41))
    self.Drain_Button.setFont(font14b)
    self.Drain_Button.setStyleSheet("background-color: rgb(0, 166, 255);")
    self.Drain_Button.setObjectName("Drain_Button")
    self.Drain_Button.setCheckable(True)

#----------# Test Parameters Widgets #----------#
    self.Test_Parameters_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Test_Parameters_Box.setGeometry(QtCore.QRect(20, 240, 311, 231))
    self.Test_Parameters_Box.setObjectName("Test_Parameters_Box")
    self.gridLayoutWidget = QtWidgets.QWidget(self.Test_Parameters_Box)
    self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 271, 141))
    self.gridLayoutWidget.setObjectName("gridLayoutWidget")
    self.Test_Parameters_Layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
    self.Test_Parameters_Layout.setContentsMargins(0, 0, 0, 0)
    self.Test_Parameters_Layout.setSpacing(0)
    self.Test_Parameters_Layout.setObjectName("Test_Parameters_Layout")

    self.Target_High_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Target_High_Label.setFont(font12)
    self.Target_High_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Target_High_Label.setObjectName("Target_High_Label")
    self.Test_Parameters_Layout.addWidget(self.Target_High_Label, 1, 0, 1, 1)

    self.Cycle_Target_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.Cycle_Target_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Cycle_Target_Entry.setObjectName("Cycle_Target_Entry")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Target_Entry, 3, 1, 1, 1)

    self.Sample_Rate_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Sample_Rate_Label.setFont(font12)
    self.Sample_Rate_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Sample_Rate_Label.setObjectName("Sample_Rate_Label")
    self.Test_Parameters_Layout.addWidget(self.Sample_Rate_Label, 4, 0, 1, 1)

    self.Target_Low_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.Target_Low_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Target_Low_Entry.setObjectName("Target_Low_Entry")
    self.Test_Parameters_Layout.addWidget(self.Target_Low_Entry, 2, 1, 1, 1)

    self.Target_Low_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Target_Low_Label.setFont(font12)
    self.Target_Low_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Target_Low_Label.setObjectName("Target_Low_Label")
    self.Test_Parameters_Layout.addWidget(self.Target_Low_Label, 2, 0, 1, 1)

    self.Cycle_Target_Units_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Cycle_Target_Units_Label.setFont(font12)
    self.Cycle_Target_Units_Label.setObjectName("Cycle_Target_Units_Label")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Target_Units_Label, 3, 2, 1, 1)

    self.Sample_Rate_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.Sample_Rate_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Sample_Rate_Entry.setObjectName("Sample_Rate_Entry")
    self.Test_Parameters_Layout.addWidget(self.Sample_Rate_Entry, 4, 1, 1, 1)

    self.Target_Low_Units_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Target_Low_Units_Label.setFont(font12)
    self.Target_Low_Units_Label.setObjectName("Target_Low_Units_Label")
    self.Test_Parameters_Layout.addWidget(self.Target_Low_Units_Label, 2, 2, 1, 1)

    self.Cycle_Target_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Cycle_Target_Label.setFont(font12)
    self.Cycle_Target_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Cycle_Target_Label.setObjectName("Cycle_Target_Label")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Target_Label, 3, 0, 1, 1)

    self.Cycle_Time_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.Cycle_Time_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Cycle_Time_Entry.setObjectName("Cycle_Time_Entry")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Time_Entry, 0, 1, 1, 1)

    self.Cycle_Time_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Cycle_Time_Label.setFont(font12)
    self.Cycle_Time_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Cycle_Time_Label.setObjectName("Cycle_Time_Label")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Time_Label, 0, 0, 1, 1)

    self.Cycle_Time_Units_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Cycle_Time_Units_Label.setFont(font12)
    self.Cycle_Time_Units_Label.setObjectName("Cycle_Time_Units_Label")
    self.Test_Parameters_Layout.addWidget(self.Cycle_Time_Units_Label, 0, 2, 1, 1)

    self.Target_High_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget)
    self.Target_High_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Target_High_Entry.setObjectName("Target_High_Entry")
    self.Test_Parameters_Layout.addWidget(self.Target_High_Entry, 1, 1, 1, 1)

    self.Target_High_Units_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Target_High_Units_Label.setFont(font12)
    self.Target_High_Units_Label.setObjectName("Target_High_Units_Label")
    self.Test_Parameters_Layout.addWidget(self.Target_High_Units_Label, 1, 2, 1, 1)

    self.Sample_Rate_Units_Label = QtWidgets.QLabel(self.gridLayoutWidget)
    self.Sample_Rate_Units_Label.setFont(font12)
    self.Sample_Rate_Units_Label.setObjectName("Sample_Rate_Units_Label")
    self.Test_Parameters_Layout.addWidget(self.Sample_Rate_Units_Label, 4, 2, 1, 1)


    self.Cycle_Time_Entry.setValidator(self.int_validator)
    self.Target_High_Entry.setValidator(self.int_validator)
    self.Target_Low_Entry.setValidator(self.int_validator)
    self.Cycle_Target_Entry.setValidator(self.int_validator)
    self.Sample_Rate_Entry.setValidator(self.int_validator)

    self.Cycle_Time_Entry.setText(self.cycle_time_default)
    self.Target_High_Entry.setText(self.target_high_default)
    self.Target_Low_Entry.setText(self.target_low_default)
    self.Cycle_Target_Entry.setText(self.cycle_target_default)
    self.Sample_Rate_Entry.setText(self.sample_rate_default)

#----------# Invalid Entry Error Label #----------#
    self.Invalid_Entry_Label = QtWidgets.QLabel(self.Test_Parameters_Box)
    self.Invalid_Entry_Label.setGeometry(QtCore.QRect(130, 160, 121, 16))
    self.Invalid_Entry_Label.setFont(font12i)
    self.Invalid_Entry_Label.setStyleSheet("color: rgb(255, 0, 0);")
    self.Invalid_Entry_Label.setObjectName("Invalid_Entry_Label")
    self.Invalid_Entry_Label.setHidden(True)

#----------# Debug Mode Label #----------#
    self.Debug_Active_Label = QtWidgets.QLabel(self.Test_Parameters_Box)
    self.Debug_Active_Label.setGeometry(QtCore.QRect(50, 180, 211, 41))
    self.Debug_Active_Label.setFont(font28bi)
    self.Debug_Active_Label.setStyleSheet("color: rgb(255, 0, 0);")
    self.Debug_Active_Label.setObjectName("Debug_Active_Label")
    self.Debug_Active_Label.setHidden(True)

#----------# Current Readings Widgets #----------#
    self.Current_Reading_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Current_Reading_Box.setGeometry(QtCore.QRect(360, 490, 191, 141))
    self.Current_Reading_Box.setFont(font10)
    self.Current_Reading_Box.setObjectName("Current_Reading_Box")

    self.horizontalLayoutWidget = QtWidgets.QWidget(self.Current_Reading_Box)
    self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 101))
    self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

    self.Current_Reading_Layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
    self.Current_Reading_Layout.setContentsMargins(0, 0, 0, 0)
    self.Current_Reading_Layout.setObjectName("Current_Reading_Layout")

    self.Current_Reading_Label = QtWidgets.QLCDNumber(self.horizontalLayoutWidget)
    self.Current_Reading_Label.setLineWidth(0)
    self.Current_Reading_Label.setSmallDecimalPoint(False)
    self.Current_Reading_Label.setDigitCount(3)
    self.Current_Reading_Label.setMode(QtWidgets.QLCDNumber.Dec)
    self.Current_Reading_Label.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
    self.Current_Reading_Label.setProperty("intValue", 0)
    self.Current_Reading_Label.setObjectName("Current_Reading_Label")

    self.Current_Reading_Layout.addWidget(self.Current_Reading_Label)

    self.Current_Reading_Units = QtWidgets.QLabel(self.horizontalLayoutWidget)
    self.Current_Reading_Units.setFont(font20)
    self.Current_Reading_Units.setObjectName("Current_Reading_Units")

    self.Current_Reading_Layout.addWidget(self.Current_Reading_Units)

#----------# Live Plot Widgets #----------#
    self.Output_Graph_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Output_Graph_Box.setGeometry(QtCore.QRect(360, 20, 691, 451))
    self.Output_Graph_Box.setFont(font10)
    self.Output_Graph_Box.setObjectName("Output_Graph_Box")

    self.Live_Plot_Widget = PlotWidget(self.Output_Graph_Box)
    self.Live_Plot_Widget.setGeometry(QtCore.QRect(19, 29, 651, 411))
    self.Live_Plot_Widget.setObjectName("Live_Plot_Widget")

#----------# Directory Widgets #----------#
    self.Directory_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Directory_Box.setGeometry(QtCore.QRect(20, 20, 311, 201))
    self.Directory_Box.setFont(font10)
    self.Directory_Box.setObjectName("Directory_Box")

    self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Directory_Box)
    self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 291, 80))
    self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")

    self.Directory_Layout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
    self.Directory_Layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
    self.Directory_Layout.setContentsMargins(0, 0, 0, 0)
    self.Directory_Layout.setObjectName("Directory_Layout")

    self.Log_Name_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
    self.Log_Name_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Log_Name_Entry.setObjectName("Log_Name_Entry")

    self.Directory_Layout.addWidget(self.Log_Name_Entry, 0, 1, 1, 1)

    self.Log_Name_Label = QtWidgets.QLabel(self.gridLayoutWidget_3)
    self.Log_Name_Label.setFont(font12)
    self.Log_Name_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Log_Name_Label.setObjectName("Log_Name_Label")

    self.Directory_Layout.addWidget(self.Log_Name_Label, 0, 0, 1, 1)

    self.Location_Label = QtWidgets.QLabel(self.gridLayoutWidget_3)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Location_Label.sizePolicy().hasHeightForWidth())
    self.Location_Label.setSizePolicy(sizePolicy)
    self.Location_Label.setFont(font12)
    self.Location_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Location_Label.setObjectName("Location_Label")

    self.Directory_Layout.addWidget(self.Location_Label, 1, 0, 1, 1)

    self.Log_Location_Entry = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Log_Location_Entry.sizePolicy().hasHeightForWidth())
    self.Log_Location_Entry.setSizePolicy(sizePolicy)
    self.Log_Location_Entry.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Log_Location_Entry.setObjectName("Log_Location_Entry")

    self.Directory_Layout.addWidget(self.Log_Location_Entry, 1, 1, 1, 1)

    self.Log_Name_Ext_Label = QtWidgets.QLabel(self.gridLayoutWidget_3)
    self.Log_Name_Ext_Label.setFont(font12)
    self.Log_Name_Ext_Label.setObjectName("Log_Name_Ext_Label")

    self.Directory_Layout.addWidget(self.Log_Name_Ext_Label, 0, 2, 1, 1)

    self.Browse_Button = QtWidgets.QPushButton(self.gridLayoutWidget_3)
    self.Browse_Button.setEnabled(True)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.Browse_Button.sizePolicy().hasHeightForWidth())
    self.Browse_Button.setSizePolicy(sizePolicy)
    self.Browse_Button.setFont(font12)
    self.Browse_Button.setIconSize(QtCore.QSize(16, 16))
    self.Browse_Button.setObjectName("Browse_Button")

    self.Directory_Layout.addWidget(self.Browse_Button, 1, 2, 1, 1)

#----------# Test Status Widgets #----------#
    self.Test_Status_Box = QtWidgets.QGroupBox(self.Master_Frame)
    self.Test_Status_Box.setGeometry(QtCore.QRect(579, 489, 471, 141))
    self.Test_Status_Box.setFont(font10)
    self.Test_Status_Box.setObjectName("Test_Status_Box")

    self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Test_Status_Box)
    self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 10, 341, 122))
    self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

    self.Test_Status_Layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
    self.Test_Status_Layout.setContentsMargins(0, 0, 0, 0)
    self.Test_Status_Layout.setObjectName("Test_Status_Layout")

    self.Elapsed_Time_Count = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Elapsed_Time_Count.setFont(font14)
    self.Elapsed_Time_Count.setFrameShape(QtWidgets.QFrame.Box)
    self.Elapsed_Time_Count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Elapsed_Time_Count.setObjectName("Elapsed_Time_Count")

    self.Test_Status_Layout.addWidget(self.Elapsed_Time_Count, 1, 1, 1, 1)

    self.Current_Cycle_Count = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Current_Cycle_Count.setFont(font14)
    self.Current_Cycle_Count.setFrameShape(QtWidgets.QFrame.Box)
    self.Current_Cycle_Count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Current_Cycle_Count.setObjectName("Current_Cycle_Count")

    self.Test_Status_Layout.addWidget(self.Current_Cycle_Count, 0, 1, 1, 1)

    self.Time_Left_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Time_Left_Label.setFont(font12)
    self.Time_Left_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Time_Left_Label.setObjectName("Time_Left_Label")

    self.Test_Status_Layout.addWidget(self.Time_Left_Label, 2, 0, 1, 1)

    self.Elapsed_Time_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Elapsed_Time_Label.setFont(font12)
    self.Elapsed_Time_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Elapsed_Time_Label.setObjectName("Elapsed_Time_Label")

    self.Test_Status_Layout.addWidget(self.Elapsed_Time_Label, 1, 0, 1, 1)

    self.Time_Left_Count = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Time_Left_Count.setFont(font14)
    self.Time_Left_Count.setFrameShape(QtWidgets.QFrame.Box)
    self.Time_Left_Count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Time_Left_Count.setObjectName("Time_Left_Count")

    self.Test_Status_Layout.addWidget(self.Time_Left_Count, 2, 1, 1, 1)

    self.Current_Cycle_Label = QtWidgets.QLabel(self.gridLayoutWidget_2)
    self.Current_Cycle_Label.setFont(font12)
    self.Current_Cycle_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
    self.Current_Cycle_Label.setObjectName("Current_Cycle_Label")

    self.Test_Status_Layout.addWidget(self.Current_Cycle_Label, 0, 0, 1, 1)

    self.Test_Progress_Bar = QtWidgets.QProgressBar(self.gridLayoutWidget_2)
    self.Test_Progress_Bar.setFont(font12)
    self.Test_Progress_Bar.setProperty("value", 0)
    self.Test_Progress_Bar.setAlignment(QtCore.Qt.AlignCenter)
    self.Test_Progress_Bar.setTextVisible(True)
    self.Test_Progress_Bar.setObjectName("Test_Progress_Bar")

    self.Test_Status_Layout.addWidget(self.Test_Progress_Bar, 3, 0, 1, 2)

#----------# Menu Bar Widgets #----------#
    MainWindow.setCentralWidget(self.centralwidget)
    self.Menu_Bar = QtWidgets.QMenuBar(MainWindow)
    self.Menu_Bar.setGeometry(QtCore.QRect(0, 0, 1120, 21))
    self.Menu_Bar.setObjectName("Menu_Bar")
    self.File_Menu = QtWidgets.QMenu(self.Menu_Bar)
    self.File_Menu.setObjectName("File_Menu")
    self.View_Menu = QtWidgets.QMenu(self.Menu_Bar)
    self.View_Menu.setObjectName("View_Menu")
    self.About_Menu = QtWidgets.QMenu(self.Menu_Bar)
    self.About_Menu.setObjectName("About_Menu")
    MainWindow.setMenuBar(self.Menu_Bar)
    self.statusbar = QtWidgets.QStatusBar(MainWindow)
    self.statusbar.setObjectName("statusbar")
    MainWindow.setStatusBar(self.statusbar)
    self.Open_Log = QtWidgets.QAction(MainWindow)
    self.Open_Log.setObjectName("Open_Log")
    self.Open_Details_Window = QtWidgets.QAction(MainWindow)
    self.Open_Details_Window.setObjectName("Open_Details_Window")
    self.Open_Plot_Settings_Window = QtWidgets.QAction(MainWindow)
    self.Open_Plot_Settings_Window.setObjectName("Open_Plot_Settings_Window")
    self.Open_Debug_Window = QtWidgets.QAction(MainWindow)
    self.Open_Debug_Window.setObjectName("Open_Debug_Window")
    self.New = QtWidgets.QAction(MainWindow)
    self.New.setObjectName("New")
    self.Save = QtWidgets.QAction(MainWindow)
    self.Save.setObjectName("Save")
    self.Exit = QtWidgets.QAction(MainWindow)
    self.Exit.setObjectName("Exit")
    self.Open_About_Window = QtWidgets.QAction(MainWindow)
    self.Open_About_Window.setObjectName("Open_About_Window")
    self.Open_Help_Window = QtWidgets.QAction(MainWindow)
    self.Open_Help_Window.setObjectName("Open_Help_Window")
    self.File_Menu.addAction(self.New)
    self.File_Menu.addAction(self.Save)
    self.File_Menu.addSeparator()
    self.File_Menu.addAction(self.Exit)
    self.View_Menu.addAction(self.Open_Log)
    self.View_Menu.addAction(self.Open_Details_Window)
    self.View_Menu.addSeparator()
    self.View_Menu.addAction(self.Open_Plot_Settings_Window)
    self.View_Menu.addSeparator()
    self.View_Menu.addAction(self.Open_Debug_Window)
    self.About_Menu.addAction(self.Open_About_Window)
    self.About_Menu.addAction(self.Open_Help_Window)
    self.Menu_Bar.addAction(self.File_Menu.menuAction())
    self.Menu_Bar.addAction(self.View_Menu.menuAction())
    self.Menu_Bar.addAction(self.About_Menu.menuAction())
    self.Target_High_Label.setBuddy(self.Target_High_Entry)
    self.Sample_Rate_Label.setBuddy(self.Sample_Rate_Entry)
    self.Target_Low_Label.setBuddy(self.Target_Low_Entry)
    self.Cycle_Target_Label.setBuddy(self.Cycle_Target_Entry)
    self.Cycle_Time_Label.setBuddy(self.Cycle_Time_Entry)
    self.Log_Name_Label.setBuddy(self.Log_Name_Entry)
    self.Location_Label.setBuddy(self.Log_Location_Entry)

    self.retranslateUi(MainWindow)
    self.Exit.triggered['bool'].connect(MainWindow.close)
    QtCore.QMetaObject.connectSlotsByName(MainWindow)
    MainWindow.setTabOrder(self.Log_Name_Entry, self.Log_Location_Entry)
    MainWindow.setTabOrder(self.Log_Location_Entry, self.Browse_Button)
    MainWindow.setTabOrder(self.Browse_Button, self.Cycle_Time_Entry)
    MainWindow.setTabOrder(self.Cycle_Time_Entry, self.Target_High_Entry)
    MainWindow.setTabOrder(self.Target_High_Entry, self.Target_Low_Entry)
    MainWindow.setTabOrder(self.Target_Low_Entry, self.Cycle_Target_Entry)
    MainWindow.setTabOrder(self.Cycle_Target_Entry, self.Sample_Rate_Entry)
    MainWindow.setTabOrder(self.Sample_Rate_Entry, self.Start_Button)
    MainWindow.setTabOrder(self.Start_Button, self.Stop_Button)
    MainWindow.setTabOrder(self.Stop_Button, self.Fill_Button)
    MainWindow.setTabOrder(self.Fill_Button, self.Drain_Button)

def retranslateUi(self, MainWindow):
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    self.Test_Controls_Box.setTitle(_translate("MainWindow", "Test Controls"))
    self.Stop_Button.setText(_translate("MainWindow", "Stop"))
    self.Reset_Button.setText(_translate("MainWindow", "Reset"))
    self.Start_Button.setText(_translate("MainWindow", "Begin Test"))
    self.Fill_Button.setText(_translate("MainWindow", "Fill"))
    self.Drain_Button.setText(_translate("MainWindow", "Drain"))
    self.Test_Parameters_Box.setTitle(_translate("MainWindow", "Test Parameters"))
    self.Target_High_Label.setText(_translate("MainWindow", "High Setpoint: "))
    self.Sample_Rate_Label.setText(_translate("MainWindow", "Sample Rate: "))
    self.Target_Low_Label.setText(_translate("MainWindow", "Low Setpoint: "))
    self.Cycle_Target_Units_Label.setText(_translate("MainWindow", " cycles"))
    self.Target_Low_Units_Label.setText(_translate("MainWindow", " psig"))
    self.Cycle_Target_Label.setText(_translate("MainWindow", "Cycle Target: "))
    self.Cycle_Time_Label.setText(_translate("MainWindow", "Est. Cycle Time: "))
    self.Cycle_Time_Units_Label.setText(_translate("MainWindow", " sec"))
    self.Target_High_Units_Label.setText(_translate("MainWindow", " psig"))
    self.Sample_Rate_Units_Label.setText(_translate("MainWindow", " hz"))
    self.Invalid_Entry_Label.setText(_translate("MainWindow", "**Invalid Entry**"))
    self.Debug_Active_Label.setText(_translate("MainWindow", "Debug Mode"))
    self.Current_Reading_Box.setTitle(_translate("MainWindow", "Current Reading"))
    self.Current_Reading_Units.setText(_translate("MainWindow", "PSI"))
    self.Output_Graph_Box.setTitle(_translate("MainWindow", "Output Graph"))
    self.Directory_Box.setTitle(_translate("MainWindow", "Directory"))
    self.Log_Name_Label.setText(_translate("MainWindow", "Log &Name: "))
    self.Location_Label.setText(_translate("MainWindow", "&Location: "))
    self.Log_Name_Ext_Label.setText(_translate("MainWindow", ".txt"))
    self.Browse_Button.setText(_translate("MainWindow", "..."))
    self.Test_Status_Box.setTitle(_translate("MainWindow", "Test Status"))
    self.Elapsed_Time_Count.setText(_translate("MainWindow", "0"))
    self.Current_Cycle_Count.setText(_translate("MainWindow", "0"))
    self.Time_Left_Label.setText(_translate("MainWindow", "Est. Time Left: "))
    self.Elapsed_Time_Label.setText(_translate("MainWindow", "Elapsed Time: "))
    self.Time_Left_Count.setText(_translate("MainWindow", "0h 0m 0s"))
    self.Current_Cycle_Label.setText(_translate("MainWindow", "Cycle: "))
    self.File_Menu.setTitle(_translate("MainWindow", "File"))
    self.View_Menu.setTitle(_translate("MainWindow", "View"))
    self.About_Menu.setTitle(_translate("MainWindow", "About"))
    self.Open_Log.setText(_translate("MainWindow", "Log"))
    self.Open_Details_Window.setText(_translate("MainWindow", "Details"))
    self.Open_Plot_Settings_Window.setText(_translate("MainWindow", "Plot Settings"))
    self.Open_Debug_Window.setText(_translate("MainWindow", "Debug"))
    self.New.setText(_translate("MainWindow", "New"))
    self.Save.setText(_translate("MainWindow", "Save"))
    self.Exit.setText(_translate("MainWindow", "Exit"))
    self.Open_About_Window.setText(_translate("MainWindow", "About"))
    self.Open_Help_Window.setText(_translate("MainWindow", "Help"))

def getvalue(self, name):
    if name == "cycletime":
        return int(self.Cycle_Time_Entry.text())
    elif name == "targethi":
        return int(self.Target_High_Entry.text())
    elif name == "targetlow":
        return int(self.Target_Low_Entry.text())
    elif name == "cycletarget":
        return int(self.Cycle_Target_Entry.text())
    elif name == "samplerate":
        return int(self.Sample_Rate_Entry.text())
    else:
        print("Error, no such value:", name)

def setvalue(self, name, value):
    pass
