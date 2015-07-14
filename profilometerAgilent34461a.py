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
        print('agilent34461a intialized')


    def retrieveReading(self):
        print('Started reading Agilent 34461a Multimeter')
        # Sets a sample size
        multimeterReadingsSampleSize = 10
        # Sets a varaible that will hold the total value of all multimeter readings for finding the average
        multimeterReadingsTotals = 0.0
        for i in range(multimeterReadingsSampleSize):
            # Checks to see if the profilometer routine has been manually stopped by the user
            if not profilometerParameters.retrieveDictionaryParameter(profilometerParameters.kHNSystemControllerProfilometer_routineRunning):
                break
            # Takes the running total and adds the current reading
            multimeterReadingsTotals = multimeterReadingsTotals + float(profilometerParameters.agilent34461a.query("MEASure:VOLTage:DC?"))
        # Finds the average multimeter reading
        multimeterReadingsAverage = multimeterReadingsTotals/multimeterReadingsSampleSize

        print(multimeterReadingsAverage)
        return multimeterReadingsAverage

    def reachEquilibrium(self):
        pass