import os
import csv


# election_data_in = os.path.join("Resources", "election_data.csv")
# Election_out = os.path.join("pypollresults.txt" )

election_data_in = "election_data.csv"
Election_out = "pypollresults.txt"

# Total Vote Counter
vote_talley = 0

# Declars an empty List to hold candidates and dictionary
candidates = []
vote_counter = {}

# Winning Candidate variable and tracker for the winning count
winner = ""
final_talley = 0

# Read csv and convert it into a list of dictionaries
with open(election_data_in) as election_data:
    reader = csv.reader(election_data)

    # declare the first line as header and to skip it
    header = next(reader)
    counter = 0
    # loop to iterate through the lists
    for row in reader:

        # Run the loader animation
        if ((counter % 300000) == 0):
            print("Processing... \n")

        # vote counter
        vote_talley = vote_talley + 1

        # Extract candidate name from third row value in csv file
        candidate_name = row[2]

        # Loop through candidates identifying each unique candidate discovered
        if candidate_name not in candidates:

            # Append each unique candidate encountered
            candidates.append(candidate_name)

            # track the candidate's voter count
            vote_counter[candidate_name] = 0

        # add a vote to the candidate's count
        vote_counter[candidate_name] = vote_counter[candidate_name] + 1
        counter += 1

# Print the results and export the data to text file
with open(Election_out, "w") as election_txt:

    # Print the final vote count (to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {vote_talley}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    election_txt.write(election_results)

    # Determine the winner by looping through the counts
    for candidate in vote_counter:

        # Retrieve vote count and percentage using float to enable decimals
        votes = vote_counter.get(candidate)
        vote_percentage = float(votes) / float(vote_talley) * 100

        # Determine winning vote count and candidate
        if (votes > final_talley):
            final_talley = votes
            winner = candidate

        # Print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        election_txt.write(voter_output)
