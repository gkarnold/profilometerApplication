'''
This is the portion of the profilometer program for initializing the
stages and loading them into the main thread for usage.
'''

# Imports
import XPS_Q8_drivers # Control program for the XPS system
import profilometerEquipment # Imports the equipment file for equipment inheritance
import time ##### TESTING ONLY

# Stages class for initializing the stages into the program. Inherits the equipment class
class stages(profilometerEquipment.equipment):
    # Class variables

    def __init__(self):
        profilometerEquipment.equipment.__init__(self)
        print('Stages Initialized')
        return
