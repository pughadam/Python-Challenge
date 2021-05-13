#import modules
import csv
import os

#create path to csv
pypoll = os.path.join('Resources', 'election_data.csv')


with open(pypoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #set variables
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    O_Tooley_votes = 0

    #loop through the data counting total_votes and total_votes by candidate
    for row in csvreader:
        total_votes += 1
    #fine the total votes for each candidate
    #remember to rename O'Tooley to O_Tooley to avoid syntax issues    
        if (row[2]) == ('Khan'):
            Khan_votes += 1
        elif (row[2]) == ('Correy'):
            Correy_votes += 1
        elif (row[2]) == ('Li'):
            Li_votes += 1
        else:
            O_Tooley_votes += 1

    #percentage of votes and rounding
    Khan_percent = round((Khan_votes/total_votes)*100, 2)
    Correy_percent = round((Correy_votes/total_votes)*100, 2)
    Li_percent = round((Li_votes/total_votes)*100, 2)
    O_Tooley_percent = round((O_Tooley_votes/total_votes)*100, 2)

    #print total vote and percent of votes for validation purposes
    #print(total_votes)
    #print(Khan_votes, Khan_percent)
    #print(Correy_votes, Correy_percent)
    #print(Li_votes, Li_percent)
    #print(O_Tooley_votes, O_Tooley_percent)

    #calculate the winner
    Winner = max(Khan_percent, Correy_percent, Li_percent, O_Tooley_percent)
    if Winner == Khan_percent:
        Winner_Name = "Khan"
    elif Winner == Correy_percent:
        Winner_Name = "Correy"
    elif Winner == Li_percent:
        Winner_Name = "Li"
    else:
        Winner_Name = "O'Tooley"

    #validate if statement for winner
    #print(Winner_Name)

    #print statement for election results
    print("Election Results")
    print("---------------------------------------")
    print("Total Votes: " + str(total_votes))
    print("---------------------------------------")
    print("Khan: " + str(Khan_percent) , "(",str(Khan_votes),")")
    print("Correy: " + str(Correy_percent) , "(",str(Correy_votes),")")
    print("Li: " + str(Li_percent) , "(",str(Li_votes),")")
    print("O'Toole: " + str(O_Tooley_percent), "(",str(O_Tooley_votes),")")
    print("---------------------------------------")
    print("Winner: " + str(Winner_Name))


#create path for textfile
with open('analysis/Election_Results.txt','w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    text.write(f"Khan: {Khan_percent} ({Khan_votes})\n")
    text.write(f"Correy: {Correy_percent} ({Correy_votes})\n")
    text.write(f"Li: {Li_percent} ({Li_votes})\n")
    text.write(f"O'Tooley: {O_Tooley_percent} ({O_Tooley_votes})\n")
    text.write("---------------------------------------\n")
    text.write("Winner: " + str(Winner_Name) + "\n")