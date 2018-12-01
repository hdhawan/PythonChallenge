import os
import csv

budget_data_sheet = "budget_data.csv"
budget_result_sheet = "budget_analysis.txt"

with open(budget_data_sheet, newline="") as budget_data_fh:
    fh_reader = csv.reader(budget_data_fh, delimiter=',')
    header = next(fh_reader)
    bank_data_list = []
    prev_month = 0
    months = 0
    total = 0
    for row in fh_reader:
        bank_data_list.append(row)
        if months == 0:
            bank_data_list[months].append(0)
        elif months > 0:
            bank_data_list[months].append(int(bank_data_list[months][1]) - prev_month)
        prev_month = int(bank_data_list[months][1])
        total += int(row[1])
        months += 1
    list_profit_loss = []
    total_change = 0.0
    for counter in range(0,(months)):
        list_profit_loss.append(int(bank_data_list[counter][2]))
        total_change += int(list_profit_loss[counter])

max_profit_index = list_profit_loss.index(max(list_profit_loss))
max_loss_index = list_profit_loss.index(min(list_profit_loss))

max_profit = '${:,.2f}'.format(max(list_profit_loss))
max_loss = '${:,.2f}'.format(min(list_profit_loss))
avg_change = '${:,.2f}'.format(total_change/(months-1))
total = '${:,.2f}'.format(total)

output_fh = open(budget_result_sheet, 'w')

print("Financial Analysis\n")
output_fh.write("Financial Analysis\n")
print("----------------------------\n")
output_fh.write("----------------------------\n")

print(f"Total Months: {months}\n")
output_fh.write(f"Total Months: {months}\n")

print(f"Total Net: {total}\n")
output_fh.write(f"Total Net: {total}\n")

print(f"Average Change: {avg_change}\n")
output_fh.write(f"Average Change: {avg_change}\n")

print(f"Greatest increase in Profits: {bank_data_list[max_profit_index][0]} ({max_profit})\n")
output_fh.write(f"Greatest increase in Profits: {bank_data_list[max_profit_index][0]} ({max_profit})\n")

print(f"Greatest Dip in Profits: {bank_data_list[max_loss_index][0]} ({max_loss})\n")
output_fh.write(f"Greatest Dip in Profits: {bank_data_list[max_loss_index][0]} ({max_loss})\n")

budget_data_fh.close()
output_fh.close()