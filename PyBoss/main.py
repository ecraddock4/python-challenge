import os
import csv
import datetime
import re

#CSV 1
employee_data1 = os.path.join("../PyBoss", "employee_data1.csv")

with open(employee_data1, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    cleaned_employee_data = csvreader
    
    first_name = []
    last_name = []

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

    # Skips title row
    next(cleaned_employee_data)

    
    for row in cleaned_employee_data:

        # Employee ID
        employee_id = row[0]

        #Changing dates
        dt = row[2]
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d').strftime('%m/%d/%y')


        #Adding astricks to social security
        ssn = row[3]
        # ssn = '617-27-1468'
        # sanitized_ssn = '***-**-1468'
        sanitized_ssn = '***-**-' + ssn[-4:]
   

        # Splitting Name into first name & last name
        name_split = row[1].split(" ")
        first_name.append(name_split[0])
        last_name.append(name_split[1])


        state_name = row[4]
        abbreviation = us_state_abbrev[state_name]

        print(employee_id,', ', name_split[0], ', ', name_split[1],', ', dt, ', ', sanitized_ssn, ', ', state_name, ', ', abbreviation)
    print('\n')
    



    #--------------------------------------------------------------------------------------------------

    # DATA SET 2

    employee_data2 = os.path.join("../PyBoss", "employee_data2.csv")

with open(employee_data2, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    cleaned_employee_data1 = csvreader
    
    first_name = []
    last_name = []

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

    # Skips title row
    next(cleaned_employee_data1)

    
    for row in cleaned_employee_data1:

        # Employee ID
        employee_id = row[0]

        #Changing dates
        dt = row[2]
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d').strftime('%m/%d/%y')


        #Adding astricks to social security
        ssn = row[3]
        # ssn = '617-27-1468'
        # sanitized_ssn = '***-**-1468'
        sanitized_ssn = '***-**-' + ssn[-4:]
   

        # Splitting Name into first name & last name
        name_split = row[1].split(" ")
        first_name.append(name_split[0])
        last_name.append(name_split[1])


        state_name = row[4]
        abbreviation = us_state_abbrev[state_name]
        
        print(employee_id,', ', name_split[0], ', ', name_split[1],', ', dt, ', ', sanitized_ssn, ', ', state_name, ', ', abbreviation)







#CSV 2
#employee_data2 = os.path.join("../PyBoss", "employee_data2.csv")

#with open(employee_data2, newline='') as csvfile:
    #csvreader2 = csv.reader(csvfile, delimiter=',')
    #dict2 = {row[0]: row[1] for row in csvreader2}