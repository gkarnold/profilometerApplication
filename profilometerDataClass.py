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




'''
#Commented out, this is for testing that the class is functioning properly with the global variable module

def main():


    for i in range(5):
        x = float(raw_input('x data: '))
        y = 1
        z = 1
        V = 1
        data = profilometerData(x,y,z,V)

    xData = [name.x for name in profilometerParameters.retrieveDataStorageInstances()]
    print(xData)

    print(profilometerParameters.retrieveDataStorageInstances())
    profilometerParameters.clearDataStorageInstances()
    xData = [name.x for name in profilometerParameters.retrieveDataStorageInstances()]
    print(xData)

    print(profilometerParameters.retrieveDataStorageInstances())



if __name__ == '__main__':
    main()
'''