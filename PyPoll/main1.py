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


#
#
#
# 	data_sheet_header = next(fh_reader)
#     row = next(fh_reader)
#     budget_profit = 0
#     budget_loss = 0
#     profit_max = int(row[1])
#     loss_max = int(row[1])
#     if int(row[1]) > 0:
#         budget_profit = int(row[1])
#     elif int(row[1]) < 0:
#         budget_loss = int(row[1])
#     count_months = 1
#     for row in fh_reader:
#         if int(row[1]) > 0:
#             budget_profit += int(row[1])
#         elif int(row[1]) < 0:
#             budget_loss += int(row[1])
#
#         if int(row[1]) >= profit_max:
#             profit_max = int(row[1])
#         elif int(row[1]) <= loss_max:
#             loss_max = int(row[1])
#         count_months += 1
#     budget_profit = '${:,.2f}'.format(budget_profit)
#     budget_loss = '${:,.2f}'.format(budget_loss)
#     profit_max = '${:,.2f}'.format(profit_max)
#     loss_max = '${:,.2f}'.format(loss_max)
#     print(f"Total profit = {budget_profit}")
#     print(f"Total Loss = {budget_loss}\n")
#     print(f"Total months = {count_months}\n")
#     print(f"Max Profit = {profit_max}\n")
#     print(f"Max Loss = {loss_max}\n")
#
# budget_report_fh = open(budget_result_sheet,'w')
# budget_report_fh.write(f"Total profit = {budget_profit}\n")
# budget_report_fh.write(f"Total Loss = {budget_loss}\n")
# budget_report_fh.write(f"Total months = {count_months}\n")
# budget_report_fh.write(f"Max Profit = {profit_max}\n")
# budget_report_fh.write(f"Max Loss = {loss_max}\n")

