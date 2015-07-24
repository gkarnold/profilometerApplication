'''
This is the main run file for the profilometer program.
This program will load the UI on the main thread and spawn a second thread with
the system controller on it.
New comment
'''

# Imports
import sys
import threading
import profilometerParameters # File containing the global variables for the appliction
import profilometerUI # File containing the UI
import profilometerSystemController # File containing the System Controller



def profilometerApplication():
    # Initalize the global variables
    profilometerParameters.init()


    # Starting up the UI
    profilometerUI.profilometerUIMain()



if __name__ == '__main__':
    profilometerApplication()


'''
ERROR THAT OCCURS WHEN EXITING DO NOT DELETE THIS COMMENT - GALEN

Exception AttributeError: "'NoneType' object has no attribute 'InvalidSession'" in Exception in thread Thread-2:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 810, in __bootstrap_inner
    self.run()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 763, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/Users/equipment/Documents/Code/profilometerApplication/profilometerSystemController.py", line 37, in run
    self.getVariables()
  File "/Users/equipment/Documents/Code/profilometerApplication/profilometerSystemController.py", line 115, in getVariables
    self.systemControllerProfilometerRoutineTravelDirection = profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineTravelDistance)
AttributeError: 'NoneType' object has no attribute 'retrieveDictionaryParameter'

 ignored

'''