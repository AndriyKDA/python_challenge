#*********Poll python exersize************import osimport csv#path to colect data from the csv file in the resource folderpath =os.path.join('/Users/ak/Documents/DA/Python/python_challenge/PyPoll/Resources/election_data.csv')#read in csv filewith open(path, 'r') as pollfile:    #pass file to csv reader and split the data on commas    csv_reader = csv.reader(pollfile, delimiter=',')    #print(csv_reader)        #ommit the header row    csv_header = next(csv_reader)        #create a line count and set it to 0    line_count = 0            #create a list to hold unique candidates names    candidates = []    candidate_all = []        #loop through csv file    for row in csv_reader:                #calcualte number of rows        #line_count +=1                #create a list of names        candidate_all.append(row[2])                #calcualte total number of votes as the number of records in the list        count = int(len(candidate_all))                 #add unique candidates names to the candidates list        if row[2] not in candidates:           candidates.append(row[2])         #create a dicitionary to store name values and counts. ref: https://www.tutorialspoint.com/count-frequencies-of-all-elements-in-array-in-python       name_count = {}       #loop thoruhg the list of names    for name in candidate_all:              #increment by 1 if name exist in the dictionary               if name in name_count:           name_count[name] +=1                  #add 1 if name is not in the dictionary          else:           name_count[name] = 1                                #print number of votes        print(f"Number of Votes is: {count}")#print(candidates)perc_list = []#loop through the dictionary for key, value in name_count.items():        #calculate percentage of total votes for each value in the dictionary    perc = round(value/count*100,3)    perc_list.append(perc)   #print dictionary output and percentage of total    print(f"{key}:  {perc}%  ({value})")max_vote = max(zip(perc_list, name_count.keys(),name_count.values())) #https://www.youtube.com/watch?v=E1GueQ5ULc8print(f"The winner is {max_vote[1]}")                    