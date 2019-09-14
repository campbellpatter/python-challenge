#importing csv module
import csv

#opening election data csv
with open("election_data.csv",newline = '') as election:
    
    #skip header
    csvreader = csv.reader(election, delimiter = ',')
    csvheader = next(csvreader)
    
    #initialize counters
    count = 0
    candidates = []
    votes = []
    
    #loop through rows
    for row in csvreader:
        
        count += 1
        
        #add to candidates already appended
        if row[2] in candidates:
            votes[candidates.index(row[2])] += 1
            
        #append if not already
        elif row[2] not in candidates:
            candidates.append(row[2])
            votes.append(1)
    
    #create percentages
    percentages = []
    for x in votes:
        percentages.append((x/count)*100)
    
    #create text file
    output = open("output.txt","w")
    
    #first few lines showing total votes, write to txt file
    message1 = ("Election Results\n-------------------------\nTotal Votes: {}\n-------------------------".format(count))
    output.write(message1 + "\n")
    print(message1)
    
    #print candidates and corresponding stats, write to txt file
    myindex = 0
    for y in candidates:
        person = y
        person_perc = round(percentages[myindex], 3)
        person_votes = votes[myindex]
        message2 = ("{}: {}% ({})".format(person, person_perc, person_votes))
        myindex += 1
        output.write(message2 + "\n")
        print(message2)
    
    #determine winner using index
    winner = candidates[votes.index(max(votes))]
    
    #print winner, write to txt file
    message3 = ("-------------------------\nWinner: {}\n-------------------------".format(winner))
    output.write(message3)
    print(message3)
   
    #close txt file
    output.close()
    
            