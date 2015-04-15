
'''
#BReaks the format of the data string sent from cam
#camDataOut = str(flag) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + " " + str(D)
def breakFormatedCameraData(dataPos,formatData):
    dataOut = formatData.split()
    
    if(dataPos == "flag"):
        dataOut = dataOut[0]
    elif(dataPos == "x"):
        dataOut = dataOut[1]
    elif(dataPos == "y"):
        dataOut = dataOut[2]
    elif(dataPos == "w"):
        dataOut = dataOut[3]
    elif(dataPos == "h"):
        dataOut = dataOut[4]
    elif(dataPos == "D"):
        dataOut = dataOut[5]
    
    return dataOut
    


txt = "True 334 293 7  8 439"
print txt

print breakFormatedCameraData("flag",txt)
print breakFormatedCameraData("x", txt)
print breakFormatedCameraData("y", txt)
print breakFormatedCameraData("w", txt)
print breakFormatedCameraData("h", txt)
print breakFormatedCameraData("D", txt)

#print "Syntax for command"
#print "command pos - ex data 1 = will give the data of pos 1"
import random

x = int(random.randrange(0, 100))
y = int(random.randrange(0, 100))
w = int(random.randrange(0, 100))
h = int(random.randrange(0, 100))
D = int(random.randrange(0, 100))

camDataOut = "rand" + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + " " + str(D)
print camDataOut
'''

'''
import os

path = os.path.dirname(os.path.realpath(__file__))
pathname = path + "/config.txt"
#valueDic = {}

def generateValueDic(file_name):
    valueDic = {}
    with open(file_name) as f:
        for line in f:
            lineArray = line.split()
    
            if(len(lineArray) > 3):
    
                if(str(lineArray[1]) == "upper"): 
                    valueDic[str(lineArray[1])] = (lineArray[3],lineArray[4],lineArray[5])
    
                if(str(lineArray[1]) == "lower"): 
                    valueDic[str(lineArray[1])] = (lineArray[3],lineArray[4],lineArray[5])
          
                if(str(lineArray[1]) == "IP"):
                    valueDic[str(lineArray[1])] = str(lineArray[3]) 
    
                if(str(lineArray[1]) == "ObjectSize"):
                    valueDic[str(lineArray[1])] = str(lineArray[3])  
    
                if(str(lineArray[1]) == "MeasuredDis"):
                    valueDic[str(lineArray[1])] = str(lineArray[3])                   
    
                if(str(lineArray[1]) == "Focal"):
                    valueDic[str(lineArray[1])] = str(lineArray[3])  
    return valueDic



def replaceLine(file_name, line_num, key, value):
    text = str(line_num) + " " + str(key) + "       = " + str(value) + '\n'
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def getLine(file_name, line_num):
    lines = open(file_name, 'r').readlines()
    txt = lines[line_num]
    return txt


print generateValueDic(pathname)

print generateValueDic(pathname).get("IP")

#print os.getcwd()
 

#print getLine(pathname, 10)
#
#replaceLine(pathname, 10, 'Focal', '500')
#
#print getLine(pathname, 10)


print os.path.dirname(os.path.realpath(__file__))
'''
from Priority_Queue import *


queue = MyPriorityQueue()
queue.put('item1', 1)
queue.put('item2', 2)
queue.put('item7', 7)
queue.put('item4', 4)
queue.put('item6', 6)
queue.put('item9', 0)


print queue.get()
print queue.get()
