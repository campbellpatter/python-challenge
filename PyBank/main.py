#importing modules
import csv

#opening csv in same working directory as this script 
with open ("budget_data.csv",newline = "", encoding='utf-8') as budget:

    #reading csv, skipping header
    csvreader = csv.reader(budget, delimiter = ",")
    csv_header = next(csvreader)
    
    #initializing variables to be appended
    my_positive = [0]
    my_positive_date = []
    my_negative = [0]
    my_negative_date = []
    my_change = []
    my_values = []
    #initializing counters
    my_months = 0
    
    #loop through rows
    for row in csvreader:
            
            #declaring second element in row to be a float for and appending to list
            my_values.append(float(row[1]))
            
            #iterating counters
            my_months += 1
            
            #creates list of difference values b/w adjacent elements
            if len(my_values) > 1:
                my_change.append(my_values[len(my_values)-1] - my_values[len(my_values)-2])
                
                #if current element is the largest positive change so far, assign as bigprofit variable and store date
                if my_change[len(my_change)-1] == max(my_change):
                    my_bigprofit = my_change[len(my_change)-1]
                    bigprofit_date = row[0]
                    
                #same thing for largest negative change
                if my_change[len(my_change)-1] == min(my_change):
                    my_bigloss = my_change[len(my_change)-1]
                    bigloss_date = row[0]
            
    
#average profit/loss
average_change = round(sum(my_change)/(my_months-1),2)
    
#total profit/loss 
net_PL = sum(my_values)
    
#creating message
message = "Financial Analysis\n\
----------------------------\n\
Total Months: {}\n\
Total: ${}\n\
Average Change: {}\n\
Greatest Increase in Profits: {} (${})\n\
Greatest Decrease in Profits: {} (${})"\
.format(my_months, net_PL, average_change, bigprofit_date, int(my_bigprofit), bigloss_date, int(my_bigloss))
 
#printing to terminal
print(message)
    
#writing to .txt file
output = open("output.txt","w")
output.write(message)
output.close()