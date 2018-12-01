import os
import csv

election_data_sheet = "election_data.csv"
election_result_sheet = "election_result.txt"
fh_writer = open(election_result_sheet, 'w')
with open(election_data_sheet, newline="") as election_data_fh:
    fh_reader = csv.reader(election_data_fh, delimiter=',')
    next(fh_reader)
    poll_list = []
    candidate_list = {}
    candidate_summary = {}
    candidate_winner = {}

    print(f"Election Results\n")
    print(f"-------------------------------\n")
    fh_writer.write(f"Election Results\n")
    fh_writer.write(f"-------------------------------\n")

    for row in fh_reader:
        poll_list.append(row)
    TotalVotes = len(poll_list)

    print(f"Total Votes = {TotalVotes}")
    print(f"-------------------------------\n")
    fh_writer.write(f"Total Votes = {TotalVotes}\n")
    fh_writer.write(f"-------------------------------\n")

    for vote in poll_list:
        candidate_name = vote[2]
        if candidate_name not in candidate_list:
            candidate_list[candidate_name] = 0
        candidate_list[candidate_name] += 1

    for name in candidate_list:
        candidate_summary[name] = (candidate_list[name]*100)/TotalVotes

    candidate_win = ["Dummy_Candidate",0]
    for name in candidate_summary:
        if candidate_win[1] < int(candidate_summary[name]):
            candidate_win[1] = candidate_summary[name]
            candidate_win[0] = name

for name in candidate_list:
    candidate_summary[name] = '%{:.3f}'.format(candidate_summary[name])
    print(f"{name}: {candidate_summary[name]} ({candidate_list[name]}) \n")
    fh_writer.write(f"{name}: {candidate_summary[name]} \n")

print(f"-------------------------------\n")
fh_writer.write(f"-------------------------------\n")
print(f"Winner: {candidate_win[0]} \n")
fh_writer.write(f"Winner: {candidate_win[0]} \n")
print(f"-------------------------------\n")
fh_writer.write(f"-------------------------------\n")

fh_writer.close()
election_data_fh.close()