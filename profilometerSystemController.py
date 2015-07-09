'''
System controller portion of the profilometer program.
The system controller handles the data and controls the equipment
'''

# Imports
import threading # threading is used for creating multiple threads
import time
import profilometerXYZStages # File containing XYZStages class
import profilometerMultimeter # File containing multimeter class

# Defines the systemController class
class systemController(threading.Thread):

    # Initializes the systemController class
    def __init__(self):
        threading.Thread.__init__(self)
        print('systemController initialized.')

    def run(self):
        print('systemController run')
        self.initializeEquipment()
        self.initializeData()

    # Initializes the equipment
    def initializeEquipment(self):
        print('systemController initialized equipment')
        self.Agilent34461a = profilometerMultimeter.multimeter()
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

    def calibrateProfilometer(self):
        self.stages.moveStages('+Z',.5)
        self.Agilent34461a.getReading()

    def profilometerRoutine(self,direction):
        if direction == 'X' or direction == 'Y':
            for i in range(5):
                self.stages.moveStages(direction,i)
                self.Agilent34461a.getReading()
                time.sleep(1)
        else:
            print('Please select a direction')
            return