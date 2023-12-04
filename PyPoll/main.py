# Import Module for to create a file path across opertaing systems
import os 

# Import Module for reading CSV files
import csv

# Specify which file to read
election_data = os.path.join('Resources', 'election_data.csv')

# Aggregating csv data in respective lists 
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Donae"]
total_votes = []
stockham_votes = []
degette_votes = []
doane_votes = []

# From aggregated lists created dictionary to read over candidate function below
candidate_data = {"candidate_votes": [stockham_votes,degette_votes,doane_votes]}

with open(election_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvreader)

    for row in csvreader:

    	# Total votes in election
    	total_votes.append(row[2])

    	# Assign candidate to list
    	if row[2] == "Charles Casper Stockham":
    		stockham_votes.append(row[2])
    	elif row[2] == "Diana DeGette":
    		degette_votes.append(row[2])
    	elif row[2] == "Raymon Anthony Doane":
    		doane_votes.append(row[2])

# Function that is dynamic to loop through each candidate for % total of votes and total votes
def candidates_election_metrics():
    total_votes_count = len(total_votes)
    highest_vote_percentage = 0
    winner = ""

    # For each candidate in candidate list, looping through candidate dict to find dynamic values for % total and total votes
    for cand in range(len(candidates)):
        candidate = candidates[cand]
        candidate_votes = candidate_data["candidate_votes"][cand]
        candidate_votes_count = len(candidate_votes)
        
        # Calculate the percentage of votes for the candidate
        vote_percentage = (candidate_votes_count / total_votes_count) * 100

        print(f"{candidate}: {round(vote_percentage, 3)}% ({candidate_votes_count})")
        print(" ")

        # Dynamic vote percentage conditional to identify who won the election 
        if vote_percentage > highest_vote_percentage:
            highest_vote_percentage = vote_percentage
            winner = candidate
    print("--------------------------")
    print(" ")  
    # Election winner   
    print(f"Winner: {winner}")
    print(" ")
    print("--------------------------")
	
# Election results 
print(" ")
print("Election Results")
print(" ")
print("--------------------------")
print(" ")
print(f"Total Votes: {len(total_votes)} ")
print(" ")
print("--------------------------")
print(" ")
candidates_election_metrics()


# Set variable for output file
output_file = os.path.join("analysis", "election_analysis_results.txt")


with open(output_file, 'w') as file:
	# Redirect the standard output to the file
	import sys
	original_stdout = sys.stdout
	sys.stdout = file
	
	print(" ")
	print("Election Results")
	print(" ")
	print("--------------------------")
	print(" ")
	print(f"Total Votes: {len(total_votes)} ")
	print(" ")
	print("--------------------------")
	print(" ")
	candidates_election_metrics()

	# Restore the standard output
	sys.stdout = sys.__stdout__