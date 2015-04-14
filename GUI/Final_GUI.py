from Tkinter import *
#import ttk
#READ: http://www.python-course.eu/tkinter_entry_widgets.php
from turtle import *
from random import randint
import math

import random 
import math

import collections

#*****************************************************************************************************************
class Result(Frame):
    ##-------------------
        #Note: when making functions iside Class you have to include the self param, but when you are calling them you don't inlucde the self param.
         
    
    #this can be considered the constructor
        def __init__(self, master, dataTxt, guiDim, guiTitle):
            
            Frame.__init__(self, master)
            self.parent = master
            
            self.data = dataTxt
        
            self.parent.geometry(guiDim)       
            self.parent.title(guiTitle)                      
            self.ResultGUI(dataTxt)
            
            self.HistogramButtonPressed = False

    
        def ResultGUI(self, fieldTxt):
            xyFrame = Frame(self, relief=RAISED, borderwidth=1, bg='blue')
            xyFrame.pack(fill=Y, expand=1)
            
            XY_cords = PanedWindow(xyFrame, orient=VERTICAL, bg='red')
            #XY_cords.pack(fill=X,side=TOP, expand=1)
            XY_cords.pack(side=TOP)
                    
            #XY_cords_Label = PanedWindow(XY_cords, orient=HORIZONTAL, bg='black')
            #XY_cords_Label.pack(side = TOP)
            #XY_cords_Label.add(Label(XY_cords_Label, text="X-Cord", bg='yellow'))         
            #XY_cords_Label.add(Label(XY_cords_Label, text="Y-Cord", bg='orange'))         
            
    ##########################
            PointBox = Listbox(XY_cords,bg='grey')
            MessageBox_X = Listbox(XY_cords,bg='grey')
            MessageBox_Y = Listbox(XY_cords,bg='grey')
            
            PointBox.pack(side=LEFT)
            MessageBox_X.pack(side=LEFT)
            MessageBox_Y.pack(side=LEFT)
            
            PointBox.insert(0, "point")
            MessageBox_X.insert(0, "Actual Cords")
            MessageBox_Y.insert(0, "Error Cords")
            
            PointBox.insert(1, "----------------")
            MessageBox_X.insert(1, "----------------")
            MessageBox_Y.insert(1, "----------------")
            
            point = 0
            ActualCord = []
            ErrorCord = []
            cordListOrdered = []
            
            
            
            for i in range(len(self.data)):   
                    for key, value in sorted(self.data[i].items()):
                            #print('%s: "%s"' % (key, value))
                    
                            if key == "Point":
                                    point = value
                            if key == "ActualCord":
                                    x,y = value
                                    x = round(x,2)
                                    y = round(y,2)   
                                    ActualCord = [x,y]
                            if key == "ErrorCord":
                                    x,y = value
                                    x = round(x,2)
                                    y = round(y,2)
                                    ErrorCord = [x,y]

                    PointBox.insert(i+2, point)
                    MessageBox_X.insert(i+2, ActualCord)
                    MessageBox_Y.insert(i+2, ErrorCord)                    

            self.pack(fill=BOTH, expand=1)
            closeButton = Button(self, text="Close", command=self.quit)#Exits the program
            closeButton.pack(side=RIGHT, padx=5, pady=5)
            
            HistogramButton = Button(self, text="Histogram", command=self.histogramLaunch)#Exits the program
            HistogramButton.pack(side=LEFT, padx=5, pady=5)

        def histogramLaunch(self):
                
                pointArray = []
                ActualLengthArray = []
                ErrorLengthArray = []
                
                for i in range(len(self.data)):   
                        for key, value in sorted(self.data[i].items()):
                                #print('%s: "%s"' % (key, value))
                        
                                if key == "Point":
                                        point = value
                                if key == "ActualLength": 
                                        ActualLength = value
                                if key == "ErrorLength":
                                        ErrorLength = value
                        
                        #print "point", point
                        #print "ActualCord" ,ActualLength
                        #print "ErrorCord" , ErrorLength
                        pointArray.insert(i,point)
                        ActualLengthArray.insert(i,ActualLength)
                        ErrorLengthArray.insert(i,ErrorLength)
                        
                #print pointArray
                #print ActualLengthArray
                #print ErrorLengthArray
                       
                import numpy as np
                import matplotlib.pyplot as plt
                
                actual = ActualLengthArray
                error = ErrorLengthArray
                pointArray = pointArray
                
                #actual = [20, 45, 30, 35]
                #error = [10, 32, 34, 20]
                #pointArray = [0, 1, 2, 3]
                
                print type(actual)
                
                n_groups = len(actual)
                
                fig, ax = plt.subplots()
                
                index = np.arange(n_groups)
                
                bar_width = 0.35
                
                opacity = 0.4
                error_config = {'ecolor': '0.3'}
                
                rects1 = plt.bar(index, actual, bar_width,color='b',alpha=opacity,label='Actual')
                rects2 = plt.bar(index+ bar_width, error, bar_width,color='r',alpha=opacity,label='Error')
                
                
                plt.xlabel('Point Number')
                plt.ylabel('Value Direvation')
                plt.title('Histogram')
                plt.xticks(index + bar_width, pointArray)
                plt.legend()
                plt.tight_layout()
                plt.show()
                
                self.quit()

    ##########################
    #*****************************************************************************************************************
class Setup(Frame):
##-------------------
    #shapeRadioTxt = [("Polygon",1),("Star Mode 1",2),("Star Mode 2",3),]   
    shapeRadioTxt = [("Polygon",1),]
    colorRadioTxt = [("Yellow",1),("Blue",2),("Black",3),] 
  
    #Note: when making functions iside Class you have to include the self param, but when you are calling them you don't inlucde the self param.   
    def makeform(self, root, fields):
        entries = []
        for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            self.c_var = IntVar()
            ent = Entry(row, textvariable=self.c_var)
            
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
        return entries

    def list_to_dict(self, listIN):
        for entry in listIN:
            field = entry[0]
            text  = entry[1].get()
            self.dataDic[field] = text

    def SetPolygonChoice(self):
        index = self.polygonVar.get()
        txt, val = self.shapeRadioTxt[index-1]
        self.dataDic['type'] = txt
        
#this can be considered the constructor
    def SetColorChoice(self):
        index = self.colorVar.get()
        txt, val = self.colorRadioTxt[index-1]
        self.dataDic['Color'] = txt
        
        
    def __init__(self, master, labels, guiDim, guiTitle):
        
        Frame.__init__(self, master)
        self.parent = master      
        self.data = [] 
        self.dataDic = {}
        
        self.optionButton = []
        
        self.polygonVar = IntVar()
        
        self.colorVar = IntVar()

        self.closeButton = Button() 
        
        self.parent.geometry(guiDim)       
        self.parent.title(guiTitle)
        
        #self.closeButton.config(state="disabled")
        
        self.buttonFrame = Frame(self)
        
        #self.radioFrame = PanedWindow(self)
        
        self.SetupGUI(labels) 
        
        self.setupComplete = False
        
    

#Initializes the Gui
    def SetupGUI(self, fieldTxt):

        #self.buttonFrame.config(relief=RAISED)
        #self.buttonFrame.config(borderwidth=1)
        #self.buttonFrame.config(bg='blue')       
        self.buttonFrame.pack(fill=BOTH, expand=1)
        
        
        #self.radioFrame.config(orient=VERTICAL)
        #self.radioFrame.pack(fill=BOTH, expand=1)
        #self.radioFrame.config(bg='red')
        #self.radioFrame.pack(expand=1)

        #addas the fields
        ents = self.makeform(self.buttonFrame, fieldTxt)
        self.data = ents
        
        #Radio buttons HOR
        for txt, val in self.colorRadioTxt:
                
            self.colorButton = Radiobutton(self.buttonFrame)     
            self.colorButton.config(text=txt)
            self.colorButton.config(indicatoron = 0)
            self.colorButton.config(width = 4)
            #self.colorButton.config(padx = 20)
            self.colorButton.config(variable=self.colorVar)
            self.colorButton.config(command=self.SetColorChoice)
            self.colorButton.config(value=val)
            self.colorButton.pack(side=LEFT)
            
            self.optionButton.append(self.colorButton)

        '''
        #Radio buttons VER
        for txt, val in self.shapeRadioTxt:
                
            self.R2 = Radiobutton(self.radioFrame)     
            self.R2.config(text=txt)
            self.R2.config(indicatoron = 0)
            self.R2.config(width = 20)
            self.R2.config(padx = 20)
            self.R2.config(variable=self.polygonVar)
            self.R2.config(command=self.SetPolygonChoice)
            self.R2.config(value=val)
            self.R2.pack(side=TOP)
            
            self.optionButton.append(self.R2)
            '''       
        
        #print len(self.optionButton)
        
        self.pack(fill=BOTH, expand=1)               
        self.closeButton.config(text="Save and Continue")
        self.closeButton.config(command=self.OnChildClose)
        self.closeButton.pack(side=TOP, padx=5, pady=5)

    def OnChildClose(self):
        #self.closeButton.config(state="disabled")
        self.list_to_dict(self.data)
        
        #disables buttons
#        for i in xrange(len(self.optionButton)):
#             self.optionButton[i].config(state="disabled")
 
        self.setupComplete = True
        
        self.closeButton.destroy()
        self.quit()


#*****************************************************************************************************************

   


class Polygon():
        
        ########################################################
        def polygon(self, n=4, length=100):  #predefined  n=4, lenght=100
            angle = 360.0/n
            for i in range(n):
                car.fd(length)
                car.lt(angle)
        ########################################################
        def randomError(self, value, randomRange):
            #randNum = random.uniform(-10, 10)
            random.seed(10)
            randNum = random.randint(-randomRange, randomRange)
            #randNum = random.randrange(-10,10)
            error = value+randNum
            errorRounded = error
            return errorRounded
        ########################################################
        #Length
        def randomLength(self, value, randomRange):
            #randNum = random.uniform(-10, 10)
            randNum = random.randint(-randomRange, randomRange)
            #randNum = random.randrange(-10,10)
            error = value+randNum
            return error
        ########################################################
        #Angle
        def randomAngle(self, value, randomRange):
            #randNum = random.uniform(-10, 10)
            randNum = random.randint(-randomRange, randomRange)
            #randNum = random.randrange(-10,10)
            error = value+randNum
            rounded = error
            rounded = round((error/100), 1)
            rounded = rounded * 100
            #print 'error' , error , ',' , 'error rounded' , rounded
        
            return rounded
        ########################################################
        def distanceCalc(self, x1,y1,x2,y2):
            #print '          ' , 'X' , ',' , 'Y'
            #print 'first cord' ,  x1 , ',' , y1
            #print 'last cord ' ,  x2 , ',' , y2
            noErrorDistance = math.sqrt((math.pow((x2-x1),2))+(math.pow((y2-y1),2)))
            #print noErrorDistance  
            return noErrorDistance  
        ########################################################
        def percentDiference(self, v1,v2):
            v1 = float(v1)
            v2 = float(v2)
            errorPercent = (abs(v1-v2)/((v1+v2)/2))*100
            errorPercent = round(errorPercent,2)
            return errorPercent
        ########################################################
        def drawPolygon(self, obj, angle, lengthSide, lineColor, txtAlign, txt):
            obj.pd # pen ON screen - Line
            obj.color(lineColor)
            obj.fd(lengthSide)
            obj.lt(angle)
            obj.write(txt, False, align=txtAlign, font = ("Ariel", 9, "normal"))
        ########################################################
        def drawPolygonLoop(self, obj, sidesNum, sidesLength, lengthErrorRange, angleErrorRange, color, txtAlign):
            angle = 360.0/sidesNum
            xy = [0,0,0,0]
            cords = []
            for i in range(sidesNum): 
                errorLength = self.randomLength(sidesLength, lengthErrorRange)
                errorAngle = self.randomAngle(angle, angleErrorRange)
                xy = [obj.xcor(), obj.ycor(),errorLength,errorAngle]
                cords.insert(i, xy)   
                
                #x = round(obj.xcor(),2)
                #y = round(obj.ycor(),2)
                #txt = x,y
                txt = i
                
                if lengthErrorRange == 0 | angleErrorRange == 0:
                    self.drawPolygon(obj, angle, sidesLength, color, txtAlign, txt)  
                else:
                    self.drawPolygon(obj, errorAngle, errorLength, color, txtAlign, txt)  
           
            return cords
        ########################################################
        def draw(self, dictionaryData):
                
            car = Turtle() #turtle created
            
            #-------------------------------------------------------
            #this section gets the passed vals from setup
            numSides = 6   #<
            length = 80    #<
            angleErrorRange = 0
            lengthErrorRange = 0
            color = 'blue' #<
            #-------------------------------------------------------

            for key, value in sorted(dictionaryData.items()):
                    print key, "-- ", value 
                    if(key == "Number of Sides"):
                         numSides = int(value)
                    if(key == "Length of Sides"):
                         length = int(value)
                    if(key == "Color"):
                         color = value
   
            
            cordNoError = self.drawPolygonLoop(car, numSides, length, lengthErrorRange, angleErrorRange, color, "left")
            
            
            ############################
            #Takes the list from drawPolygonLoop and separates it into 4 diferent lists, makes easier the calculations
            xCord_noError = []
            yCord_noError = []
            length_noError = []
            angle_noError = []
            for i in range(numSides):
                element = cordNoError[i]
                #print 'element - ' , i , element
                xCord_noError.insert(i, element[0])
                yCord_noError.insert(i, element[1])
                length_noError.insert(i, element[2])
                angle_noError.insert(i, element[3])
            ############################
            
            #-------------------------------------------------------
            #this section gets the passed vals from setup
            angleErrorRange = 10 #+/- degree resolution
            lengthErrorRange = length * .10 #gets the percentage range for the length
            color = 'red'
            #-------------------------------------------------------
            
            cordError = self.drawPolygonLoop(car, numSides, length, lengthErrorRange, angleErrorRange, color, "right")
            ############################
            #Takes the list from drawPolygonLoop and separates it into 4 diferent lists, makes easier the calculations
            xCord_Error = []
            yCord_Error = []
            length_Error = []
            angle_Error = []
            for i in range(numSides):
                element = cordError[i]
                #print 'element - ' , i , element
                xCord_Error.insert(i, element[0])
                yCord_Error.insert(i, element[1])
                length_Error.insert(i, element[2])
                angle_Error.insert(i, element[3])
            ############################
            
            #Calculations of the errors.
            
            totalPerimeterNoError = 0;
            totalPerimeterError = 0;
            
            dataList = []
            
            for i in range(numSides):
                x = xCord_noError[i]
                y = yCord_noError[i]
                xError = xCord_Error[i]
                yError = yCord_Error[i]      
                distance = self.distanceCalc(x,y,xError,yError)
                
                angleNoError = angle_noError[i]
                angleError = angle_Error[i]
                angleDiference = angleError-angleNoError
                
                lengthError = length_Error[i]
                lengthNoError = length_noError[i]
                lengthPercentDiference = self.percentDiference(lengthError,lengthNoError)
                
                totalPerimeterNoError = totalPerimeterNoError + lengthNoError
                totalPerimeterError = totalPerimeterError + lengthError
               
                #print 'pt' , i, 'Coordinates No Error->[x,y]' , '[',round(x, 3),',', round(y, 3),']'
                #print '                 Error---->[x,y]' , '[',round(xError, 3),',', round(yError, 3),']'
                #print 'Distance from "ideal" cord to "actual" cord ->' , round(distance, 4)
                #print 'Ideal Angle  ->' , angleNoError , '--Actual Angle  ->' , angleError , '--Angle diference  ->' , angleDiference
                #print 'Ideal Length ->' , lengthNoError , '--Actual Length ->' , lengthError , '--Length Error Percent ->' , lengthPercentDiference, '%'
                #print '------------------------------------------------------------------------'

                dataDic = {}
                dataDic['Point'] = i
                dataDic['ActualCord'] = [x,y]
                dataDic['ErrorCord'] = [xError,yError]
                dataDic['ActualAngle'] = angleNoError
                dataDic['ErrorAngle'] = angleError
                dataDic['AngleDiference'] = angleDiference
                
                dataDic['ActualLength'] = lengthNoError
                dataDic['ErrorLength'] = lengthError
                dataDic['lengthPercentDiference'] = lengthPercentDiference
                
                #orderedDic = collections.OrderedDict(sorted(dataDic.items()))
                

        
                dataList.append(dataDic)
            
            #print 'Total Perimeter Distance with NO error---->' , totalPerimeterNoError
            #print 'Total Perimeter Distance with ERROR------->' , totalPerimeterError
            #print 'Percent diference Between the two lengths->' , self.percentDiference(totalPerimeterNoError,totalPerimeterError),'%'
                
            
           
            return dataList
                    
                    
            #create a dict with the info that we are prinitng.
            #create a dict with the X,Ys for the histogram, with perfet poly cords and irregular cords.
            
        
            
            #exitonclick()    
            
        ##MAin
########################################################

                
                
#simple function to call the class that returns the values, notice the syntax
def setupScreen(dat, dim, titt):
    root = Tk()
    cl = Setup(root, dat, dim, titt)   
    root.mainloop()
    return cl
   
def resultScreen(dat, dim, titt):
    root = Tk()
    cl = Result(root, dat, dim, titt)
    root.mainloop()
    return cl

def drawScreen():
    print 'drawScree Def'
    dr = Polygon()
    return dr




#//------------------//
#this is what we are feeding the class
data = 'Number of Sides', 'Length of Sides'
dim = '300x150+100+100'
title = "FAU Robot Setup"


#this is the data that the class retirned
returnedData = setupScreen(data, dim, title)

#main loop

setupDic = returnedData.dataDic

#print 'setupDic = ' ,setupDic

dim = '350x200+100+420'
title = "FAU Robot Result"

polygonDic = {}

if(returnedData.setupComplete == True):
        #we pass a dictionary with the selections from setup screen
        #and it returns another dictionary with the results
        polygonList = drawScreen().draw(setupDic)
        
        resultScreen(polygonList, dim, title)        
elif(returnedData.setupComplete == True):
        print "error, closed without params" 



#%matplotlib inline #Usefull