import os
import csv

pypoll= os.path.join('/users/rheapius/python_challenge/pypoll/resources/election_data.csv')

Voters= []
Candidates=[]      

with open(pypoll, 'r') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    header= next(csvreader)
    for row in csvreader:
        Voters.append(row[0])
        if row[2] not in Candidates:
            Candidates.append(row[2])

    total_votes= int(len(Voters))
    Candidates_names= str(Candidates)

output= (
        f"Election Results\n"
        f"----------------------------------------------\n"
        f"Total Votes: {total_votes}\n"
        f'----------------------------------------------\n'
        f"{Candidates_names}\n"
        )

print(output)

results= os.path.join('/users/rheapius/python_challenge/pypoll/analysis/results.txt')

with open(results, "w") as text_file:
    text_file.write(output)