#importing dependencies
import csv
from Resources.my_states import my_dict

filepath = 'Resources/employee_data.csv'

#reading employee data
with open(filepath, newline = '') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    #creating list of lists of new variables
    outrow = []
    for row in csvreader:
        emp_ID = row[0]
        first = row[1].split(' ')[0]
        last = row[1].split(' ')[1]
        dob = row[2].split('-')[1] + '/' + row[2].split('-')[2] + '/' + row[2].split('-')[0]
        ssn = '***-***-' + row[3].split('-')[2]
        
        #using dictionary from abbreviation doc
        if row[4] in my_dict:
            state = my_dict[row[4]]
            
        #writing new list of variables to outrow list
        outrow.append([emp_ID, first, last, dob, ssn, state])
    
#write to output csv   
with open('output.csv', 'w', newline='') as out:
    
    csvwriter = csv.writer(out, delimiter=',')
    
    #header
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    
    #rows
    for row in outrow:
        csvwriter.writerow(row)
    





