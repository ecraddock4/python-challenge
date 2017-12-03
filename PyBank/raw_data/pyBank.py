import os
import csv


budget_data = os.path.join('budget_data_1.csv')


#Initialize/open data
with open(budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip Header
    next(csvreader)

    month_count = 0

    revenue_count = 0


    greatest_increase = {
        'date' : '',
        'revenue' : 0
    }


    increase_in_revenue = []

    previous_month = 0


    for row in csvreader:
        month_count = month_count + 1

        #Declare Columns
        date=row[0]
        revenue=int(row[1])

        revenue_count += revenue


        if revenue > greatest_increase['revenue']:
            greatest_increase['revenue'] = revenue
            greatest_increase['date'] = date

        difference = revenue - previous_month
        previous_month = revenue
        increase_in_revenue.append(difference)

    increase_in_revenue.pop(0)

    print(month_count)
    print(revenue_count)
    print(greatest_increase)
    print(increase_in_revenue)

    print(max(increase_in_revenue))