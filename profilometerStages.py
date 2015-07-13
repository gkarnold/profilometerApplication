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

    def stagesInitialize(self,controlSystemIP,controlSystemPort,controlSystemTimeOut):
        # Define global variables that will be created when stages are initialized
        global macroGroup
        global positionerXYX
        global positionerXYY
        global positionerZPos
        global controlSystem
        global socketID

        # Checks for potential errors connecting to the XPS System (Code from XPS manufacture)
        def displayErrorAndClose (socketId, errorCode, APIName):
			if (errorCode != -2) and (errorCode != -108):
				[errorCode2, errorString] = myxps.ErrorStringGet(socketId, errorCode)
				if (errorCode2 != 0):
					print (APIName + ': ERROR ' + str(errorCode))
				else:
					print (APIName + ': ' + errorString)
			else:
				if (errorCode == -2):
					print (APIName + ': TCP timeout')
				if (errorCode == -108):
					print (APIName + ': The TCP/IP connection was closed by an administrator')
			myxps.TCP_CloseSocket(socketId)
			return

        # Sets the controlSystem to an instance of the XPS class from XPS_Q8_drivers.py
        controlSystem = XPS_Q8_drivers.XPS()
        # Gets the socketID based on connecting the the server with the specified input IP, port and timeout
        socketID = 1
        # socketID = controlSystem.TCP_ConnectToServer(str(controlSystemIP),controlSystemPort,controlSystemTimeOut)
        # If the connection fails, socketID will be set to -1, this loop checks for this and exits the program if connection fails
        if (socketID == -1):
            print('Connection to XPS failed, check IP & Port')
            sys.exit()

        # String assignments that will be used later to send commands to the controlSystem
        macroGroup = 'XYZ'
        positionerXYX = macroGroup + '.X'
        positionerXYY = macroGroup + '.Y'
        positionerZPos = macroGroup + '.Z'
        print('Done')
        return

    def moveStages(self,direction,distance):
        print('Stages moved in {} by {} mm.'.format(direction,distance))

    def moveToOrigin(self):
        print('Stages moved to origin')
        ### TESTING ONLY
        for i in range(5):
            print(i)
            time.sleep(1)

    def retrieveStageLocation(self):
        x = 1
        y = 2
        z = 3
        return x,y,z
