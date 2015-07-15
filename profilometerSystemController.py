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

# Defines the systemController class
class systemController(threading.Thread):

    # Initializes the systemController class
    def __init__(self):
        threading.Thread.__init__(self)
        print('systemController initialized')
        self._directionDictionary = {
            '+X': [1],
            '-X': [-1],
            '+Y': [1],
            '-Y': [-1],
            '+Z': [1],
            '-Z': [-1],

        }

        # TEMP VARIABLE INITIALIZATION #
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection,'X')
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize,'0')
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance,'0')

    def run(self):


        print('systemController run')
        self.initializeEquipment()
        self.initializeData()
        self.getVariables()
        print('Starting controller while loop')
        # while True:
        while (True):
            # self.getVariables()

            # if self.systemControllerProfilometerRoutineStart: # True - start profilometer routine # Commented out to see if we can skip getVaraibles
            if profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart): # True - start profilometer routine
                # self.profilometerRoutine(self.systemControllerProfilometerRoutineDirection,self.systemControllerProfilometerRoutineTravelDirection,self.systemControllerProfilometerRoutineStepSize)
                self.profilometerRoutine(profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection), profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance), profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize))


    # Initializes the equipment
    def initializeEquipment(self):
        print('systemController initialized equipment')
        profilometerParameters.profilometerResourceManager = visa.ResourceManager()

        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)
        self.Agilent34461a = profilometerAgilent34461a.agilent34461aClass()
        self.substrateStages = profilometerXYZStages.XYZStages()
        self.substrateStages.XYZStagesInitialize()

    # Initializes the Data
    def initializeData(self):
        print('systemController initialized data')

    # Method to move the stages in the specified direction by the specified amount
    def moveTheStage(self,direction,distance):
        # Checks the direction and multiplies by a -1 if negative or a 1 is positive
        distance = distance * self._directionDictionary[direction]

        if direction == '-X' or direction == '+X':
            direction = self.substrateStages.positionerXYX
        elif direction == '-Y' or direction == '+Y':
            direction = self.substrateStages.positionerXYY
        elif direction == '-Z' or direction == '+Z':
            direction = self.substrateStages.positionerZPos

        self.substrateStages.moveStageRelative(direction,[distance])

    # Method to move the stages to the origin
    def moveStageToOrigin(self):
        self.substrateStages.moveStageAbsolute(self.substrateStages.macroGroup,[0,0,0])

    # Method to determine if the profilometer is properly calibrated
    def calibrateProfilometer(self):
        self.substrateStages.moveStages('+Z',.5)
        self.Agilent34461a.retrieveVoltage()

    # Method that runs the profilometer routine
    def profilometerRoutine(self,direction,travelDistance,stepSize):

        # Clears the data from any previous runs
        profilometerParameters.clearDataStorageInstances()

        # Creates an instance of the stages
        _stagesInstance = profilometerXYZStages.XYZStages()

        # If statement that checks to make sure a valid direction has been entered and changes direction to
        # a value recognized by the stages class
        if direction == 'X':
            _movementDirection = _stagesInstance.positionerXYX

        elif direction == 'Y':
            _movementDirection = _stagesInstance.positionerXYY

        else:
            print('Please select a direction')
            return


        i = 0
        # While loop that starts at 0 and moves the stage by step size until travel distance has been reached
        # Flow is: Scan > Move > Iterate - This allows us to scan the first and last points
        while i <= float(travelDistance):

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
            _stagesInstanceThread = threading.Thread(target=_stagesInstance.moveStageRelative,args=(_movementDirection,[float(stepSize)/1000])

            # For loop that runs during the stage movement and aborts the movement if the user clicks the stop button
            motionStatus = _stagesInstance.checkMotionStatus()
            while (motionStatus != 0):
                motionStatus = _stagesInstance.checkMotionStatus()
                # Checks to see if the user has clicked the stop button and aborts the stage movement if they have
                if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                    _stagesInstance.moveStageAbort()
                    print('MID PRINTING STOP')
                    break
                print('Movement Done')

            # Increases i by the step size for the next iteration
            i = i + float(stepSize)/1000
        print('Profilometer Routine Complete')

        # Updates the global parameter for profilometer routine running to false at end of print routine
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)


    # Method to update the instance variables
    def getVariables(self):
        self.systemControllerProfilometerRoutineStart = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)

        self.systemControllerProfilometerRoutineRunning = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning)
        self.systemControllerProfilometerRoutineDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection)
        self.systemControllerProfilometerRoutineStepSize = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize)
        self.systemControllerProfilometerRoutineTravelDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance)