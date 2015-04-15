
import sys

def add(client_addr_array, s):
    addr_array = client_addr_array
    
    print "waiting for a new client"
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]
    
    addr_array.append(d)
    
    txt = "From server: " +str(addr) + " Joined the network - Pos: " + str(data)
    print txt
    s.sendto(txt , addr)    
    return addr_array

def Kill(command, client_addr_array, s):
    addr_array = client_addr_array

    if(command == "kill"):
        for index in range(len(addr_array)):
            print "Index: " + str(index) + str(addr_array[index]) 
        
        print "Server will crash if a Letter is Entered"
        command_index = raw_input('Enter Index to Kill : ')
        
        ind = int(command_index)

        if(ind < len(addr_array)):
            d = addr_array[ind]
            s.sendto("kill" , d[1])
            addr_array.pop(ind)        

              
    if(command == "kill_All" or command == "kill_A"):
        for addr in addr_array:
            s.sendto("kill" , addr[1])
        addr_array = []
    
    
    return addr_array

def exit(command, client_addr_array, s):
    Kill("kill_All", client_addr_array, s)
    print "BYE"
    sys.exit()
    

def broadCast_hi(command, client_addr_array, s):
    if(command == "hi"):
        for d in client_addr_array:
            client_details = d[1]
            txt = "addr: " + str(d[0]) + " - Hi client adress: " + str(client_details[0])
            print txt
            #data = raw_input('Enter message : ')            
            s.sendto(txt , d[1])    

def check_Cam_State(index, client_addr_array, s):
    
        addr_array = client_addr_array[index]
       
        s.sendto("state" , addr_array[1])    
            
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]  
            
        if(data == "False"):
            data = False
        elif(data == "True"):
            data = True
             
        return data


def client_data(index, client_addr_array, s):  
    
        addr_array = client_addr_array[index]
        
        s.sendto("data" , addr_array[1])    
            
        d = s.recvfrom(1024)
        data = d[0]
        addr = d[1]  
        
        data = (addr_array[0], data) 
        #Pos Number, client Info, Data
        return data
    
def client_comm(command, index, client_addr_array, s):  
    addr_array = client_addr_array[index]
    
    s.sendto(command , addr_array[1])    
        
    d = s.recvfrom(1024)
    data = d[0]
    addr = d[1]  
    
    data = (addr_array[0], data) 
    #Pos Number, client Info, Data
    return data    


#Pi position
#Makes it easier, instead of going Position 0 we use Position 1, more natural
def command_to_index(command):

    pos = 0
    
    if(command == "1"):
        pos = 0
    elif(command == "2"):
        pos = 1
    elif(command == "3"):
        pos = 2
    elif(command == "4"):
        pos = 3 
    
    return pos

