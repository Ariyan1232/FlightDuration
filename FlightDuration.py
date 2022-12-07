import matplotlib.pyplot as plt
import numpy as np
#Imported Matplotlib libraries

myDataFile = open("JFKTakeoff.csv") #Opened the data set which included my csv

headerString = myDataFile.readline()


#reads the first line of the file and saves in our variable
headerList = headerString.split(",")
data = []

#Allows each row of the CSV file to be read and stored in a list
for line in myDataFile.readlines():

    column = line.replace("\n","")
    column = column.split(",")

    #a list of each column in an individual row
    print(column)
    data.append(column)

#Creates an empty list
LAX = []
MCO = [] 
ATL = [] 
BOS = [] 
DFW = []
CHS = []
IAH = []
SFO = []
DEN = []
MIA = []
ORD = []

for row in range(1, len(data)-1): #1 --> Starts the data on the specific row, -1 --> one less than the length of data
    if data[row][5] == "LAX":  #If the value in column 5 is equal to "LAX" then...
        LAXinfo = (int(data[row][6]) + int(data[row][7])) #Adds the values of column 7 and 8 when the destination is LAX
        LAX.append(LAXinfo) # Adds the values received in line 39 to the list
        average1 = sum(LAX)/len(LAX) # Divides the sum of the values in the list LAX by the number of values in the list
        round1 = round(average1, 2) # Rounds the number received to two decimal points
        print(round1) #Prints the average of the data collected in the list LAX
#This process is repeated 10 more times to gather data for other destinations

for row in range(1, len(data)-1): 
    if data[row][5] == "MCO": 
        MCOinfo = (int(data[row][6]) + int(data[row][7])) 
        MCO.append(MCOinfo) 
        average2 = sum(MCO)/len(MCO)
        round2 = round(average2, 2)
        #print(round2)

for row in range(1, len(data)-1): 
    if data[row][5] == "ATL":  
        ATLinfo = (int(data[row][6]) + int(data[row][7])) 
        ATL.append(ATLinfo) 
        average3 = sum(ATL)/len(ATL)
        round3 = round(average3, 2)
        #print(round3)

for row in range(1, len(data)-1): 
    if data[row][5] == "BOS":  
        BOSinfo = (int(data[row][6]) + int(data[row][7])) 
        BOS.append(BOSinfo) 
        average4 = sum(BOS)/len(BOS)
        round4 = round(average4, 2)
        #print(round4)

for row in range(1, len(data)-1): 
    if data[row][5] == "DFW":  
        DFWinfo = (int(data[row][6]) + int(data[row][7])) 
        DFW.append(DFWinfo) 
        average5 = sum(DFW)/len(DFW)
        round5 = round(average5, 2)
        #print(round5)

for row in range(1, len(data)-1): 
    if data[row][5] == "CHS":  
        CHSinfo = (int(data[row][6]) + int(data[row][7])) 
        CHS.append(CHSinfo) 
        average6 = sum(CHS)/len(CHS)
        round6 = round(average6, 2)
        #print(round6)

for row in range(1, len(data)-1): 
    if data[row][5] == "IAH":  
        IAHinfo = (int(data[row][6]) + int(data[row][7])) 
        IAH.append(IAHinfo) 
        average7 = sum(IAH)/len(IAH)
        round7 = round(average7, 2)
        #print(round7)

for row in range(1, len(data)-1): 
    if data[row][5] == "SFO":  
        SFOinfo = (int(data[row][6]) + int(data[row][7])) 
        SFO.append(SFOinfo) 
        average8 = sum(SFO)/len(SFO)
        round8 = round(average8, 2)
        #print(round8)

for row in range(1, len(data)-1): 
    if data[row][5] == "DEN": 
        DENinfo = (int(data[row][6]) + int(data[row][7])) 
        DEN.append(DENinfo) 
        average9 = sum(DEN)/len(DEN)
        round9 = round(average9, 2)
        #print(round9)

for row in range(1, len(data)-1): 
    if data[row][5] == "MIA":  
        MIAinfo = (int(data[row][6]) + int(data[row][7])) 
        MIA.append(MIAinfo) 
        average10 = sum(MIA)/len(MIA)
        round10 = round(average10, 2)
        #print(round10)

for row in range(1, len(data)-1): 
    if data[row][5] == "ORD":  
        ORDinfo = (int(data[row][6]) + int(data[row][7])) 
        ORD.append(ORDinfo) 
        average11 = sum(ORD)/len(ORD)
        round11 = round(average11, 2)
        #print(round11)

fig, ax = plt.subplots()

cities = ['Los Angeles', 'Orlando', 'Atlanta', 'Boston', 'Dallas', 'Charleston', 'Houston', 'San Francisco', 'Denver', 'Miami', 'Chicago']  #X-Axis Labels
counts = [round1, round2, round3, round4, round5, round6, round7, round8, round9, round10, round11] #Y-Axis Values
bar_labels = ['LAX', 'MCO', 'ATL', 'BOS', 'DFW', 'CHS', 'IAH', 'SFO', 'DEN', 'MIA', 'ORD'] # Legend labels (Will sit beside the colour they represent)
bar_colors = ['tab:red', 'tab:blue', 'tab:pink', 'tab:orange', 'tab:olive', 'tab:brown', 'tab:cyan', 'tab:gray', 'tab:purple', 'tab:green', 'k'] # Bar colours on the graph

ax.bar(cities, counts, label=bar_labels, color=bar_colors) #Calls for the lists to be displayed

ax.set_ylabel('Time (min)') #Y-Axis Label
ax.set_title('Average Time To Reach Destination From JFK Airport') #Graph Title
ax.legend(title='Destination') #Legend Title

plt.show() #Shows the graph