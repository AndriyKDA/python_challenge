#*********Poll python exersize************
import os
import csv

#path to colect data from the csv file in the resource folder
path =os.path.join('..//Resources/election_data.csv')

#read in csv file
with open(path, 'r') as pollfile:

    #pass file to csv reader and split the data on commas
    csv_reader = csv.reader(pollfile, delimiter=',')
    #print(csv_reader)
    
    #omit the header row
    csv_header = next(csv_reader)
    
    #create a line count and set it to 0
    line_count = 0
    
    
    #create a list to hold unique candidates names in the rally
    candidates = []
    #create a list to hold value of all set of candidates
    candidate_all = []
    #create list to hold total number of votes for each candidate
    candidates_votes = []
    #create a list to hold percentage of votes for each candidate
    percent_votes = []
    
    #loop through csv file
    for row in csv_reader:
        
       
        #add names of all candidates to the list
        candidate_all.append(row[2])
        
        #calcualte total number of votes as the number of records in the list
        count = int(len(candidate_all))
         
        #add unique candidates names to the candidates list
        if row[2] not in candidates:
           candidates.append(row[2])
        #print(candidates)
           
    #Loop through the unique candiates list name to determine a total number of votes and percentage for each candidate
    for i in range(len(candidates)):
        
        if i == 0:
            count2 = candidate_all.count(candidates[i])
            percent = round((candidate_all.count(candidates[i])/count)*100,2)
        else:
            count2 = candidate_all.count(candidates[i])
            percent = round((candidate_all.count(candidates[i])/count)*100,2)
        
        #Add results to the respective lists    
        candidates_votes.append(count2)
        percent_votes.append(percent)
        
#print number of votes        
print(f"Number of Votes is: {count}", "\n")

#print(candidates)
#print(candidates_votes)
#print(percent_votes)

#create a list to hold values of combined text string 
prin =[]

#loop through candiates list to create a text srting for each  candidtae which will be printed in exported to output.txt
for x in range(len(candidates)):
    
    if x == 0:
        text = (candidates[x])+": "+str(percent_votes[x])+"%, "+ str(candidates_votes[x])
        prin.append(text)
        
    else:
        text = (candidates[x])+": "+str(percent_votes[x])+"%, "+ str(candidates_votes[x])
        prin.append(text)    

#print the results         
print(*prin, sep = "\n")

#find maximum value in the percentage list to determine the winner
maxv = max(percent_votes)   
#print(maxv)

#return name for max percentaged based on list index of max value
winner = candidates[percent_votes.index(maxv)]
print(f"\nThe winner of the rally is: {winner} with {maxv}% of votes" )

#define a path for the output txt file to export the results
path_txt = os.path.join('..//Analysis/Output.txt')

#open the output file, then write the data
with open(path_txt, 'w') as output:
    output.write("Election results:" + "\n")
    output.write("---------------------------" + "\n")
    output.write("Total votes: " + str(count) + "\n")
    output.write("---------------------------" + "\n")
    output.write('\n'.join(prin)+"\n")
    output.write("---------------------------" + "\n")
    output.write("The winner is: " + (winner)+ "\n")
    output.write("---------------------------"+ "\n")






    
