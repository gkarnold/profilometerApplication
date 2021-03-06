'''
Agilent 34461a class that inherets from the multimeter class.
'''

# Import
import profilometerMultimeter
import profilometerParameters
import visa
import time

class agilent34461aClass(profilometerMultimeter.multimeter):

    def __init__(self):
        profilometerParameters.agilent34461a = profilometerParameters.profilometerResourceManager.open_resource('USB0::0x0957::0x1A07::MY53205040::INSTR')
        profilometerMultimeter.multimeter.__init__(self)


    def retrieveVoltage(self):
        # profilometerParameters.agilent34461a.query("DIAG:REMOTE")

        # Sets a sample size
        multimeterReadingsSampleSize = 1
        # Sets a varaible that will hold the total value of all multimeter readings for finding the average
        multimeterReadingsTotals = 0.0
        for i in range(multimeterReadingsSampleSize):
            # Checks to see if the profilometer routine has been manually stopped by the user
            if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                # Returns the multimeter back to local so that the display updates
                # profilometerParameters.agilent34461a.query("DIAG:LOCAL")
                break
            # Takes the running total and adds the current reading
            multimeterReadingsTotals = multimeterReadingsTotals + float(profilometerParameters.agilent34461a.query("MEASure:VOLTage:DC?"))

        # Finds the average multimeter reading
        multimeterReadingsAverage = multimeterReadingsTotals/multimeterReadingsSampleSize

        # Returns the multimeter back to local so that the display updates
        # profilometerParameters.agilent34461a.query("DIAG:LOCAL") # Command does not work for this device (no known command)
        return multimeterReadingsAverage

    def reachEquilibrium(self):
        pass