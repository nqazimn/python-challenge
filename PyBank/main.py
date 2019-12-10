import os
import csv

def display_list(a_list):
    # Print items of a list on the terminal
    for item in a_list:
        print(item)

path_to_file = os.path.join('Resources','budget_data.csv')

budget_dates=[]
budget_profit_losses=[]

with open(path_to_file, newline='',encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # * Step over the headers
    csv_header = next(csvreader)

    for row in csvreader:
        budget_dates.append(row[0])
        budget_profit_losses.append(row[1])

#display_list(budget_dates)
#display_list(budget_profit_losses)

