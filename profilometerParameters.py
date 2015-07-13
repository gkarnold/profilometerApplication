'''
Portion of profilometer program that holds the parameters. This is shared between all modules and is used to allow
communication between the different threads.
'''

# Initializes the global paramters
def init():
    global globalParameters
    globalParameters = {}

# Variables holding the keys for the profilometer's system controller
kHNSystemControllerProfilometer_routineRunning = 'kHNSystemControllerProfilometer_routineRunning'
kHNSystemControllerProfilometer_routineStart = 'kHNSystemControllerProfilometer_routineStart'
kHNSystemControllerProfilometer_routineStepSize = 'kHNSystemControllerProfilometer_routineStepSize'
kHNSystemControllerProfilometer_routineDirection = 'kHNSystemControllerProfilometer_routineDirection'
kHNSystemControllerProfilometer_routineTravelDistance = 'kHNSystemControllerProfilometer_routineTravelDistance'

# Data Storage instance ID list
_kHNSystemControllerProfilometer_dataStorageInstances = []

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
    global _kHNSystemControllerProfilometer_dataStorageInstances
    _kHNSystemControllerProfilometer_dataStorageInstances.append(updatedInstanceID)

# Functon to retrieve the list of data storage instances
def retrieveDataStorageInstances():
    return _kHNSystemControllerProfilometer_dataStorageInstances

# Functin to clear the list of data storage instances
def clearDataStorageInstances():
    global _kHNSystemControllerProfilometer_dataStorageInstances
    _kHNSystemControllerProfilometer_dataStorageInstances = []