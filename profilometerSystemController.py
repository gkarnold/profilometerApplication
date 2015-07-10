'''
System controller portion of the profilometer program.
The system controller handles the data and controls the equipment
'''

# Imports
import threading # threading is used for creating multiple threads
import time
import profilometerVariables
import profilometerXYZStages # File containing XYZStages class
import profilometerAgilent34461a # File containing Agilent 34461a class

# Defines the systemController class
class systemController(threading.Thread):

    # Initializes the systemController class
    def __init__(self):
        threading.Thread.__init__(self)
        print('systemController initialized')
        self.getVariables()

    def run(self):
        print('systemController run')
        self.initializeEquipment()
        self.initializeData()
        print('Starting controller while loop')
        while True:
        #     if not self.getVariables(): # False
        #         time.sleep(2)
        #     elif self.getVariables(): # True
        #         # stageMove = threading.Thread(target=self.stages.moveToOrigin())
        #         # stageMove.start()
        #         # print('move done')
        #         # print('true')
        #         time.sleep(2)

    # Initializes the equipment
    def initializeEquipment(self):
        print('systemController initialized equipment')
        self.Agilent34461a = profilometerAgilent34461a.agilent34461a()
        self.stages = profilometerXYZStages.XYZStages()

    # Initializes the Data
    def initializeData(self):
        print('systemController initialized data')
        print(threading.currentThread())

    # Method to move the stages in the specified direction by the specified amount
    def moveTheStage(self,direction,distance):
        self.stages.moveStages(direction,distance)

    # Method to move the stages to the origin
    def moveStageToOrigin(self):
        self.stages.moveToOrigin()

    def calibrateProfilometer(self):
        self.stages.moveStages('+Z',.5)
        self.Agilent34461a.getReading()

    def profilometerRoutine(self,direction):
        if direction == 'X' or direction == 'Y':
            for i in range(3):
                self.stages.moveStages(direction,i)
                self.Agilent34461a.getReading()
                time.sleep(.5)
        else:
            print('Please select a direction')
            return

    def getVariables(self):
        keepLoopRunning = profilometerVariables.getDictionaryVariable('systemControllerController')
        return keepLoopRunning
