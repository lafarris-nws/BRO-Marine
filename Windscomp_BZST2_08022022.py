#Accessing a text file - BZST2_May.txt
#Script to ...
#Author: Laura Farris
#Updated: 8/02/2022

# import numpy as np
# import pandas as pd

# file = open("BZST2_windscomp_08022022.csv","r")
# skipheaderdata = pd.read_csv("BZST2_windscomp_08022022.csv", skiprows=3)
# print(skipheaderdata)

from itertools import islice

with open("BZST2_winds_0802022.txt") as f:
  # start reading from line 4
  for line in f:
    print(line)

# creating empty lists to be filled in for loop

day = []
hr = []
mn = []
wdir = []
wspd = []
wgst = []
wtmp = []


#Repeat for each row of data in the text file
for line in skipheaderdata:
  
  #Let's split the line into an array called "fields" using the "," as a separator:
  fields = line.split(",")
  fields = np.where(fields=="M", np.nan, fields)

  #Filling the placeholder lists for desired variables:
#  day.append(fields[2])
#  hr.append(fields[3])
#  mn.append(fields[4])
#  wdir.append(float(fields[5]))
  wspd.append(float(fields[6]))
#  wgst.append(float(fields[7]))
#  wtmp.append(float(fields[14]))

print(wspd)

#It is good practice to close the file at the end to free up resources   
skipheaderdata.close()
