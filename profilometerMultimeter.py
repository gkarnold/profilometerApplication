'''
Generic multimeter class that inherits the equipment class.
This is for the profilometer program
'''

# Imports
import profilometerEquipment # Imports the equipment file for equipment inheritance
import time # used to hold the program while the profilometer is allowed to reach equlibrium

class multimeter(profilometerEquipment.equipment):

    def __init__(self):
        profilometerEquipment.equipment.__init__(self) # Initializes the equipment superclass
        print('Multimeter Initialized')
        return

    def retrieveReading(self):
        print(' ')
        print('Multimeter reading started')
        self.reachEquilibrium()
        multimeterReading = 15 # temp number to test code flow
        print('Multimeter reading finished')
        print(' ')
        return multimeterReading

    def reachEquilibrium(self):
        print('Please wait for multimeter to reach equilibrium')
        time.sleep(1.5)
        return