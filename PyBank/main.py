import os
import csv
import statistics as stats


def display_list(a_list):
    # Print items of a list on the terminal
    for item in a_list:
        print(item)


path_to_file = os.path.join('Resources', 'budget_data.csv')

budget_dates = []
budget_profit_losses = []
changes = []
with open(path_to_file, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # * Step over the headers
    csv_header = next(csvreader)

    for row in csvreader:
        budget_dates.append(row[0])
        budget_profit_losses.append(int(row[1]))

for idx in range(1, len(budget_profit_losses)):
    changes.append(budget_profit_losses[idx] - budget_profit_losses[idx-1])

print("Financial Analysis")
print("----------------------------------\n")
print(f"Total Months: {len(budget_dates)}")
print(f"Total: ${sum(budget_profit_losses)}")
print(f"Average change: ${round(stats.mean(changes),2)}")

# * Print max value and location of max value
max_date = budget_dates[changes.index(max(changes))+1]
print("Greatest Increase in Profits: " + max_date + f" $({max(changes)})")

# * Print min value and location of min value
min_date = budget_dates[changes.index(min(changes))+1]
print("Greatest Decrease in Profits: " + min_date + f" $({min(changes)})")
