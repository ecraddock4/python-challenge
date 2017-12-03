
candidate_name = row[2]

# And begin tracking that candidate's voter count
votes = 0

# Dictinary
candidates_2 = {}


    for row in csvreader:

         votes += 1

        # Find the Candidates Values and Number of Votes
        # If candidate is not in the dictionary, create it, 
        # ELSE if it is in the dictionary add one value count to that candidate name. 
        if candidate not in candidates_2:
            votes[candidate] = 1
        else:
            votes[candidate] += 1

    # Divide count by total items, make percent 
    # aka accessing everything in the dictionary
    for key, value in candidates_2.items():

        # declare percent as a int
        percent = 0

        # Divide value by the total
        percent = value / votes

        # Format as percent 
        percent = '{0:.0f}%'.format(percent * 100)


        #key = candidate, value = vote count for candidate, percent
        print(str(key) + str(value) + str(percent))
          
      