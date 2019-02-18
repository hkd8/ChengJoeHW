#IMPORTS AND PATHS
from statistics import mean
import os
import csv
csvpath = "C:\\Users\\cheng\\Desktop\\UKED201811DATA5\\02-Homework\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv"
with open(csvpath, newline='') as csvfile:

    #CSV READERS skip that header 
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    csvlist = list(csvreader)

    #creating blank lists to store the values obtained from the data
    dates = []
    revenues = []
    
    #LOOP for rows 
    for x in csvlist:
        dates.append(x[0])
        revenues.append(int(x[1]))
    
    #Blank list for revenue change between months 
    revCHANGE = []

    #LOOP for each change between months
    revCHANGE = [revenues[i+1] - revenues[i] for i in range(len(revenues) -1)]
    
    #MORE VARIABLES MORE PROBLEMS
    maxCHANGE = max(revCHANGE)
    worstLOSS = min(revCHANGE)
    totalNET = sum(revenues)
    avgCHANGE = round(mean(revCHANGE), 2)
    totalMONTH = len(dates)
    maxMONTH = None
    worstMONTH = None
    
    #LOOP to find specific DATES, setting OGval as a base
    OGval = None
    for row in csvlist:
        if OGval is None:
            OGval = int(row[1])
            continue
        if int(row[1]) - OGval == worstLOSS:
            worstMONTH = row[0]
        OGval = int(row[1])

    OGval2 = None
    for row in csvlist:
        if OGval2 is None:
            OGval2 = int(row[1])
            continue
        if abs(int(row[1]) - OGval2) == maxCHANGE:
            maxMONTH = row[0]
        OGval2 = int(row[1])
    
    #take note of use of the ":," function to turn results with commas 
    print("Financial Analysis")
    print("-----------------------------------------------------------------------------")
    print(f"Total Months: {totalMONTH}")
    print(f"Total: (${totalNET:,})")
    print(f"Average Change: (${avgCHANGE:,})")
    print(f"Greatest Increase in Profits: {maxMONTH} (${maxCHANGE:,})")
    print(f"Greatest Decrease in Profits: {worstMONTH} (${worstLOSS:,})")
    
    #creating text file, note w+ to signify if there is no file named, CREATE one
    f=open("PyBankRESULTS.txt","w+")

    #TAKE note of \n to signify go to next line
    f.write("Financial Analysis\n")
    f.write("-----------------------------------------------------------------------------\n")
    f.write(f"Total Months: {totalMONTH}\n")
    f.write(f"Total: (${totalNET:,})\n")
    f.write(f"Average Change: (${avgCHANGE:,})\n")
    f.write(f"Greatest Increase in Profits: {maxMONTH} (${maxCHANGE:,})\n")
    f.write(f"Greatest Decrease in Profits: {worstMONTH} (${worstLOSS:,})\n")

#MOMMA WE MADE IT
    f.close()