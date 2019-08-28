import csv
import os

election_data = os.path.join('election_data.csv')

def winner(election_data):
 
    Votes = 0
    dict = {"Khan":0, "Correy":0, "Li":0, "O'Tooley":0}
    percent_vote_K = 0
    percent_vote_C = 0
    percent_vote_L = 0
    percent_vote_O = 0
    
    with open(election_data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        
        for row in csvreader:
            Votes += 1
            K_votes = dict["Khan"]
            C_votes = dict["Correy"]
            L_votes = dict["Li"]
            O_votes = dict["O'Tooley"]
            if row[2] == "Khan":
                dict["Khan"] = dict["Khan"] +1
                percent_vote_K = (dict["Khan"] +1)/Votes * 100
            if row[2] == "Correy":
                dict["Correy"] = dict["Correy"] +1
                percent_vote_C = (dict["Correy"] +1)/Votes * 100
            if row[2] == "Li":
                dict["Li"] = dict["Li"] +1
                percent_vote_L = (dict["Li"] +1)/Votes * 100
            if row[2] == "O'Tooley":
                dict["O'Tooley"] = dict["O'Tooley"] +1
                percent_vote_O = (dict["O'Tooley"] +1)/Votes * 100

    print(dict)      
    return [Votes, K_votes, percent_vote_K, C_votes, percent_vote_C, L_votes, percent_vote_L, O_votes, percent_vote_O]
final = winner(election_data)
print(final)  

K_percent = final[2]
C_percent = final[4]
L_percent = final[6]
O_percent = final[8]

print("Election Results")
print("_______________________________")
print(f"Total Votes: {(final[0])}")
print("_______________________________")
print(f"Khan: {K_percent:.3f}% ({(final[1])})")
print(f"Correy: {C_percent:.3f}% ({(final[3])})")
print(f"Li: {L_percent:.3f}% ({(final[5])})")
print(f"O'Tooley: {O_percent:.3f}% ({(final[7])})")
print("_______________________________")
print(f"Winner: Khan")
print("_______________________________")

