
# ---HOW TO USE---
# 
# To run the script place the .csv you want to scrape
# in the same folder with this script file. Then open 
# command line (and navigate to the folder the script 
# and .csv are in) and type: "python ScrapeCSV.py filename"
# where filename is the name of the .csv file.
#

# ---WHERE TO FIND AMD ADRENALINE LOGS
# 
# AMD adrenaline log files by default are found 
# in C:/Users/user/AppData/Local/AMD/CN/ folder, with name 
# Hardware.xxxxxxxx-xxxxxxxx.CSV where the xxxxxxxx-xxxxxxxx
# is the time when the log has ended, such as 20240606-130101. 
#
 
import sys

f = open(str(sys.argv[1]), "r")
data = f.readlines()
currhi = 0

for j in range(1, 17):
    currhi = 0
    for i in range(1, len(data)):
        line = data[i].split(',')
        num = float(line[j])
        
        if num >= currhi:
            currhi = num
            currtime = line[0]
             
    print("Highest ", data[0].split(',')[j], " value: ", currhi, " at ", currtime)

print ("Last recorded time: ", data[len(data) - 1].split(',')[0])    
    