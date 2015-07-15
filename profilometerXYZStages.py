'''
XYZ Stages that inherit from the stages class.
'''

# Imports
import profilometerStages # Imports the stages file for stage inheritance
import XPS_Q8_drivers

class XYZStages(profilometerStages.stages):

    def __init__(self):
        profilometerStages.stages.__init__(self)
        print('XYZStages Initialized')
        # Instance variables that will be defined during the stages initialization in below method
        self._XPSSystem = XPS_Q8_drivers.XPS()
        self._socketID1 = None
        self._socketID2 = None
        self.macroGroup = None
        self.positionerXYX = None
        self.positionerXYY = None
        self.positionerZPos = None

        return

# What function does
    def XYZStagesInitialize(self):
        print('XYZStagesInitialize')

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

        # Creates an instance of the XPS system
        self._XPSSystem = XPS_Q8_drivers.XPS()

        # Gets the socketIDs for the created system
        # SocketID1 is for initiating stage movements
        self._socketID1 = self._XPSSystem.TCP_ConnectToServer('192.168.0.254',5001,20) # Returns -1 if connection error occurs
        # SocketID2 is for interrupting stage movements
        self._socketID2 = self._XPSSystem.TCP_ConnectToServer('192.168.0.254',5001,21) # Returns -1 if connection error occurs

        # If statements to check to make sure that both sockets were created correctly
        if (self._socketID1 == -1):
            print('Connection to XPS failed, check IP and Port. SocketID1')
            sys.exit()
        if (self._socketID2 == -1):
            print('Connection to XPS failed, check IP and Port. SocketID2')
            sys.exit()
        # Sets up the macro group and the positioners
        self.macroGroup = 'XYZ'
        self.positionerXYX = self.macroGroup + '.X'
        self.positionerXYY = self.macroGroup + '.Y'
        self.positionerZPos = self.macroGroup + '.Z'

    # Method for moving the stages to an aboslute position
    def moveStageAbsolute(self, direction, location):
        self._XPSSystem.GroupMoveAbsolute(self._socketID1,direction,location)

    # Method for moving the stages a relative distance
    def moveStageRelative(self, direction, distance):
        self._XPSSystem.GroupMoveRelative(self._socketID1,direction,distance)

    # Method for aborting stage movement. Aborts all directions.
    def moveStageAbort(self):
        self._XPSSystem.GroupMoveAbort(self._socketID2, self.positionerXYX)
        self._XPSSystem.GroupMoveAbort(self._socketID2, self.positionerXYY)
        self._XPSSystem.GroupMoveAbort(self._socketID2, self.positionerZPos)
        self._XPSSystem.GroupMoveAbort(self._socketID2, self.macroGroup)

    # Gets the current location of the stage
    def retrieveStagePostion(self):

        ### LOOK into doing a single call on macroGroup and seeing what the returned results look like.
        # Might be able to simplify this down into a single line of code.

        # Gets the current location of each axis of the stage
        [_stagePositionXError, _stagePositionX] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self.positionerXYX,1)
        [_stagePositionYError, _stagePositionY] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self.positionerXYY,1)
        [_stagePositionZError, _stagePositionZ] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self.positionerZPos,1)

        # Retruns the locations
        return _stagePositionX, _stagePositionY, _stagePositionZ

    def checkMotionStatus(self):
        # Gets the current motion status of each positioner
        [_stageMotionStatusXError, _stageMotionStatusX] = self._XPSSystem.GroupMotionStatusGet(self._socketID2,self.positionerXYX,1)
        [_stageMotionStatusYError, _stageMotionStatusY] = self._XPSSystem.GroupMotionStatusGet(self._socketID2,self.positionerXYX,1)
        [_stageMotionStatusZError, _stageMotionStatusZ] = self._XPSSystem.GroupMotionStatusGet(self._socketID2,self.positionerXYX,1)
        [_stageMotionStatusError, _stageMotionStatus] = self._XPSSystem.GroupMotionStatusGet(self._socketID2,self.macroGroup,1)
        if _stageMotionStatusX == 0 and _stageMotionStatusY == 0 and _stageMotionStatusZ == 0:
            return 0
        else:
            return 1