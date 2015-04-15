'''
    udp socket client
    Silver Moon
    
    http://www.binarytides.com/programming-udp-sockets-in-python/
'''
import time
 
import socket   #for sockets
import sys  #for exit

from client_functions import *

import random



#-----Camera Init-----------
#Import OpenCV
import cv2
#Import Numpy
import numpy as np

import threading


#---------------------------

flag = False

#-----------------------------------------
def clientThread(data_Q,command_Q,varDict):
    # create dgram udp socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print 'Failed to create socket'
        sys.exit()
    
    IP = str(varDict.get("IP"))
    host = IP;
    port = 8888;

    addr_client = False
    
    while(1):
   
        if(addr_client == False):
            print "Enter Position Number of Pi 1-4"
            print "Client will crash if a letter is entered"
            msg = raw_input('Enter Position: ')    
            sendMSG(msg, host, port, s) 
            addr_client = True   
        else: 
            try :
                d = s.recvfrom(1024)
                reply = d[0]
                addr = d[1]
                
                if(reply == "data"):
                    #Here is where we get the data from the queve 
                    data = str(data_Q.get())
                    #data = data.split()
                    #data.pop(0)
                    if(data_Q.empty() != False):
                        print "Sending Data - " +data               
                        s.sendto(data , (host, port))
                    else:
                        print "Data_Q empty"               
                        s.sendto("Queue Empty", (host, port))                        
                    
                elif(reply == "state"):
                    #Here is where we get the data from the queve 
                    flag = data_Q.get().split()
                    print "data to server: " + str(flag[0])
                    s.sendto(str(flag[0]), (host, port)) 
    
                #Server killed the client
                elif(reply == "kill"):
                    print "Client Thread Killed"
                    command_Q.put("kill", 0)               
                    sys.exit()
                    
                else:
                    print "else"
                    command_Q.put(reply, 1) 
                    s.sendto("wait", (host, port))
                
             
            except socket.error, msg:
                print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
                sys.exit()
#--------------------------

from Queue import Queue
data_Queue = Queue()

from Priority_Queue import *
command_Queue = MyPriorityQueue()

import datetime
import time

#testing
from random import randint

import os

path = os.path.dirname(os.path.realpath(__file__))


pathname = os.path.dirname(os.path.realpath(__file__)) + "/config.txt"

# Object that signals shutdown
_sentinel = object()

print "Client Code"

dictVar = generateValueDic(pathname)

thread_client = threading.Thread(target=clientThread, args=(data_Queue,command_Queue,dictVar))

firstRun = True #It's true only the first run, then it is set to false. Prevents problems with starting the thread multiple times
showWindow = False

lower = np.array([50,0,0])
upper = np.array([255,255,255]) 

#Uncomment and implement when Ali finishes the distance calculations
'''
camera_feed = 0
camera_feed = cv2.VideoCapture(0)

while(1):
    flag,frame = camera_feed.read()
    
    if(flag): 
        
        mask = setMask(frame, lower, upper)                  
        bestContour = bestContourCheck(cv2, mask)      
        x,y,w,h = drawShapes(frame, cv2, bestContour)         
        #print x,y,w,h 
        D = calDis(x,y,w,h)
        camDataOut = str(flag) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + " " + str(D)
        
        if(showWindow):
            cv2.waitKey(1)
            imshow(frame, mask) #<<--
        else:
            cv2.destroyAllWindows() 

        data_Queue.put(camDataOut)  
        
        #If the thread has not been started, starts it.
        if(thread_client.isAlive() == False and firstRun == True):
            thread_client.start()
            firstRun = False
        
        
        if(command_Queue.empty() != True):
            command_Q = command_Queue.get()
            print "command_Queue.get(): " + str(command_Q)
            
            if(command_Q == "kill"):
                print "Time to go Bye -- Main Loop"
                break
            
            if(command_Q == "show"):
                showWindow = not(showWindow)
                print "Show Window: " + str(showWindow)
                        
cv2.destroyAllWindows() 


'''

lineNum = 0
while(1):

    #data_Queue.put("f" + " " + "x" + " " + "y" + " " + "w" + " " + "h" + " " + "D")  
    
    if(data_Queue.empty() == True):
        #print "add more"
        #####
        #lineNum += 1 
        #Change fucion, remove split
        txtData = getLine(path + "/dummyData.txt", random.randint(1,9))

        #if(txtData != "null"):
            
        txtData = txtData.split()         
        ts = time.time()       
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H:%M:%S')
        #txtData[6] = st
        dataOut = str(txtData[2] + " " + txtData[4] + " " + st + " " + txtData[8] + " " + txtData[10])

        #else:
            #lineNum = 0

               
        #####
        data_Queue.put(dataOut) 
        
    
    
    #If the thread has not been started, starts it.
    if(thread_client.isAlive() == False and firstRun == True):
        thread_client.start()
        firstRun = False
    
    
    if(command_Queue.empty() != True):
        command_Q = command_Queue.get()
        print "command_Queue.get(): " + str(command_Q)
        
        if(command_Q == "kill"):
            print "Time to go Bye -- Main Loop"
            break
            

print "Done"