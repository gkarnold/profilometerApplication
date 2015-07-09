'''
Generic multimeter class that inherits the equipment class.
This is for the profilometer program
'''

# Imports
import profilometerEquipment # Imports the equipment file for equipment inheritance

class multimeter(profilometerEquipment.equipment):

    def __init__(self):
        profilometerEquipment.equipment.__init__(self) # Initializes the equipment superclass
        print('Multimeter Initialized')
        return

    def getReading(self):
        print('Multimeter reading')