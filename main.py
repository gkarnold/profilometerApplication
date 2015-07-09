'''
This is the main run file for the profilometer program.
This program will load the UI on the main thread and spawn a second thread with
the system controller on it.
'''

# Imports
import sys
import threading
import profilometerVariables # File containing the global variables for the appliction
import profilometerUI # File containing the UI
import profilometerSystemController # File containing the System Controller



def main():
    # Initalize the global variables
    profilometerVariables.init()


    # Starting up the UI
    profilometerUI.main()

    systemController.doSomething()



if __name__ == '__main__':
    main()
