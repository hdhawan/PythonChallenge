import os
import csv

budget_data_sheet = "budget_data.csv"
budget_result_sheet = "budget_analysis.txt"
with open(budget_data_sheet,newline="") as budget_data_fh:
    fh_reader = csv.reader(budget_data_fh,delimiter=',')
    data_sheet_header = next(fh_reader)
    row = next(fh_reader)
    budget_profit = 0
    budget_loss = 0
    profit_max = int(row[1])
    loss_max = int(row[1])
    if int(row[1]) > 0:
        budget_profit = int(row[1])
    elif int(row[1]) < 0:
        budget_loss = int(row[1])
    count_months = 1
    for row in fh_reader:
        if int(row[1]) > 0:
            budget_profit += int(row[1])
        elif int(row[1]) < 0:
            budget_loss += int(row[1])

        if int(row[1]) >= profit_max:
            profit_max = int(row[1])
        elif int(row[1]) <= loss_max:
            loss_max = int(row[1])
        count_months += 1
    budget_profit = '${:,.2f}'.format(budget_profit)
    budget_loss = '${:,.2f}'.format(budget_loss)
    profit_max = '${:,.2f}'.format(profit_max)
    loss_max = '${:,.2f}'.format(loss_max)
    print(f"Total profit = {budget_profit}")
    print(f"Total Loss = {budget_loss}\n")
    print(f"Total months = {count_months}\n")
    print(f"Max Profit = {profit_max}\n")
    print(f"Max Loss = {loss_max}\n")

budget_report_fh = open(budget_result_sheet,'w')
budget_report_fh.write(f"Total profit = {budget_profit}\n")
budget_report_fh.write(f"Total Loss = {budget_loss}\n")
budget_report_fh.write(f"Total months = {count_months}\n")
budget_report_fh.write(f"Max Profit = {profit_max}\n")
budget_report_fh.write(f"Max Loss = {loss_max}\n")

budget_data_fh.close()
budget_report_fh.close()