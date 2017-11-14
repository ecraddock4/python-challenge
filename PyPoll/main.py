import os
import csv

#V2 = Data Set 1


# Read CSV
election_data_2 = os.path.join("../PyPoll", "election_data_2.csv")

#Create Dictionary for Votes
votes = {}

# Create variables for total votes and the winner
total_votes = 0
winner = 0

# Initialize
with open(election_data_2, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	# Skips title row
	next(csvreader)

	# Count all rest of rows
	for row in csvreader:
		total_votes = total_votes + 1

		# Declare Columns 
		county = row[1]
		candidate = row[2]
	
		# Count candidates
		if candidate not in votes:
			votes[candidate] = 1
		else:
			votes[candidate] += 1


	print("Election Results")
	print("------------------------")
	print("Total Votes: " + str(total_votes))
	print("------------------------")


	# Divide count by total items, make percentage
	for key, value in votes.items():
		pct = 0
		pct = value / total_votes
		pct = '{0:.0f}%'.format(pct * 100)

		print(str(key) + ": " + str(value) + " (" + str(pct) + ")")


	# Find max count and declare to winner
	winner = max(votes, key=votes.get)

	print("------------------------")	
	print("The winner is " + winner)
	print("------------------------")	
	print('\n')


#=====================================================================

#V2 = Data Set 1

# Read CSV
election_data_1 = os.path.join("../PyPoll", "election_data_1.csv")

#Create Dictionary for Votes
votes_b = {}

# Create variables for total votes and the winner
total_votes_b = 0
winner_b = 0

# Initialize
with open(election_data_1, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	
	# Skips title row
	next(csvreader)

	# Count all rest of rows
	for row in csvreader:
		total_votes_b = total_votes_b + 1

		# Declare Columns 
		county = row[1]
		candidate = row[2]
	
		# Count candidates
		if candidate not in votes_b:
			votes_b[candidate] = 1
		else:
			votes_b[candidate] += 1


	print("Election Results")
	print("------------------------")
	print("Total Votes: " + str(total_votes_b))
	print("------------------------")


	# Divide count by total items, make percentage
	for key, value in votes_b.items():
		pct = 0
		pct = value / total_votes_b
		pct = '{0:.0f}%'.format(pct * 100)

		print(str(key) + ": " + str(value) + " (" + str(pct) + ")")



	# Find max count and declare to winner
	winner_b = max(votes_b, key=votes_b.get)

	print("------------------------")	
	print("The winner is " + winner_b)
	print("------------------------")	




#voter_output = f"{candidate}:{pct} ({votes})/n"
#zip
#two list of equal length, zipping together creates tuples
#list of names
#list of percentages
#totals_votes
#zip together
#data frames
#concatinate structures 

		

