'''
    Simple udp socket server
    Silver Moon (m00n.silv3r@gmail.com)
'''
import time

import socket
import sys

from server_functions import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 8888 # Arbitrary non-privileged port
 
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
 
# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 


client_addr_array = []
iteration = 1

pos = 0

while 1:
    #usserIn = raw_input('Enter Command : ')
    command = raw_input('Enter Command : ').split()
    
    client_addr_array = Kill(command[0], client_addr_array, s) 
       
    if(command[0] == "add"):
        client_addr_array = add(client_addr_array, s)
       
    elif(command[0] == "exit"):
        exit("exit", client_addr_array, s)
    
    elif(command[0] == "loop"):
        #get size of array <-----------
        for x in range(len(client_addr_array)):
            print "Data - " + str(x) + " - " + str(client_comm("data",x, client_addr_array, s))
            #Position Calc probably goes here - Waiting Ali
            
    elif(command[0] == "data_loop"):
        
        for index in range(len(client_addr_array)):
            
            while(True):
                received_Data = client_comm("data",index, client_addr_array, s)

                piPos = received_Data[0]
                piData = received_Data[1].split()
    
                Robot_Found = piData[0]
                Computation_Done = piData[1]
                Time_Stamp = piData[2]
                Distance_Robot = piData[3]
                Angle_to_robot = piData[4] 

                if(int(Robot_Found) == 0 and int(Robot_Found) == 0):
                    print "Position of Pi: " +str(piPos) + " | Found: " + str(Robot_Found) + " | Computation: " + str(Computation_Done) + " | Time: " + str(Time_Stamp) + " | data not good"  
                    time.sleep(2)
                elif(int(Computation_Done) == 0 and int(Robot_Found) == 1):
                    print "Position of Pi: " +str(piPos) + " | Found: " + str(Robot_Found) + " | Computation: " + str(Computation_Done) + " | Time: " + str(Time_Stamp) + " | data not good"  
                    time.sleep(2)
                if(int(Robot_Found) == 1 and int(Robot_Found) == 0):
                    print "Position of Pi: " +str(piPos) + " | Found: " + str(Robot_Found) + " | Computation: " + str(Computation_Done) + " | Time: " + str(Time_Stamp) + " | data not good"
                    time.sleep(2)
                elif(int(Computation_Done) == 1 and int(Robot_Found) == 1):                    
                    print "Position of Pi: " +str(piPos) + " | Found: " + str(Robot_Found) + " | Computation: " + str(Computation_Done) + " | Time: " + str(Time_Stamp) + " | Distance: " + str(Distance_Robot) + " | Angle: " + str(Angle_to_robot)                 
                    break
            
        print "Finished Pulling Data from: " + str(client_addr_array) 
   
   
#--------------------------------------------------------------
    if(len(command) > 1):
        pos = command_to_index(command[1])
        com = command[0]

        client_Data = client_comm(com,pos, client_addr_array, s)
        
        if(str(com) == "data"):
            print "raw " + str(com) + ": " + str(client_Data)
        else:
            print str(com) + ": " + str(client_Data)
#--------------------------------------------------------------


s.close()

