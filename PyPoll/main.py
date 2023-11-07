

import os
import csv

#Set path for files
csv_path = os.path.join("Resources", "election_data.csv")
#Path derived from Dianna in 'Ask-The-Class'
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Set variables calculations
total_votes = 0
winner_count = 0
winner_percentage = 0

#Set lists for sorting and calculations
candidate_list = []
candidate_count = {}

winner = ""
# Open the CSV using the UTF-8 encoding
with open(csv_path, encoding='UTF-8') as csv_file:
    csvreader = csv.reader(csv_file)
    next(csvreader, None)
    
    #Loop Through Data
    for row in csvreader:
        
        #Count Total Votes
        total_votes += 1

        #Candidate Data 
        candidate_name = row[2]

        #Append List For Candidates Only
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_count[candidate_name] = 0
        
        #End Vote total
        candidate_count[candidate_name] += 1 


#Output Election Results Analysis
print("Election Results")
print("--------------------------")
print("Total votes:" + str(total_votes))
print("--------------------------")

for each_candidate in candidate_count:
    candidate_vote = (candidate_count[each_candidate])
    candidate_percent = float(candidate_vote) / float(total_votes)*100
    if candidate_vote > winner_count:
        winner_count = candidate_vote
        winner = each_candidate
        
        #Nesting in the for loop to get all 3 candidate outputs
    voter_output = (f'{each_candidate} {candidate_percent:.3f}% ({candidate_vote})\n')
    print(voter_output) 

print("--------------------------")
print("Winner:" + " " + winner)
print("--------------------------")

#Create text filed and print analysis to text file
output_file=os.path.join("analysis", "analysis.txt")
with open(output_file,'w') as file:
    #Election results
    file.write("Election Results")
    file.write('\n'"--------------------------")
    file.write('\n'"Total votes:" + str(total_votes))
    file.write('\n'"--------------------------")
    file.write('\n' + voter_output)
    file.write('\n'"--------------------------")
    file.write('\n' + "Winner" + " " + winner)
    file.write('\n'"--------------------------")