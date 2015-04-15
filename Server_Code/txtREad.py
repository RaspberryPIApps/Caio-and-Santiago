import os

path = os.path.dirname(os.path.realpath(__file__))
pathname = path + "/dummyData.txt"
#valueDic = {}
#pathname = os.path.dirname(os.path.realpath(__file__)) + "\config.txt"

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




#print generateValueDic(pathname)
#
#print generateValueDic(pathname).get("IP")
#
#print os.getcwd()
#
#print getLine(pathname, 10)
#
#replaceLine(pathname, 10, 'Focal', '500')
#
#print getLine(pathname, 10)
#


#print path
#print pathname
import datetime
import time

def getLine(file_name, line_num):
    lines = open(file_name, 'r').readlines()
    txt = lines[line_num]
    txt = txt.split()
    return txt


lineNum = 0

while(True):

    txtData = getLine(pathname, lineNum)
    print type(txtData)
    print txtData    

    if(txtData != "null"):
        #txtData = txtData.split()
        
        ts = time.time()
        
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
        txtData[4] = st
        dataOut = txtData[0] + " " + txtData[2] + " " + txtData[4] + " " + txtData[6] + " " + txtData[8]
        print dataOut
    else:
        print "error no more data"
        break
    lineNum += 1
    
    
    msg = raw_input('More data: ')  

    
    
print "done"



'''
with open(pathname) as f:
    for line in f:
        #lineArray = getLine(pathname, l)
        lineArray = line.split()
        print lineArray
'''
