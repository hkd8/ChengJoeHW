#ALL I DO IS IMPORT
import csv
import os
csvpath = 'C:\\Users\\cheng\\Desktop\\UKED201811DATA5\\02-Homework\\03-Python\\Instructions\\PyPoll\\Resources\\election_data.csv'
with open(csvpath, 'r') as csvfile:

#READERS AND SKIP THAT HEADER
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

#MAKING MY BLANK LISTS DOWNTOWN WALKING FAST 
    candidate = [] 
    votes = []
    name = []
#storing the candidate data
    for row in csvreader:
        candidate.append(row[2])
    candidateCOUNT = [[x,candidate.count(x)] for x in set(candidate)]
   
    for row in candidateCOUNT:
        name.append(row[0])
        votes.append(row[1])

#Using ZIP function, combining name to votes to get a count
    candidateZIP = zip(name, votes)
    candidateLIST = list(candidateZIP)

#winner winner chicken dinner using max function to find who had most 
    winner = max(votes)

#matching most votes to a name
    for row in candidateLIST:
        if row[1] == winner:
            winnerNAME = row[0]   

#using LENGTH to count each vote           
voteTOTAL = len(candidate)

#making candidate totals 
correyTOTAL = candidate.count('Correy')
correyPERCENT = int(correyTOTAL) / int(voteTOTAL)

otooleyTOTAL = candidate.count("O'Tooley")
otooleyPERCENT = otooleyTOTAL / voteTOTAL

liTOTAL = candidate.count('Li')
liPERCENT = liTOTAL / voteTOTAL

khanTOTAL = candidate.count('Khan')
khanPERCENT = khanTOTAL / voteTOTAL

#note using .3% to get to 3 decimals 
print(f'Election Results')
print(f'-----------------------------')
print(f'Total Votes: {voteTOTAL}')
print(f'-------------------------------')
print(f'Khan: {khanPERCENT:.3%} ({khanTOTAL:,})')
print(f'Correy: {correyPERCENT:.3%} ({correyTOTAL:,})')
print(f'Li: {liPERCENT:.3%} ({liTOTAL:,})')
print(f"O'Tooley: {otooleyPERCENT:.3%} ({otooleyTOTAL:,})")
print(f'-----------------------------')
print(f'Winner: {winnerNAME}')
print(f'----------------------------')

#we making more texts
f=open("PyRollRESULTS.txt","w+")

f.write(f'Election Results\n')
f.write(f'-----------------------------\n')
f.write(f'Total Votes: {voteTOTAL:,}\n')
f.write(f'-------------------------------\n')
f.write(f'Khan: {khanPERCENT:.3%} ({khanTOTAL:,})\n')
f.write(f'Correy: {correyPERCENT:.3%} ({correyTOTAL:,})\n')
f.write(f'Li: {liPERCENT:.3%} ({liTOTAL:,})\n')
f.write(f"O'Tooley: {otooleyPERCENT:.3%} ({otooleyTOTAL:,})\n")
f.write(f'--------------------------------\n')
f.write(f'Winner: {winnerNAME}\n')
f.write(f'--------------------------------\n')

#MOMMA WE MADE IT 2.0
f.close()