import profilometerStages
import XPS_Q8_drivers
import threading
import time

class XYZStages(profilometerStages.stages):

    def __init__(self):
        profilometerStages.stages.__init__(self)
        print('XYZStages Initialized')
        # Instance variables that will be defined during the stages initialization in below method
        self._XPSSystem = XPS_Q8_drivers.XPS()
        self._socketID1 = None
        self._socketID2 = None
        self._macroGroup = None
        self._positioner_X = None
        self._positioner_Y = None
        self._positioner_Z = None

        self.XYZStagesInitialize()

        return

    def run(self):
        self.XYZStagesInitialize()

        # print('Move in X')
        # self.moveStageAbsolute(self._positionerXYX,[0])
        # print('Move in X')
        # self.moveStageAbsolute(self._positionerXYX,[15])

    def XYZStagesInitialize(self):
        print('XYZStagesInitialize')
        # Creates an instance of the XPS system
        self._XPSSystem = XPS_Q8_drivers.XPS()
        
        # Gets the socketIDs for the created system
        # SocketID1 is for initiating movements
        self._socketID1 = self._XPSSystem.TCP_ConnectToServer('192.168.0.254',5001,20) # Returns -1 if connection error occurs
        # SocketID2 is for interrupting movements
        self._socketID2 = self._XPSSystem.TCP_ConnectToServer('192.168.0.254',5001,21) # Returns -1 if connection error occurs

        # If statements to check to make sure that both sockets were created correctly
        if (self._socketID1 == -1):
            print('Connection to XPS failed, check IP and Port. SocketID1')
            sys.exit()
        if (self._socketID2 == -1):
            print('Connection to XPS failed, check IP and Port. SocketID2')
            sys.exit()
        # Sets up the macro group and the positioners
        self._macroGroup = 'XYZ'
        self._positioner_X = self._macroGroup + '.X'
        self._positioner_Y = self._macroGroup + '.Y'
        self._positioner_Z = self._macroGroup + '.Z'

    def moveStageAbsolute(self,direction,location):
        self._XPSSystem.GroupMoveAbsolute(self._socketID1,direction,location)

    def moveStageRelative(self,direction,distance):
        print(distance)
        self._XPSSystem.GroupMoveRelative(self._socketID1,direction,distance)


    def moveStageAbort(self):
        self._XPSSystem.GroupMoveAbort(self._socketID2,self._positioner_X)
        self._XPSSystem.GroupMoveAbort(self._socketID2,self._positioner_Y)
        self._XPSSystem.GroupMoveAbort(self._socketID2,self._positioner_Z)
        self._XPSSystem.GroupMoveAbort(self._socketID2,self._macroGroup)

    def retrieveStagePosition(self):
        [XError,X] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self._positioner_X,1)
        [YError,Y] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self._positioner_Y,1)
        [ZError,Z] = self._XPSSystem.GroupPositionCurrentGet(self._socketID1,self._positioner_Z,1)
        return X,Y,Z

def main():
    '''
    # Creates a stages instance
    createdStages1 = XYZStages()
    createdStages2 = XYZStages()
    # Create a thread for the stages instance
    createdStages1Thread = threading.Thread(target=createdStages1.moveStageAbsolute,args=(createdStages1._positionerXYX,[0]))
    createdStages1Thread.start()

    print(threading.activeCount())
    time.sleep(3)
    createdStages2
    createdStages2.moveStageAbort()
    '''

    createdStages3 = XYZStages()
    [x,y,z] = createdStages3.retrieveStagePosition()
    print('Location: ({},{},{})'.format(x,y,z))


if __name__ == '__main__':
    main()