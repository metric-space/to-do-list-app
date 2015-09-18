import os 
import os.path

defaultname     = '.to-do-list.db'
home            = os.path.expanduser('~')
defaultFilePath = os.path.join(home,defaultname)

def checkIfTableFileExists(name=defaultFilePath):
    return os.path.exists(name)

def deleteTableFile(name=defaultFilePath):
    os.remove(name)

def createTableFile(name=defaultFilePath):
    open(name,'w')    




