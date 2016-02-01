'''
Portion of profilometer program that holds the parameters. This is shared between all modules and is used to allow
communication between the different threads.
'''

# Imports
import os.path
import threading

# Initializes the global paramters
def init():
    global globalParameters
    global profilometerDefaultSavePath
    global dataThreadLock

    globalParameters = {}
    agilent34461a = None
    profilometerResourceManager = None
    profilometerDefaultSavePath = os.path.expanduser('~/Documents/Data/Profilometer')
    dataThreadLock = threading.Lock()


# Variables holding the keys for the profilometer's system controller
kHNSystemControllerProfilometer_routineRunning = 'kHNSystemControllerProfilometer_routineRunning'
kHNSystemControllerProfilometer_routineStart = 'kHNSystemControllerProfilometer_routineStart'
kHNSystemControllerProfilometer_routineStepSize = 'kHNSystemControllerProfilometer_routineStepSize'
kHNSystemControllerProfilometer_routineDirection = 'kHNSystemControllerProfilometer_routineDirection'
kHNSystemControllerProfilometer_routineTravelDistance = 'kHNSystemControllerProfilometer_routineTravelDistance'
kHNSystemControllerProfilometer_calibrationRatio = 'kHNSystemControllerProfilometer_calibrationRatio'
kHNSystemControllerProfilometer_newDataPoint = 'kHNSystemControllerProfilometer_newDataPoint'

# Data Storage instance ID list
kHNSystemControllerProfilometer_dataStorageInstances = []



# Function to update a dictionary parameter
def updateDictionaryParameter(key,value):
    global globalParameters
    globalParameters[key] = value
# Function to remove a dictionary parameter
def removeDictionaryParameter(key):
    global globalParameters
    del globalParameters[key]

# Function to retrieve a dictionary parameter
def retrieveDictionaryParameter(key):
    return globalParameters[key]

# Function to retrieve the entire dictionary
def retrieveDictionary():
    return globalParameters

# Function to update the list of data storage instances
def updateDataStorageInstances(updatedInstanceID):
    global kHNSystemControllerProfilometer_dataStorageInstances
    kHNSystemControllerProfilometer_dataStorageInstances.append(updatedInstanceID)

# Functon to retrieve the list of data storage instances
def retrieveDataStorageInstances():
    return kHNSystemControllerProfilometer_dataStorageInstances

# Functin to clear the list of data storage instances
def clearDataStorageInstances():
    global kHNSystemControllerProfilometer_dataStorageInstances
    kHNSystemControllerProfilometer_dataStorageInstances = []