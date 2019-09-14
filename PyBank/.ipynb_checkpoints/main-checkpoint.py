#importing modules
import csv

#opening csv in same working directory as this script 
with open ("budget_data.csv",newline = "") as budget:

    #reading csv, skipping header
    csvreader = csv.reader(budget, delimiter = ",")
    csv_header = next(csvreader)
    
    #initializing variables to be appended
    my_profit = [0]
    my_profit_date = []
    my_loss = [0]
    my_loss_date = []
    
    #initializing counters
    my_months = 0
    net_PL = 0
    
    #loop through rows
    for row in csvreader:
            
            #declaring second column value to be a float for performing math operations
            pL = float(row[1])
            
            #iterating counters
            my_months += 1
            net_PL += pL
            
            #checks if profit, and if greater than last largest profit, appends if true
            if pL > 0 and pL > my_profit[len(my_profit)-1]:
                
                #append to increasing profits list
                my_profit.append(pL)
                #append to dates of increasing profits list
                my_profit_date.append(row[0])
            
            #checks if loss, and if greater than last largest loss
            if pL < 0 and pL < my_loss[len(my_loss)-1]:
                
                #append to increasing losses list
                my_loss.append(pL)
                #append to dates of increasing losses list
                my_loss_date.append(row[0])
    
    #average profit/loss
    average_PL = round(net_PL/my_months,2)
    
    #formating net profit/loss 
    net_PL = int(net_PL)
    
    #takes last value of increasing profits list
    my_bigprofit = my_profit.pop()
    
    #takes last value of increasing losses list
    my_bigloss = my_loss.pop()
    
    #takes last values of lists which have corresponding dates
    bigprofit_date = my_profit_date.pop()
    bigloss_date = my_loss_date.pop()
    
    #printing
    message = "Financial Analysis\n----------------------------\nTotal Months: {}\nTotal: ${}\nAverage Change: {}\nGreatest Increase in Profits: {} (${})\nGreatest Decrease in Profits: {} (${})".format(my_months, net_PL, average_PL, bigprofit_date, int(my_bigprofit), bigloss_date, int(my_bigloss))    
    print(message)
    
    #writing to text file
    output = open("output.txt","w")
    output.write(message)
    output.close()
            