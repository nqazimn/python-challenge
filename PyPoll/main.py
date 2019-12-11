import os
import csv


def display_list(a_list):
    # Print items of a list on the terminal
    for item in a_list:
        print(item)


path_to_file = os.path.join('Resources', 'election_data.csv')

voter_IDs = []
counties = []
candidates = []

with open(path_to_file, newline='', encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # * Step over the headers
    csv_header = next(csvreader)

 # Read and store data
    for row in csvreader:
        voter_IDs.append(int(row[0]))
        counties.append(row[1])
        candidates.append(row[2])

# * Print output on terminal
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {len(voter_IDs)}")
print("----------------------------------\n")

#print(f"Average Change: ${round(stats.mean(changes),2)}")
