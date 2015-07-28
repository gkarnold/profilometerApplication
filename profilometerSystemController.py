'''
System controller portion of the profilometer program.
The system controller handles the data and controls the equipment
'''

# Imports
import threading # threading is used for creating multiple threads
import visa
import profilometerParameters
import profilometerXYZStages # File containing XYZStages class
import profilometerAgilent34461a # File containing Agilent 34461a class
import profilometerDataClass # File containing the data class

import math

# Defines the systemController class
class systemController(threading.Thread):

    # Initializes the systemController class
    def __init__(self):
        threading.Thread.__init__(self)
        # Dictionary of multipliers based on the movement direction. This flips the sign of the number the user enters
        # when they click a negative manual movement button.
        self._directionDictionary = {
            '+X': 1,
            '-X': -1,
            '+Y': 1,
            '-Y': -1,
            '+Z': 1,
            '-Z': -1,
        }

        # TEMP VARIABLE INITIALIZATION #
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection,'X')
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize,'0')
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance,'0')

    def run(self):
        # Initializes the data and equipment
        self.initializeData()
        self.initializeEquipment()
        self.retrieveVariables()
        while (True):
            # if self.systemControllerProfilometerRoutineStart: # True - start profilometer routine # Commented out to see if we can skip getVaraibles
            if profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart): # True - start profilometer routine
                # self.profilometerRoutine(self.systemControllerProfilometerRoutineDirection,self.systemControllerProfilometerRoutineTravelDirection,self.systemControllerProfilometerRoutineStepSize)
                self.profilometerRoutine(profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection), profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance), profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize))


    # Initializes the equipment
    def initializeEquipment(self):
        profilometerParameters.profilometerResourceManager = visa.ResourceManager()

        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)
        self.Agilent34461a = profilometerAgilent34461a.agilent34461aClass()
        self.substrateStages = profilometerXYZStages.XYZStages()
        self.substrateStages.XYZStagesInitialize()

    # Initializes the Data
    def initializeData(self):
        # Sets the profilometer correction ratio to 1
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_calibrationRatio,1)

    # Method to move the stages in the specified direction by the specified amount
    def moveTheStage(self,direction,distance):
        # Checks the direction and multiplies by a -1 if negative or a 1 is positive
        distance = distance * int(self._directionDictionary[direction])

        if direction == '-X' or direction == '+X':
            direction = self.substrateStages.positioner_X
        elif direction == '-Y' or direction == '+Y':
            direction = self.substrateStages.positioner_Y
        elif direction == '-Z' or direction == '+Z':
            direction = self.substrateStages.positioner_Z

        self.substrateStages.moveStageRelative(direction,[distance])

    # Method to move the stages to the origin (profilometer start position) (2,41,9.4) per Chris
    def moveStageToOrigin(self):
        self.substrateStages.moveStageAbsolute(self.substrateStages.macroGroup,[2,41,9.4])

    # Method to determine if the profilometer is properly calibrated
    # Moves stage by 0.5 mm in Z and checks to see how much the omron sensor thinks the stage moved
    def calibrateProfilometer(self):
        # Temporary Usage: Get current location
        [stageX, stageY, stageZ] = self.substrateStages.retrieveStagePostion()
        print('Stage Position (x,y,z): ({},{},{})'.format(stageX,stageY,stageZ))

        # Sets the routine to running so we can get readings from the mutlimeter
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,True)

        # Checks the omron sensor for its current reading
        _calibrationValue1 = self.Agilent34461a.retrieveVoltage()

        # Moves the satges in the -Z direction by 0.5 mm
        self.substrateStages.moveStageRelative(self.substrateStages.positioner_Z,[-0.5])

        # Checks the omron sensor for its new reading
        _calibrationValue2 = self.Agilent34461a.retrieveVoltage()

        # Finds the correction ratio based on the known move distance and the read move distance
        _correctionRatio = -0.5/(_calibrationValue2 - _calibrationValue1)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_calibrationRatio,(_correctionRatio))

        # Updates the routine to no longer be running
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)

        # Moves the stages back up 0.5 mm to their original postion
        self.substrateStages.moveStageRelative(self.substrateStages.positioner_Z,[0.5])

    # Method that runs the profilometer routine
    def profilometerRoutine(self, direction, travelDistance, stepSize):
        # Converts the travel distance and step size to a float
        travelDistance = float(travelDistance)
        stepSize = float(stepSize)

        # Changes profilometer start to false so that the routine only runs once
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)

        # Clears the data from any previous runs
        profilometerParameters.clearDataStorageInstances()

        # Creates an instance of the stages
        _stagesInstance = profilometerXYZStages.XYZStages()
        _stagesInstance.XYZStagesInitialize()

        # If statement that checks to make sure a valid direction has been entered and changes direction to
        # a value recognized by the stages class
        if direction == 'X':
            _movementDirection = _stagesInstance.positioner_X

        elif direction == 'Y':
            _movementDirection = _stagesInstance.positioner_Y

        else:
            print('Please select a direction')
            return

        # If statement that checks the sign of the travel distance
        if travelDistance < 0:
            stepSize = -stepSize

        i = 0
        # While loop that starts at 0 and moves the stage by step size until travel distance has been reached
        # Flow is: Scan > Move > Iterate - This allows us to scan the first and last points
        while i <= abs(float(travelDistance)):
            # Checks to see if the user clicked the stop button mid print and stops the print if so
            if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                _stagesInstance.moveStageAbort()
                print('MID PRINTING STOP')
                break

            # Gets a data reading from the multimeter
            multimeterData = self.Agilent34461a.retrieveVoltage()
            # Gets the current x,y,z stage locations
            [x,y,z] = _stagesInstance.retrieveStagePostion()

            # Creates an instance of the data class with the current data
            profilometerDataClass.profilometerData(x,y,z,multimeterData)

            # Moves the stages by creating a stage thread and then running that thread for the movement amount and direction
            _stagesInstanceThread = threading.Thread(target=_stagesInstance.moveStageRelative,args=(_movementDirection,[stepSize/1000]))
            _stagesInstanceThread.start()

            # For loop that runs during the stage movement and aborts the movement if the user clicks the stop button
            motionStatus = _stagesInstance.checkMotionStatus()

            while (motionStatus != 0):
                motionStatus = _stagesInstance.checkMotionStatus()
                # Checks to see if the user has clicked the stop button and aborts the stage movement if they have
                if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                    _stagesInstance.moveStageAbort()
                    print('MID PRINTING STOP')
                    break

            # Increases i by the step size for the next iteration
            i = i + abs(stepSize)/1000

        print('Profilometer Routine Complete')


        ### ---- ### UNCOMMENT BELOW EVENTUALLY
        # For now we will force the user to click the stop button once the routine finishes.
        # This is so that we can free the interface without having to start/stop the print routine

        # # Updates the global parameter for profilometer routine running to false at end of print routine
        # profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)




    # Method to update the instance variables
    def retrieveVariables(self):
        self.systemControllerProfilometerRoutineStart = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)

        self.systemControllerProfilometerRoutineRunning = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning)
        self.systemControllerProfilometerRoutineDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection)
        self.systemControllerProfilometerRoutineStepSize = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize)
        self.systemControllerProfilometerRoutineTravelDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance)

    # Method to save the data from the last run
    def retrieveData(self):
        # Creates lists that will be appended to with the desired data
        _dataDirection_X = []
        _dataDirection_Y = []
        _dataDirection_Z = []
        _dataVolts = []
        _dataHeight = []

        # # Generates fake data for testing
        # profilometerParameters.clearDataStorageInstances()
        # for i in range(2000):
        #     profilometerDataClass.profilometerData(i*1.0,i*1.0,i*1.0,math.sin(i/math.pi*180/10000)*math.exp(i/1000))

        # Loops through each data class instance and appends the data to the lists
        # Also pulls out the data to return
        for _dataSet in profilometerParameters.retrieveDataStorageInstances():
            _dataDirection_X.append(_dataSet.x)
            _dataDirection_Y.append(_dataSet.y)
            _dataDirection_Z.append(_dataSet.z)
            _dataVolts.append(_dataSet.volts)
            #Calculates the height of the sample by multiplying it by the correction factor
            _dataHeight.append(_dataSet.volts * profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_calibrationRatio))

        # Returns the direction and volts data
        return _dataDirection_X, _dataDirection_Y, _dataDirection_Z, _dataVolts, _dataHeight