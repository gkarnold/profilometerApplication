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

# Function to update a dictionary parameter
def updateDictionaryParameter(key,value):
    globalParameters[key] = value
# Function to remove a dictionary parameter
def removeDictionaryParameter(key):
    del globalParameters[key]

# Function to retrieve a dictionary parameter
def retrieveDictionaryParameter(key):
    return globalParameters[key]

# Function to retrieve the entire dictionary
def retrieveDictionary():
    return globalParameters