
#*********PyBank python exersize************
import os
import csv

#path to colect data from the csv file in the resource folder
path =os.path.join('/Users/ak/Documents/DA/Python/python_challenge/PyBank/Resources/budget_data.csv')

#read in csv file
with open(path, 'r') as bankfile:

    #pass file to csv reader and split the data on commas
    csv_reader = csv.reader(bankfile, delimiter=',')
    #print(csv_reader)
    
    #ommit the header row
    csv_header = next(csv_reader)
    
    #create a line count and set it to 0
    line_count = 0
    
    #define a total amount as zero
    net_total_amount = 0
    
    #create a list to hold monthly profit/loss values
    monthly_value = []
    
    #create a list to hold dates
    date = []
    
    #loop through csv file
    for row in csv_reader:
        
        #calcualte number of rows
        line_count +=1
        
        #calculate total net amount
        net_total_amount += int(row[1])
        
        #add monthly profits/losses to the new list
        monthly_value.append(int(row[1]))
        
        #add monthly dates to the new list
        date.append(row[0])
        
#orint results        
print(f"Total Months: {line_count}")
print(f"Net Total Amount: ${net_total_amount}")


#create a new list to hold monthly variance values
monthly_var = []

#write a function to loop through the list indexes and calulate the monthly difference
def monthly_change(monthly_value, date):
    
    for i in range(len(monthly_value)):
    
        #set a condition to make sure indexes are within the range
        if i >= 0 and i <= int(line_count)-2:
        
            #function argument
            change = monthly_value[i+1] - monthly_value[i]
            
            #add formula values to the list
            monthly_var.append(change)
            #print(change)
        
# call the function
monthly_change(monthly_value, date)
#print(monthly_change)


#caluclating average variance value
average = round(sum(monthly_var)/len(monthly_var),2)
print(f"The average change for the period is ${average}")

#returning max variance value
max_value = max(monthly_var)

#returning date for max variance value by refernecing the index of the value
date_max = date[monthly_var.index(max_value)+1]
print(f"The maximum increase was in: {date_max} ${max_value}")


#returning  min value
min_value = min(monthly_var)

#returning date for min variance value by refernecing the index of the value
date_min = date[monthly_var.index(min_value)+1]
print(f"The maximum decrease was in: {date_min} ${min_value}")


#define a path for the output txt file
path_txt = os.path.join('/Users/ak/Documents/DA/Python/python_challenge/PyBank/Analysis/Output.txt')

#open the output file, then write the data
with open(path_txt, 'w') as output:
    writer_txt = output.write("Financial Analysis" + "\n")
    writer_txt = output.write("------------------" + "\n")
    writer_txt = output.write("Total Months: " + str(line_count)+ "\n")
    writer_txt = output.write("Total Amount: $" + str(net_total_amount)+ "\n")
    writer_txt = output.write("Greatest Increase in Profits was in: "+ str(date_max)+" $"+str(max_value)+ "\n")
    writer_txt = output.write("Greatest Decrease in Profits was in: "+ str(date_min)+" $"+str(min_value)+ "\n")
        
    
       
     







