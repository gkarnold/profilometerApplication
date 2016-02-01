'''
UI portion of the profilometer program.
The visual aspect of this code was generated by running pyuic4 on the .ui file created by QT Designer.
The functionality was added after the code was generated.
'''

## Imports
# Built in modules
import sys # Gives access to system comands
import threading # Threading functionality
import csv # Allows for the saving of CSV files
import os # OS commands
import datetime # Date and time access for saving data
from PyQt4 import QtCore, QtGui # GUI functionality
import pyqtgraph as pg # PyQt graphing module
# Custom modules
import profilometerParameters # Global parameters for comunicating between the UI and the system controller thread
import profilometerSystemController # System controller that will be created and started on a new thread
import profilometerUIConvert # Base UI that is generated by pyuic4 and inherited

# Primary UI class that inherits the converted python UI class class
class Ui_formProfilometer(profilometerUIConvert.Ui_formProfilometer):
    def __init__(self):
        # Initializes the QWidget superclass
        QtGui.QWidget.__init__(self)
        # Runs setupIU method upon initialization
        self.setupUi(self)
        # QtGui.QApplication.processEvents()
        self.buttonFunctionality()
        self.move(0,0)

        profilometerParameters.init()
        self.initializeEquipment()

    # Code specifying the button functionality
    def buttonFunctionality(self):
        # Button clicked commands added after generation, these direct the program to the correct method upon each button click
        self.buttonStartStop.clicked.connect(self.buttonClickedStartStop)
        self.buttonSaveData.clicked.connect(self.buttonClickedSaveData)
        self.buttonPlotData.clicked.connect(self.buttonClickedPlotData)
        self.buttonOrigin.clicked.connect(self.buttonClickedOrigin)
        self.buttonCalibrate.clicked.connect(self.buttonClickedCalibrate)
        # Manual stage movement clicked commands
        self.buttonXPositive.clicked.connect(lambda: self.buttonClickedManualMove('+X',float(self.entryBoxMovementDistance.text())))
        self.buttonXNegative.clicked.connect(lambda: self.buttonClickedManualMove('-X',float(self.entryBoxMovementDistance.text())))
        self.buttonYPositive.clicked.connect(lambda: self.buttonClickedManualMove('+Y',float(self.entryBoxMovementDistance.text())))
        self.buttonYNegative.clicked.connect(lambda: self.buttonClickedManualMove('-Y',float(self.entryBoxMovementDistance.text())))
        self.buttonZPositive.clicked.connect(lambda: self.buttonClickedManualMove('+Z',float(self.entryBoxMovementDistance.text())))
        self.buttonZNegative.clicked.connect(lambda: self.buttonClickedManualMove('-Z',float(self.entryBoxMovementDistance.text())))

    # Method for clicking the start/stop button
    def buttonClickedStartStop(self):

        ## If statement that cycles through the start/stop functionality of the button
        # First if statement that checks for routine running = True and then stops the run
        if profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning) == True:
            # Update the profilometer routine running to False when start/stop button clicked
            profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)
            self.updateMovementButtonsState(True)
            # Updates the start/stop button to green and start
            self.buttonStartStop.setText('Start')
            self.buttonStartStop.setStyleSheet('background-color: green;border:0px;border-radius:10')
            print('Profilometer Routine Stopped')

        # Else if statement that checks for routine running = False and then starts the run
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
            self.buttonStartStop.setStyleSheet('background-color: red;border:0px;border-radius:10')
            print('Profilometer Routine Started')

            ## Routine plot in realtime
            # Runs a while loop that checks to see if the routine is running
            while profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                # Asks the GUI to process any events manually
                QtGui.QApplication.processEvents()

                try:
                    # If statement that checks to see if a new data point has been added
                    if profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_newDataPoint):
                        # Calls the plot data routine
                        self.buttonClickedPlotData()
                        # print('plot')

                        # Acquires the data thread lock
                        profilometerParameters.dataThreadLock.acquire()
                        # print('dataThreadLock acquired (UI)')
                        # Sets the new data point to false
                        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_newDataPoint,False)
                        # Releases the data thread lock
                        profilometerParameters.dataThreadLock.release()
                        # print('dataThreadLock released (UI)')
                except:
                    pass
                # # For loop that causes the plot to be updated once every second while still allowing the loop to be interrupted
                # for i in range(1000):
                #     # Asks the GUI to process any events manually
                #     QtGui.QApplication.processEvents()
                #     # Checks to see if the routine has been stopped once every 0.001 seconds
                #     if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                #         break
                #     time.sleep(.001)



    # Method for clicking the save button.
    # This saves the profilomter data to the file name specified.
    def buttonClickedSaveData(self):
        # While loop that checks for widgets within the plot layout and then deletes them
        # This is used to clear the plot each time a new plot is added to the plot layout
        while self.layoutPlot.count() > 0:
            item = self.layoutPlot.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if w:
                w.deleteLater()

        # Retrieves the direction and millivolts data from the system controller
        [data_X, data_Y, data_Z, data_volts, data_height] = self.systemController.retrieveData()

        # Checks to see if the desired default path doesn't exists on the machine
        if not os.path.exists(profilometerParameters.profilometerDefaultSavePath):
            # Tries to create the desired default path if it doesn't exist
            try:
                os.makedirs(profilometerParameters.profilometerDefaultSavePath)
            except:
                pass

        # Opens a save as dialog directed towards the users' Documents/Data/Profilometer folder
        _saveFileName, saveButtonClicked = QtGui.QFileDialog.getSaveFileNameAndFilter(self, "Save Profilometer Data", os.path.expanduser('~/Documents/Data/Profilometer'))

        # If the user clicks the save button the data is saved as a csv
        if saveButtonClicked:
            # Opens the CSV file to save the data too
            _dataFile = open(str(_saveFileName) + '.csv','wt')

            # Creates a writer that will write the data to the csv file
            _dataWriter = csv.writer(_dataFile)

            # Finds the number of blocks that the user has entered (new block when user hits enter)
            numberOfBlocks = self.entryBoxHeader.blockCount()
            # Runs through each block and saves it as a new row in the CSV file
            for block in range(numberOfBlocks):
                _dataWriter.writerow(('# ' + str(self.entryBoxHeader.document().findBlockByNumber(block).text()),'')) # '' is needed to keep each line together

            # Includes the calibration ratio used below the header data
            _dataWriter.writerow(('# Calibration ratio used: ' + str(profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_calibrationRatio)),''))

            # Includes the direction of the scan
            _dataWriter.writerow(('# Scan direction: ' + str(self.retrieveProfilometerRoutineDirection())))

            # Includes the date and time of the save
            _dataWriter.writerow(('Date and time: ' + str(datetime.datetime.now()),''))

            # Writes the column headers into the file
            _dataWriter.writerow(('X','Y','Z','Volts','Height (mm)'))

            # Loops through each element of the data lists and writes them to a row in the csv
            for i in range(len(data_X)):
                _dataWriter.writerow((data_X[i],data_Y[i],data_Z[i],data_volts[i],data_height[i]))

            # Closes the data file
            _dataFile.close()
        # If the cancel button is clicked nothing happens for now
        else:
            pass

        # Displays the plot of the data that was also saved
        graphicsLayoutWidget = pg.GraphicsLayoutWidget()
        graphicsLayout = pg.GraphicsLayout(border=(100,100,100))
        graphicsLayoutWidget.addItem(graphicsLayout)
        plot1 = graphicsLayout.addPlot(title='Profile')
        plot1.plot(x = data_X, y = data_height)
        plot1.setLabel('bottom','Distance (mm)')
        plot1.setLabel('left','Height (mm)')
        # plot1.setXRange(0,(float(self.entryBoxTravelDistance.text()) + 2.0))
        # plot1.setYRange(-1.0,1.0)
        plot1.showGrid(True, True, 0.75)
        self.layoutPlot.addWidget(graphicsLayoutWidget)

    # Method for clicking the plot data button
    def buttonClickedPlotData(self):
        # While loop that checks for widgets within the plot layout and then deletes them
        # This is used to clear the plot each time a new plot is added to the plot layout
        while self.layoutPlot.count() > 0:
            item = self.layoutPlot.takeAt(0)
            if not item:
                continue
            w = item.widget()
            if w:
                w.deleteLater()

        # Retrieves the direction and millivolts data from the system controller
        [data_X, data_Y, data_Z, data_volts, data_height] = self.systemController.retrieveData()

        # Displays the plot of the data that was also saved
        graphicsLayoutWidget = pg.GraphicsLayoutWidget()
        graphicsLayout = pg.GraphicsLayout(border=(100,100,100))
        graphicsLayoutWidget.addItem(graphicsLayout)
        plot1 = graphicsLayout.addPlot(title='Profile')
        plot1.plot(x = data_X, y = data_height)
        plot1.setLabel('bottom','Distance (mm)')
        plot1.setLabel('left','Height (mm)')
        # plot1.setXRange(0,(float(self.entryBoxTravelDistance.text()) + 2.0))
        # plot1.setYRange(-1,1)
        plot1.showGrid(True, True, 0.75)
        self.layoutPlot.addWidget(graphicsLayoutWidget)

    # Method for clicking the origin button.
    # This takes the profilometer to the origin.
    def buttonClickedOrigin(self):
        self.systemController.moveStageToOrigin()

    # Method for clicking the calibrate button.
    # This allows us to determine if the profilomter is reading correctly.
    def buttonClickedCalibrate(self):
        self.systemController.calibrateProfilometer()

    # Method for clicking the manual movement buttons.
    # Moves the stage in the specified direction direction by specified amount.
    def buttonClickedManualMove(self,_stageMovementManualDirection,_stageMovementManualDistance):
        self.systemController.moveTheStage(_stageMovementManualDirection,_stageMovementManualDistance)

    # Method for determining which direction to run the profilometer routine
    def retrieveProfilometerRoutineDirection(self):
        # If statements that checks which direction radio button is selected.
        if self.radioButtonX.isChecked():
            return 'X'
        elif self.radioButtonY.isChecked():
            return 'Y'

    # Method for initializing the equipment.
    # Initializes the equipment.
    def initializeEquipment(self):
        # Changes the start/stop button to a green start button
        self.buttonStartStop.setText('Start')
        self.buttonStartStop.setStyleSheet('background-color: green;border:0px;border-radius:10')

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
        self.buttonSaveData.setEnabled(_condition)

        # Changes clickability of radio buttons
        self.radioButtonY.setEnabled(_condition)
        self.radioButtonX.setEnabled(_condition)

        # Changes clickability of all entry boxes
        self.entryBoxTravelDistance.setEnabled(_condition)
        self.entryBoxStepSize.setEnabled(_condition)
        self.entryBoxMovementDistance.setEnabled(_condition)
        self.entryBoxHeader.setEnabled(_condition)

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