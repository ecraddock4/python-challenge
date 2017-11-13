import os
import csv
import datetime
import re

#CSV 1
employee_data1 = os.path.join("../PyBoss", "employee_data1.csv")

with open(employee_data1, newline='') as csvfile:
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


		#Changing dates
		#dt = row[2]
		#dt = datetime.datetime.strptime(dt, '%Y-%m-%d').strftime('%m/%d/%y')



		#Adding astricks to social security
		ssn = row[3]
		ssn = list(ssn)
		ssn[5:] = '*'
		''.join(ssn)
		print(ssn)
		#regular expression
		#ssn = re.sub(r"</?\[])

		# Splitting Name into first name & last name
		name_split = row[1].split(" ")
		first_name.append(name_split)
		last_name.append(name_split)

		#??append rows or names or what????


		for key in us_state_abbrev.key():
			us_state_abbrev(key) = us_state_abbrev(value)


	print(cleaned_employee_data1)





#CSV 2
#employee_data2 = os.path.join("../PyBoss", "employee_data2.csv")

#with open(employee_data2, newline='') as csvfile:
	#csvreader2 = csv.reader(csvfile, delimiter=',')
	#dict2 = {row[0]: row[1] for row in csvreader2}