#print("hello")



import os
import csv

#state abbriviation dictionary
#state_2 = {state: abbrev for abbrev, state in state_2.items()}
us_state_abbrev = {
        'Alabama': 'AL',
        'Alaska': 'AK',
        'Arizona': 'AZ',
        'Arkansas': 'AR',
        'California': 'CA',
        'Colorado': 'CO',
        'Connecticut': 'CT',
        'Delaware': 'DE',
        'Florida': 'FL',
        'Georgia': 'GA',
        'Hawaii': 'HI',
        'Idaho': 'ID',
        'Illinois': 'IL',
        'Indiana': 'IN',
        'Iowa': 'IA',
        'Kansas': 'KS',
        'Kentucky': 'KY',
        'Louisiana': 'LA',
        'Maine': 'ME',
        'Maryland': 'MD',
        'Massachusetts': 'MA',
        'Michigan': 'MI',
        'Minnesota': 'MN',
        'Mississippi': 'MS',
        'Missouri': 'MO',
        'Montana': 'MT',
        'Nebraska': 'NE',
        'Nevada': 'NV',
        'New Hampshire': 'NH',
        'New Jersey': 'NJ',
        'New Mexico': 'NM',
        'New York': 'NY',
        'North Carolina': 'NC',
        'North Dakota': 'ND',
        'Ohio': 'OH',
        'Oklahoma': 'OK',
        'Oregon': 'OR',
        'Pennsylvania': 'PA',
        'Rhode Island': 'RI',
        'South Carolina': 'SC',
        'South Dakota': 'SD',
        'Tennessee': 'TN',
        'Texas': 'TX',
        'Utah': 'UT',
        'Vermont': 'VT',
        'Virginia': 'VA',
        'Washington': 'WA',
        'West Virginia': 'WV',
        'Wisconsin': 'WI',
        'Wyoming': 'WY',
}


#create lists for data points
ID = []
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []

file_name = "NameSSN.csv"
csvpath = os.path.join("..", "Resources", "NamesSSN.csv")



#print(csvpath)


#opening Homework file as csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
     


    # Loop through the csv data
    for i,row in enumerate(csvreader):
        if i >0:
            #print(row)
            line = row[0]
            elements = line.split(",")
            ID.append(elements[0])
            #print(elements)
            #temp = elements[1]
            temp = elements[1].split(" ")
            First_Name.append(temp[0])
            Last_Name.append(temp[1])
            temp = elements[2].split("-")
            temp1 = temp[1] + "/" + temp[2] + "/" + temp[0]
            DOB.append(temp1)
            temp = elements[3].split("-")
            temp1 = "***-**-" + temp[2]
            SSN.append(temp1)
            #print(elements)
            temp = us_state_abbrev[elements[4]]
            State.append(temp)

#print(len(ID))

#Column headers 
header = ['ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']
new_employee_list = []
#to create dictionaries of customers 
for i in range(len(ID)):
    employee_dict = {}
    employee_dict[header[0]] = ID[i]
    employee_dict[header[1]] = First_Name[i]
    employee_dict[header[2]] = Last_Name[i]
    employee_dict[header[3]] = DOB[i]
    employee_dict[header[4]] = SSN[i]
    employee_dict[header[5]] = State[i]

    #print(employee_dict)

    new_employee_list.append(employee_dict)

cleaned_csv = zip(ID, First_Name, Last_Name, DOB, SSN, State)

# Set variable for output file
output_file = os.path.join("new_employee_list.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["ID", "First Name", "Last Name", "Birthdate", "SSN", "State"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)