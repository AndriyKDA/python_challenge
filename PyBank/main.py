
#*********PyBank python exersise************
import os
import csv

#path to colect data from the csv file in the resource folder
path =os.path.join('/Users/ak/Documents/DA/Python/python_challenge/PyBank/Resources/budget_data.csv')

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
    date = []
    
    for row in csv_reader:
        line_count +=1
        net_total_amount += int(row[1])
        monthly_value.append(int(row[1]))
        date.append(row[0])
        
print(f" Total Months: {line_count}")
print(f" Net Total Amount: {net_total_amount}")



monthly_var = []
#monthly_var_date = []
#write a function to loop through the list indexes and calulate the difference
def monthly_change(monthly_value, date):
    
    for i in range(len(monthly_value)):
    
        #set a condition to make sure indexes are within the range
        if i >= 0 and i <= int(line_count)-2:
        
            #function argument
            change = monthly_value[i+1] - monthly_value[i]
            monthly_var.append(change)
            #print(change)
    
           
    #for x in range(len(date)):
            
        #set a condition to make sure indexes are within the range
     #   if x >= 0 and x <= int(line_count)-2:
            
      #      date_change = date[x+1]
        #    monthly_var_date.append(date_change)
       #     print(date_change)
            
        
# call the function
monthly_change(monthly_value, date)
#print(monthly_change)


#caluclating average value
average = sum(monthly_var)/len(monthly_var)
print(f"The average change for the period is {average}")

#returning max value
max_value = max(monthly_var)
index_max = date[monthly_var.index(max_value)+1]
print(f"The maximum increase: {index_max} {max_value}")


#returning  min value
min_value = min(monthly_var)
index_min = date[monthly_var.index(min_value)+1]
print(f"The maximum decrease: {index_min} {min_value}")



#define a pth for the output txt file
path_txt = os.path.join('/Users/ak/Documents/DA/Python/python_challenge/PyBank/Analysis/Output.txt')

#create list of data to write onto the txt file
#output_text = ["Total Months: $" + str(line_count)+ "\n", 
 #              "Total Amount: $" + str(net_total_amount)+ "\n",
  #             "Greatest Increase in Profits:  $"+ str(max_value)+ "\n", 
   #            "Greatest Decrease in Profits:  $"+ str(min_value)]

#open the output file, then write the data

with open(path_txt, 'w', newline = '') as output:
    writer_txt = output.write("Total Months: " + str(line_count)+ "\n")
    writer_txt = output.write("Total Amount: $" + str(net_total_amount)+ "\n")
    writer_txt = output.write("Greatest Increase in Profits: "+ str(index_max)+" $"+str(max_value)+ "\n")
    writer_txt = output.write("Greatest Decrease in Profits: "+ str(index_min)+" $"+str(min_value)+ "\n")
        
    
       
     







