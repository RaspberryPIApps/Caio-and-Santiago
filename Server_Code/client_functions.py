#Import OpenCV
import cv2
#Import Numpy
import numpy as np

def bestContourCheck(cv2, mask):
    #Create Contours for all blue objects
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maximumArea = 0   
    
    bestContour = None

    for contour in contours:
        currentArea = cv2.contourArea(contour)
        if currentArea > maximumArea:
            bestContour = contour
            maximumArea = currentArea
            
    return bestContour
                
def drawShapes(frame, cv2, bestContour):    
    
    if bestContour is not None:
        x,y,w,h = cv2.boundingRect(bestContour)
        
        #print "----"
        #print "x cord" + str(x)
        #print "y cord" + str(y)
        #print "Width " + str(w)
        #print "Length " + str(h)
        

        #cv2.rectangle(frame, (x,y),(x+10,y+10), (0,0,255), 3)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (0,0,255), 3)
        #cv2.circle(frame, (x,y), 10, (0,0,255))
        #cv2.circle(frame, (x+w,y), 10, (0,0,255))
        #cv2.circle(frame, (x,y+h), 10, (0,0,255))
        #cv2.circle(frame, (x+w,y+h), 10, (0,0,255))
        
        cv2.circle(frame, (x+w/2,y+h/2), w/2, (255,255,255), 3)
        
        cv2.circle(frame, (x+w/2,y+h/2), 5, (255,255,255), 3)
        
        #cv2.rectangle(frame, (x+w/2,y+h/2),(0,0), (0,255,255), 3)
        
        cv2.line(frame, (x+w/2,y+h/2),(x+w/2,0), (0,255,255), 3)
        cv2.line(frame, (x+w/2,y+h/2),(0,y+h/2), (255,255,0), 3)  
        #cv2.line(frame, (x+w/2,y+h/2),(0,0), (0,0,0), 1)  
        return (x,y,w,h)
    else:
        return (0,0,0,0)

def setMask(frame, lower, upper):
    #Convert the current frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    #Create a binary image, where anything blue appears white and everything else is black
    mask = cv2.inRange(hsv, lower, upper)

    #Get rid of background noise using erosion and fill in the holes using dilation and erode the final image on last time
    element = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    mask = cv2.erode(mask,element, iterations=2)
    mask = cv2.dilate(mask,element,iterations=2)
    mask = cv2.erode(mask,element)    
    
    return mask
    
    
def imshow(frame, mask):
    #Show the original camera feed with a bounding box overlayed 
    cv2.imshow('frame',frame)
    #Show the contours in a seperate window
    cv2.imshow('mask',mask)    
    
def calDis(x,y,w,h):
    #-----------------
    #F = (P x  D) / W
    #perceived focal length F
    #apparent width in pixels P
    #some distance D
    #with a known width W << 16 circurference -> 5inch diameter
    #D' = (W x F) / P
    D = 30 #inch measured distance
    
    #D' = (W x F) / P
    F = 615#aprox
    W = 5#inch
    P = w
    D = 0
    if(P > 0):
        D = (W * F) / P
    return D


def sendMSG(msg,host, port,s):    
    try :
        #Set the whole string
        s.sendto(msg, (host, port))
         
        # receive data from client (data, addr)
        d = s.recvfrom(1024)
        reply = d[0]
        addr = d[1]
         
        print 'Server reply : ' + reply
     
    except socket.error, msg:
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


#Not to be used inside a loop. They are used to retrieve variables that should not change.
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
    #txt = txt.split()
    return txt

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