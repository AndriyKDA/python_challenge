
#*********PyBank python exersise************
import os
import csv

#path to colect data from the csv file in the resource folder
path = '/Users/ak/Documents/DA/Python/python_challenge/PyBank/Resources/budget_data.csv'

#read in csv file
with open(path, 'r') as bankfile:

    #pass file to csv reader and split the data on commas
    csv_reader = csv.reader(bankfile, delimiter=',')
    print(csv_reader)
    
    #ommit the header row
    csv_header = next(csv_reader)
    
    #create a line count and set it to 0
    line_count = 0
    #define a total amount as zero
    net_total_amount = 0
    
    #create a list to hold monthly profit/loss values
    monthly_value = []
    
    
    for row in csv_reader:
        line_count +=1
        net_total_amount += int(row[1])
        monthly_value.append(int(row[1]))
        #monthly_value2.append(row[1])
        

print(f" Total Months: {line_count}")
print(f" Net Total Amount: {net_total_amount}")
#print(monthly_value)
#print(monthly_value2)

monthly_var = []
#write a function to loop through the list indexes and calulate the difference
def monthly_change(monthly_value):
    
    for i in range(len(monthly_value)):
    
        #set a condition to make sure indexes are within the range
        if i >= 0 and i <= 84: #int(net_total_amount)-2:
        
            #fundtion argument
            change = monthly_value[i+1] - monthly_value[i]
            monthly_var.append(change)
            print(change)
    
# call the function
monthly_change(monthly_value)
print(monthly_change)

average = sum(monthly_var)/len(monthly_var)
print(f" the average change for the period is {average}")

    
       
     







