'''
System controller portion of the profilometer program.
The system controller handles the data and controls the equipment
'''

# Imports
import threading # threading is used for creating multiple threads
import time
import profilometerParameters
import profilometerXYZStages # File containing XYZStages class
import profilometerAgilent34461a # File containing Agilent 34461a class

# Defines the systemController class
class systemController(threading.Thread):

    # Initializes the systemController class
    def __init__(self):
        threading.Thread.__init__(self)
        print('systemController initialized')

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
        while True:
            self.getVariables()

            if self.systemControllerProfilometerRoutineStart: # True - start profilometer routine
                self.profilometerRoutine(self.systemControllerProfilometerRoutineDirection,self.systemControllerProfilometerRoutineTravelDirection,self.systemControllerProfilometerRoutineStepSize)

            if not self.systemControllerProfilometerRoutineRunning: # False - profilometer routine is not running
                time.sleep(.5)
            elif self.systemControllerProfilometerRoutineRunning: # True - profilometer routine is running
                time.sleep(2)

    # Initializes the equipment
    def initializeEquipment(self):
        print('systemController initialized equipment')
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning,False)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)
        self.Agilent34461a = profilometerAgilent34461a.agilent34461a()
        self.stages = profilometerXYZStages.XYZStages()

    # Initializes the Data
    def initializeData(self):
        print('systemController initialized data')

    # Method to move the stages in the specified direction by the specified amount
    def moveTheStage(self,direction,distance):
        self.stages.moveStages(direction,distance)

    # Method to move the stages to the origin
    def moveStageToOrigin(self):
        self.stages.moveToOrigin()

    # Method to determine if the profilometer is properly calibrated
    def calibrateProfilometer(self):
        self.stages.moveStages('+Z',.5)
        self.Agilent34461a.retrieveReading()

    # Method that runs the profilometer routine
    def profilometerRoutine(self,direction,travelDistance,stepSize):
        # If statement that checks to make sure a valid direction has been entered
        if direction == 'X' or direction == 'Y':
            i = 0
            # While look that starts at 0 and moves the stage by step size until travel distance has been reached
            # Flow is: Scan > Move > Iterate - This allows us to scan the first and last points
            while i <= float(travelDistance):
                if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                    print('MID PRINTING STOP')
                    break
                self.Agilent34461a.retrieveReading()
                self.stages.moveStages(direction,float(stepSize))
                i = i + float(stepSize)
            print('Profilometer Routine Complete')
        else:
            print('Please select a direction')
            return

    def getVariables(self):
        self.systemControllerProfilometerRoutineStart = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart)
        profilometerParameters.updateDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStart,False)
        self.systemControllerProfilometerRoutineRunning = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning)
        self.systemControllerProfilometerRoutineDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineDirection)
        self.systemControllerProfilometerRoutineStepSize = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineStepSize)
        self.systemControllerProfilometerRoutineTravelDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance)