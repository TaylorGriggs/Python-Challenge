# Analysis of Bank System

import os
import csv


# Set path for file
CSV_PATH = os.path.join("Resources", "budget_data.csv")
#Path derived from Dianna in 'Ask-The-Class'
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Set the variables for calculations
rowcount = 0
num_rows = 0
total_rev = 0
previous_revenue = 0
revenue = 0
current_rev = 0

#List creation for sorting
month_list = []
month_change = []

# Open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)
# Count rows in text
    for row in csvreader:
        rowcount += 1
        #Calculate the total revenue through all rows
        revenue = int(row[1])
        total_rev += revenue
        #print("total_rev",total_rev)
        total_change = revenue - previous_revenue 
        previous_revenue = revenue
        #list creation for calculation of ave, min, max
        month_list.append(row[0])
        month_change.append(total_change)
        Ave_Total = sum(month_change)
        Total_Mon = rowcount
    
    #Remove the first month and first value due to starting point
    month_change.pop(0)
    month_list.pop(0)
    Ave_Mon = sum(month_change)/(len(month_change))
     #Greatest increase & greatest decrease
    great_inc = max(month_change)
    great_dec = min(month_change)

print('Financial Analysis')
print("----------------------------")
print("Total Months:" + str(rowcount))
print("Average Change: $" + str(Ave_Mon))
print("Greatest Increase in Profits:" + month_list[month_change.index(great_inc)] + " " +"$" + str(great_inc))
print("Greatest Decrease in Profits:" + month_list[month_change.index(great_dec)] + " " +"$" + str(great_dec))
# Output all calculated values to a file
output_file=os.path.join("analysis", "analysis.txt")
with open(output_file,'w') as file:
    file.write("Financial Analysis")
    file.write('\n'"----------------------------")    
    file.write('\n'"Total Months:" + str(rowcount) )
    file.write('\n'"Total: $" + str(total_rev) )
    file.write('\n'"Average Change: $" + str(Ave_Mon))
    file.write('\n'"Greatest Increase in Profits:" + month_list[month_change.index(great_inc)] + " " +"$" + str(great_inc))
    file.write('\n'"Greatest Decrease in Profits:" + month_list[month_change.index(great_dec)] + " " +"$" + str(great_dec))