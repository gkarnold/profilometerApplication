def init():
    global globalVariables
    globalVariables = {}

def setDictionaryVariable(key,value):
    globalVariables[key] = value

def removeDictionaryVariable(key):
    del globalVariables[key]

def getDictionaryVariable(key):
    return globalVariables[key]

def getEntireDictionary():
    return globalVariables

def setVariable(variable,value):
    pass

def getVariable(variable):
    pass