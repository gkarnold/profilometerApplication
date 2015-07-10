def init():
    global globalVariables
    globalVariables = {}
    globalVariables['allowStageMovement'] = True
    globalVariables['counter'] = 0
    globalVariables['systemControllerController'] = False

def setDictionaryVariable(key,value):
    globalVariables[key] = value

def removeDictionaryVariable(key):
    del globalVariables[key]

def getDictionaryVariable(key):
    return globalVariables[key]

def setVariable(variable,value):
    pass

def getVariable(variable):
    pass