# import the magic ...
import os
import csv

## "Call" the data...
election_data = os.path.join("Resources", "election_data.csv")

# Create the space (lists) to put our data

total_number_of_votes = []
votes_per_candidate = []
list_of_candidates = []
percentage_of_votes = []

#Read the data taking the first record as a header and then going through each row. Stating that after the "," it continues reading on the line below
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

# Loop through each of the values. Then, if a vote for the candidate is not there... add it

    for row in csvreader:
        total_number_of_votes.append(row[0])

        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])
            index = list_of_candidates.index(row[2])
            votes_per_candidate.append(1)
        else:
            index = list_of_candidates.index(row[2])
            votes_per_candidate[index] +=1

# Get the percentages...

    for votes in votes_per_candidate:
        percent = (votes/len(total_number_of_votes))*100
        percentage_of_votes.append('%.3f' % percent)


# Max number of votes per candidates and comparison to see who won...
max_votes_per_candidate = max(votes_per_candidate)
final_winner = list_of_candidates[votes_per_candidate.index(max_votes_per_candidate)]



#Print everything and format it to the hw's specifications

print("Election Results")
print("------------------------")
print(f"Total votes: {len(total_number_of_votes)-1}")
print("------------------------")
for i in range(len(list_of_candidates)):
    print(f"{list_of_candidates[i]}: ({str(percentage_of_votes[i])}%) ({str(votes_per_candidate[i])})")
print("------------------------")
print(f"Winner: {final_winner}")
print("------------------------")

# Finally we create the .txt document with the print part from above
output = os.path.join("analysis", "output.txt")

with open(output,"w") as result:
    result.write("Election Results")
    result.write("\n")
    result.write("------------------------")
    result.write("\n")
    result.write(f"Total votes: {len(total_number_of_votes)-1}")
    result.write("\n")
    result.write("------------------------")
    result.write("\n")

    for i in range(len(list_of_candidates)):
        result.write(f"{list_of_candidates[i]}: ({str(percentage_of_votes[i])}%) ({str(votes_per_candidate[i])})")
    result.write("\n")
    result.write("------------------------")
    result.write("\n")
    result.write(f"Winner: {final_winner}")
    result.write("\n")
    result.write("------------------------")


        
