# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:24:18 2018
@author: Paul Ag (github name: paulXLV)
"""
import csv

inputfile='election_data.csv'
outputfile='election_output.txt'
# Create empty list for csv file
polls=[]
# Create empty dictionary to record only candidate names
dict_polls={}
# Create empty dictionaty to summarize the total number votes per candidate name
dict_summary={}
# Open file and assign to csvfile object name
with open(inputfile, newline='') as csvfile:
    # read and split the data on commas assign to pollreader string variable
    pollreader=csv.reader(csvfile,delimiter=',')
    # Skip header row
    next(pollreader)
    text_file=open(outputfile,"w")
    # Output to text file
    text_file.write("Election Results")
    # Output to console
    print("Election Results")
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------") 
    # Convert pollreader string to list 
    for line in pollreader:
        polls.append(line)
    # Output to text file
    text_file.write("\nTotal Votes: "+str(len(polls)))
    # Output to console
    print("Total Votes: "+str(len(polls)))
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    # Convert polls list into dictionary for counting and grouping candidate names
    for line in polls:
        name_key=line[2]
        if name_key not in dict_polls:
           # insert name_key into dictionary and initialize to 0
            dict_polls[name_key]=0
        # count the name key inside dictionary
        dict_polls[name_key]+=1
    
    # Compute the percentages of each name key of dict_polls and insert into dict_summary
    total_polls=len(polls)
    for name in dict_polls:
        dict_summary[name]=round((dict_polls[name]/total_polls)*100)
        # Output to text file
        text_file.write("\n"+str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        # Output to console
        print(str(name)+": "+str(dict_summary[name])+"% "+"("+str(dict_polls[name])+")")
        
    # Initialize the highest value to comapre
    highest=0
    # Find larget value of the key/value pair inside dictionary and place the key name inside winner
    for name in dict_summary:
        if highest < dict_summary[name]:
            highest=dict_summary[name]
            winner=name
            
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    # Output to text file
    text_file.write("\nWinner: "+winner)
    # Output to console
    print("Winner: "+winner)
    # Output to text file
    text_file.write("\n-------------------------")
    # Output to console
    print("-------------------------")
    
# Close text file
text_file.close()

'''
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Khan: 63.000% (2218231)
Correy: 20.000% (704200)
Li: 14.000% (492940)
O'Tooley: 3.000% (105630)
-------------------------
Winner: Khan
-------------------------
'''