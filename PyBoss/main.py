import os
import csv

employee_data = "employee_data.csv"
employee_data_transformed = "employee_data_transformed.csv"

us_state_abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
                   'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN',
                   'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                   'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
                   'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
                   'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
                   'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                   'West Virginia': 'WV', 'Wisconsin': 'WI','Wyoming': 'WY'}

with open(employee_data, newline="") as employee_data_fh:
    fh_reader = csv.reader(employee_data_fh, delimiter= ',')
    counter = 0
    employee_data_list = []
    split_name = []
    for row in fh_reader:
        employee_data_list.append(row)
    employee_count = len(employee_data_list)
    for counter in range(0, employee_count):
        if counter == 0:
            employee_data_list[counter].insert(2, "Last Name")
            employee_data_list[counter][1] = "First Name"
        elif counter > 0:
            full_name = employee_data_list[counter][1]
            ssn_original = employee_data_list[counter][3]
            ssn_list = ssn_original.split("-",3)
            ssn_third = ssn_list[2]
            ssn_modified = "***"+"-"+"**"+ssn_third
            employee_data_list[counter][3] = ssn_modified
            date_original = employee_data_list[counter][2]
            date_list = date_original.split("-",3)
            date_modified = date_list[0]+"/"+date_list[1]+"/"+date_list[2]
            employee_data_list[counter][2] = date_modified
            split_name = full_name.split(" ",2)
            employee_data_list[counter][1] = split_name[0]
            employee_data_list[counter].insert(2, split_name[1])
            if employee_data_list[counter][5] in us_state_abbrev:
                employee_data_list[counter][5] = us_state_abbrev[employee_data_list[counter][5]]
fh_writer = open(employee_data_transformed, 'w')
for row in employee_data_list:
    row = map(str, row)
    line = ",".join(row)
    fh_writer.write(f"{line}\n")

employee_data_fh.close()
fh_writer.close()