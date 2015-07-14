'''
UI portion of the profilometer program.
The visual aspect of this code was generated by running pyuic4 on the .ui file created by QT Designer.
The functionality was added after the code was generated.
'''

# Imports
import sys
import threading
from PyQt4 import QtCore, QtGui
import profilometerParameters
import profilometerSystemController

# Code from the automatic generation from the UI file
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# Primary UI class that inherits the QWidget class
class Ui_formProfilometer(QtGui.QWidget):
    def __init__(self):
        # Initializes the QWidget superclass
        QtGui.QWidget.__init__(self)
        # Runs setupIU method upon initialization
        self.setupUi(self)
        self.initializeEquipment()

    # Code specifying what the UI looks like, creation and location of all UI elements (generated code)
    def setupUi(self, formProfilometer):
        formProfilometer.setObjectName(_fromUtf8("formProfilometer"))
        formProfilometer.resize(655, 396)
        formProfilometer.move(30,30)
        self.buttonOrigin = QtGui.QPushButton(formProfilometer)
        self.buttonOrigin.setGeometry(QtCore.QRect(30, 350, 81, 41))
        self.buttonOrigin.setObjectName(_fromUtf8("buttonOrigin"))
        self.buttonStartStop = QtGui.QPushButton(formProfilometer)
        self.buttonStartStop.setGeometry(QtCore.QRect(40, 150, 110, 61))
        self.buttonStartStop.setObjectName(_fromUtf8("buttonStartStop"))
        self.frameProfileDisplay = QtGui.QFrame(formProfilometer)
        self.frameProfileDisplay.setGeometry(QtCore.QRect(210, 10, 431, 331))
        self.frameProfileDisplay.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameProfileDisplay.setFrameShadow(QtGui.QFrame.Raised)
        self.frameProfileDisplay.setObjectName(_fromUtf8("frameProfileDisplay"))
        self.lineProfilometerControlsSubstrteControls = QtGui.QFrame(formProfilometer)
        self.lineProfilometerControlsSubstrteControls.setGeometry(QtCore.QRect(10, 210, 191, 16))
        self.lineProfilometerControlsSubstrteControls.setFrameShape(QtGui.QFrame.HLine)
        self.lineProfilometerControlsSubstrteControls.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineProfilometerControlsSubstrteControls.setObjectName(_fromUtf8("lineProfilometerControlsSubstrteControls"))
        self.labelSubstrateControls = QtGui.QLabel(formProfilometer)
        self.labelSubstrateControls.setGeometry(QtCore.QRect(40, 230, 111, 16))
        self.labelSubstrateControls.setObjectName(_fromUtf8("labelSubstrateControls"))
        self.groupBoxTravelDirection = QtGui.QGroupBox(formProfilometer)
        self.groupBoxTravelDirection.setGeometry(QtCore.QRect(30, 90, 131, 51))
        self.groupBoxTravelDirection.setObjectName(_fromUtf8("groupBoxTravelDirection"))
        self.layoutWidget = QtGui.QWidget(self.groupBoxTravelDirection)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 131, 18))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.layoutTravelDirection = QtGui.QHBoxLayout(self.layoutWidget)
        self.layoutTravelDirection.setMargin(0)
        self.layoutTravelDirection.setObjectName(_fromUtf8("layoutTravelDirection"))
        self.radioButtonX = QtGui.QRadioButton(self.layoutWidget)
        self.radioButtonX.setChecked(True)
        self.radioButtonX.setObjectName(_fromUtf8("radioButtonX"))
        self.layoutTravelDirection.addWidget(self.radioButtonX)
        self.radioButtonY = QtGui.QRadioButton(self.layoutWidget)
        self.radioButtonY.setChecked(False)
        self.radioButtonY.setObjectName(_fromUtf8("radioButtonY"))
        self.layoutTravelDirection.addWidget(self.radioButtonY)
        self.buttonCalibrate = QtGui.QPushButton(formProfilometer)
        self.buttonCalibrate.setGeometry(QtCore.QRect(100, 350, 81, 41))
        self.buttonCalibrate.setObjectName(_fromUtf8("buttonCalibrate"))
        self.layoutWidget1 = QtGui.QWidget(formProfilometer)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 350, 431, 33))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.layoutSave = QtGui.QGridLayout(self.layoutWidget1)
        self.layoutSave.setMargin(0)
        self.layoutSave.setObjectName(_fromUtf8("layoutSave"))
        self.labelFileName = QtGui.QLabel(self.layoutWidget1)
        self.labelFileName.setObjectName(_fromUtf8("labelFileName"))
        self.layoutSave.addWidget(self.labelFileName, 0, 0, 1, 1)
        self.entryBoxFileName = QtGui.QLineEdit(self.layoutWidget1)
        self.entryBoxFileName.setObjectName(_fromUtf8("entryBoxFileName"))
        self.layoutSave.addWidget(self.entryBoxFileName, 0, 1, 1, 1)
        self.buttonSave = QtGui.QPushButton(self.layoutWidget1)
        self.buttonSave.setObjectName(_fromUtf8("buttonSave"))
        self.layoutSave.addWidget(self.buttonSave, 0, 2, 1, 1)
        self.layoutWidget2 = QtGui.QWidget(formProfilometer)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 181, 77))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.layoutProfilometerControls = QtGui.QVBoxLayout(self.layoutWidget2)
        self.layoutProfilometerControls.setMargin(0)
        self.layoutProfilometerControls.setObjectName(_fromUtf8("layoutProfilometerControls"))
        self.labelProfilometerControls = QtGui.QLabel(self.layoutWidget2)
        self.labelProfilometerControls.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProfilometerControls.setObjectName(_fromUtf8("labelProfilometerControls"))
        self.layoutProfilometerControls.addWidget(self.labelProfilometerControls)
        self.layoutProfilometerSettings = QtGui.QGridLayout()
        self.layoutProfilometerSettings.setObjectName(_fromUtf8("layoutProfilometerSettings"))
        self.labelTravelDistance = QtGui.QLabel(self.layoutWidget2)
        self.labelTravelDistance.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelTravelDistance.setObjectName(_fromUtf8("labelTravelDistance"))
        self.layoutProfilometerSettings.addWidget(self.labelTravelDistance, 0, 0, 1, 1)
        self.labelStepSize = QtGui.QLabel(self.layoutWidget2)
        self.labelStepSize.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStepSize.setObjectName(_fromUtf8("labelStepSize"))
        self.layoutProfilometerSettings.addWidget(self.labelStepSize, 1, 0, 1, 1)
        self.entryBoxStepSize = QtGui.QLineEdit(self.layoutWidget2)
        self.entryBoxStepSize.setObjectName(_fromUtf8("entryBoxStepSize"))
        self.layoutProfilometerSettings.addWidget(self.entryBoxStepSize, 1, 1, 1, 1)
        self.entryBoxTravelDistance = QtGui.QLineEdit(self.layoutWidget2)
        self.entryBoxTravelDistance.setObjectName(_fromUtf8("entryBoxTravelDistance"))
        self.layoutProfilometerSettings.addWidget(self.entryBoxTravelDistance, 0, 1, 1, 1)
        self.layoutProfilometerControls.addLayout(self.layoutProfilometerSettings)
        self.layoutWidget3 = QtGui.QWidget(formProfilometer)
        self.layoutWidget3.setGeometry(QtCore.QRect(30, 280, 151, 66))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.layoutButtonsMovementDirections = QtGui.QGridLayout(self.layoutWidget3)
        self.layoutButtonsMovementDirections.setMargin(0)
        self.layoutButtonsMovementDirections.setObjectName(_fromUtf8("layoutButtonsMovementDirections"))
        self.buttonXPositive = QtGui.QPushButton(self.layoutWidget3)
        self.buttonXPositive.setObjectName(_fromUtf8("buttonXPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonXPositive, 0, 0, 1, 1)
        self.buttonYPositive = QtGui.QPushButton(self.layoutWidget3)
        self.buttonYPositive.setObjectName(_fromUtf8("buttonYPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonYPositive, 0, 1, 1, 1)
        self.buttonZPositive = QtGui.QPushButton(self.layoutWidget3)
        self.buttonZPositive.setObjectName(_fromUtf8("buttonZPositive"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonZPositive, 0, 2, 1, 1)
        self.buttonXNegative = QtGui.QPushButton(self.layoutWidget3)
        self.buttonXNegative.setObjectName(_fromUtf8("buttonXNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonXNegative, 1, 0, 1, 1)
        self.buttonYNegative = QtGui.QPushButton(self.layoutWidget3)
        self.buttonYNegative.setObjectName(_fromUtf8("buttonYNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonYNegative, 1, 1, 1, 1)
        self.buttonZNegative = QtGui.QPushButton(self.layoutWidget3)
        self.buttonZNegative.setObjectName(_fromUtf8("buttonZNegative"))
        self.layoutButtonsMovementDirections.addWidget(self.buttonZNegative, 1, 2, 1, 1)
        self.layoutWidget4 = QtGui.QWidget(formProfilometer)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 250, 191, 23))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.layoutMovemetDistance = QtGui.QHBoxLayout(self.layoutWidget4)
        self.layoutMovemetDistance.setMargin(0)
        self.layoutMovemetDistance.setObjectName(_fromUtf8("layoutMovemetDistance"))
        self.labelMovementDistance = QtGui.QLabel(self.layoutWidget4)
        self.labelMovementDistance.setObjectName(_fromUtf8("labelMovementDistance"))
        self.layoutMovemetDistance.addWidget(self.labelMovementDistance)
        self.entryBoxMovementDistance = QtGui.QLineEdit(self.layoutWidget4)
        self.entryBoxMovementDistance.setObjectName(_fromUtf8("entryBoxMovementDistance"))
        self.layoutMovemetDistance.addWidget(self.entryBoxMovementDistance)

        self.retranslateUi(formProfilometer)
        QtCore.QMetaObject.connectSlotsByName(formProfilometer)
        formProfilometer.setTabOrder(self.entryBoxTravelDistance, self.entryBoxStepSize)
        formProfilometer.setTabOrder(self.entryBoxStepSize, self.radioButtonX)
        formProfilometer.setTabOrder(self.radioButtonX, self.radioButtonY)
        formProfilometer.setTabOrder(self.radioButtonY, self.buttonStartStop)
        formProfilometer.setTabOrder(self.buttonStartStop, self.entryBoxMovementDistance)
        formProfilometer.setTabOrder(self.entryBoxMovementDistance, self.buttonXPositive)
        formProfilometer.setTabOrder(self.buttonXPositive, self.buttonYPositive)
        formProfilometer.setTabOrder(self.buttonYPositive, self.buttonZPositive)
        formProfilometer.setTabOrder(self.buttonZPositive, self.buttonXNegative)
        formProfilometer.setTabOrder(self.buttonXNegative, self.buttonYNegative)
        formProfilometer.setTabOrder(self.buttonYNegative, self.buttonZNegative)
        formProfilometer.setTabOrder(self.buttonZNegative, self.buttonOrigin)
        formProfilometer.setTabOrder(self.buttonOrigin, self.buttonCalibrate)
        formProfilometer.setTabOrder(self.buttonCalibrate, self.entryBoxFileName)
        formProfilometer.setTabOrder(self.entryBoxFileName, self.buttonSave)

    # Code specifying what the display text of the elements and what to do when they are interacted with (generated)
    def retranslateUi(self, formProfilometer):
        formProfilometer.setWindowTitle(_translate("formProfilometer", "Profilometer", None))
        self.buttonOrigin.setText(_translate("formProfilometer", "Origin", None))
        self.buttonStartStop.setText(_translate("formProfilometer", "Start/Stop", None))
        self.labelSubstrateControls.setText(_translate("formProfilometer", "Substrate Controls", None))
        self.groupBoxTravelDirection.setTitle(_translate("formProfilometer", "Travel Direction:", None))
        self.radioButtonX.setText(_translate("formProfilometer", "X", None))
        self.radioButtonY.setText(_translate("formProfilometer", "Y", None))
        self.buttonCalibrate.setText(_translate("formProfilometer", "Calibrate", None))
        self.labelFileName.setText(_translate("formProfilometer", "File Name:", None))
        self.buttonSave.setText(_translate("formProfilometer", "Save", None))
        self.labelProfilometerControls.setText(_translate("formProfilometer", "Profilometer Controls", None))
        self.labelTravelDistance.setText(_translate("formProfilometer", "Travel Distance(mm):", None))
        self.labelStepSize.setText(_translate("formProfilometer", "Step Size(um):", None))
        self.entryBoxStepSize.setText(_translate("formProfilometer", "500", None))
        self.entryBoxTravelDistance.setText(_translate("formProfilometer", "2", None))
        self.buttonXPositive.setText(_translate("formProfilometer", "+ X", None))
        self.buttonYPositive.setText(_translate("formProfilometer", "+ Y", None))
        self.buttonZPositive.setText(_translate("formProfilometer", "+ Z", None))
        self.buttonXNegative.setText(_translate("formProfilometer", "- X", None))
        self.buttonYNegative.setText(_translate("formProfilometer", "- Y", None))
        self.buttonZNegative.setText(_translate("formProfilometer", "- Z", None))
        self.labelMovementDistance.setText(_translate("formProfilometer", "Movement Distance(mm):", None))
        self.entryBoxMovementDistance.setText(_translate("formProfilometer", "0", None))


        # Button clicked commands added after generation, these direct the program to the correct method upon each button click
        self.buttonStartStop.clicked.connect(self.buttonClickedStartStop)
        self.buttonSave.clicked.connect(self.buttonClickedSave)
        self.buttonOrigin.clicked.connect(self.buttonClickedOrigin)
        self.buttonCalibrate.clicked.connect(self.buttonClickedCalibrate)
        # Manual stage movement clicked commands
        self.buttonXPositive.clicked.connect(lambda: self.buttonClickedManualMove('+X',self.entryBoxMovementDistance.text()))
        self.buttonXNegative.clicked.connect(lambda: self.buttonClickedManualMove('-X',self.entryBoxMovementDistance.text()))
        self.buttonYPositive.clicked.connect(lambda: self.buttonClickedManualMove('+Y',self.entryBoxMovementDistance.text()))
        self.buttonYNegative.clicked.connect(lambda: self.buttonClickedManualMove('-Y',self.entryBoxMovementDistance.text()))
        self.buttonZPositive.clicked.connect(lambda: self.buttonClickedManualMove('+Z',self.entryBoxMovementDistance.text()))
        self.buttonZNegative.clicked.connect(lambda: self.buttonClickedManualMove('-Z',self.entryBoxMovementDistance.text()))

    # Method for clicking the start/stop button
    def buttonClickedStartStop(self):

        # If statement that cycles through the start/stop functionality of the button
        # First if statement that checks for routine running = True
        if profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning) == True:
            # Update the profilometer routine running to False when start/stop button clicked
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)
            self.updateMovementButtonsState(True)
            # Updates the start/stop button to green and start
            self.buttonStartStop.setText('Start')
            self.buttonStartStop.setStyleSheet('background-color: green')
            print('Profilometer Routine Stopped')

        # Else if statement that checks for routine running = False
        elif profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning) == False:
            # Updates the profilometer routine running to True when start/stop button clicked
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,True)
            # Updates the profilometer start flag to True when start/stop button clicked
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,True)
            # Updates the profilometer routine direction based on the radio button selected
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection,self.retrieveProfilometerRoutineDirection())
            # Updates the profilometer routine step size based on the value entered into the entry box
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize,self.entryBoxStepSize.text())
            # Updates the profilometer routine travel distance based on the value entered into the entry box
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance,self.entryBoxTravelDistance.text())
            self.updateMovementButtonsState(False)
            # Updates the start/stop button to red and stop
            self.buttonStartStop.setText('STOP')
            self.buttonStartStop.setStyleSheet('background-color: red')
            print('Profilometer Routine Started')

    # Method for clicking the save button.
    # This saves the profilomter data to the file name specified.
    def buttonClickedSave(self):
        print('Save Clicked')

    # Method for clicking the origin button.
    # This takes the profilometer to the origin.
    def buttonClickedOrigin(self):
        print('Origin Clicked')

    # Method for clicking the calibrate button.
    # This allows us to determine if the profilomter is reading correctly.
    def buttonClickedCalibrate(self):
        print('Calibrate Clicked')
        # self.systemController.initializeData()
        # self.systemControllerThread.systemController.initializeData()

    # Method for clicking the manual movement buttons.
    # Moves the stage in the specified direction direction by specified amount.
    def buttonClickedManualMove(self,_stageMovementManualDirection,_stageMovementManualDistance):
        print('Manual Move Clicked')
        self.systemController.moveTheStage(_stageMovementManualDirection,_stageMovementManualDistance)

    # Method for determining which direction to run the profilometer routine
    def retrieveProfilometerRoutineDirection(self):
        # If statements that checks which direction radio button is selected.
        if self.radioButtonX.isChecked():
            print('X Direction')
            return 'X'
        elif self.radioButtonY.isChecked():
            print('Y Direction')
            return 'Y'

    # Method for initializing the equipment.
    # Initializes the equipment.
    def initializeEquipment(self):
        print('initializeEquipment accessed')
        # Changes the start/stop button to a green start button
        self.buttonStartStop.setText('Start')
        self.buttonStartStop.setStyleSheet('background-color: green')

        # Creates and starts the systemController on a daemon thread
        self.systemController = profilometerSystemController.systemController()
        self.systemControllerThread = threading.Thread(target=self.systemController.run,args=())
        # Makes the thread a daemon thread so thread exits when main thread exits
        self.systemControllerThread.daemon = True
        self.systemControllerThread.start()

    # Method for changing the clickability of the manual movement and save buttons
    def updateMovementButtonsState(self,_condition):
        # Changes clickability of all buttons except start/stop
        self.buttonOrigin.setEnabled(_condition)
        self.buttonCalibrate.setEnabled(_condition)
        self.buttonXPositive.setEnabled(_condition)
        self.buttonXNegative.setEnabled(_condition)
        self.buttonYPositive.setEnabled(_condition)
        self.buttonYNegative.setEnabled(_condition)
        self.buttonZPositive.setEnabled(_condition)
        self.buttonZNegative.setEnabled(_condition)
        self.buttonSave.setEnabled(_condition)
        # Changes clickability of radio buttons
        self.radioButtonY.setEnabled(_condition)
        self.radioButtonX.setEnabled(_condition)
        # Changes clickability of all entry boxes
        self.entryBoxTravelDistance.setEnabled(_condition)
        self.entryBoxStepSize.setEnabled(_condition)
        self.entryBoxMovementDistance.setEnabled(_condition)
        self.entryBoxFileName.setEnabled(_condition)

def profilometerUIMain():
    # Creates the GUI application
    app = QtGui.QApplication(sys.argv)
    # Creates the class instance defining what to display
    ex = Ui_formProfilometer()
    # Shows the class instance
    ex.show()
    # Exits the program when the GUI application is exited
    sys.exit(app.exec_())

if __name__ == '__main__':
    profilometerUIMain()