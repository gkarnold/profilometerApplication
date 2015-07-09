'''
XYZ Stages that inherit from the stages class
'''

# Imports
import profilometerStages # Imports the stages file for stage inheritance

class XYZStages(profilometerStages.stages):

    def __init__(self):
        profilometerStages.stages.__init__(self)
        print('XYZStages Initialized')
        return