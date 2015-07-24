'''
Portion of the profilometer application that defines the class that will be used to store
the data. The data will be imported and then the instance of the class will be appended to the global
storage variable for later recall and processing.
'''

# Imports
import profilometerParameters

# Defines the profilometer data class. This class stores the x,y,z stage location and the millivolts reading
class profilometerData():
    def __init__(self,x,y,z,millivolts):
        self.x = x
        self.y = y
        self.z = z
        self.millivolts = millivolts

        # Adds the instance to the global list of the instances
        profilometerParameters.updateDataStorageInstances(self)