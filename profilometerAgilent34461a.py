'''
Agilent 34461a class that inherets from the multimeter class.
'''

# Import
import profilometerMultimeter

class agilent34461a(profilometerMultimeter.multimeter):

    def __init__(self):
        profilometerMultimeter.multimeter.__init__(self)
        print('agilent34461a intialized')