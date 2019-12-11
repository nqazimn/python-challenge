import os
import csv
import collections


def display_list(a_list):
    # Print items of a list on the terminal
    for item in a_list:
        print(item)


path_to_file = os.path.join('Resources', 'election_data.csv')
path_to_text_file = os.path.join('election_results.txt')

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

# Total votes is length of any of the 3 lists obtained from csv file
total_votes = len(voter_IDs)

# * Using collections module to analyze the stored data
""" 
* using most_common() method from collections module.
* most_commin(): Returns a list of the n most common elements and 
* their counts from the most common to the least. 
 ! source: (https://docs.python.org/3/py-modindex.html)
"""
election_data = collections.Counter(candidates).most_common()

percent_votes = []
for candidate in election_data:
    temp = round(candidate[1]/total_votes*100.0, 2)
    temp_str = ("{0:0.3f}".format(temp))
    percent_votes.append(temp_str)

# * Print output on terminal
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------\n")

for idx in range(0, len(percent_votes)):
    print(
        f"{election_data[idx][0]}: {percent_votes[idx]} % ({election_data[idx][1]})")

print("----------------------------------")
# * Since election_data is sorted the first element will be
# * the candidate with most votes
print(f"Winner: {election_data[0][0]}")
print("----------------------------------")

# * Print output to text file
with open(path_to_text_file, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("----------------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("----------------------------------\n")

    for idx in range(0, len(percent_votes)):
        text_file.write(
            f"{election_data[idx][0]}: {percent_votes[idx]} % ({election_data[idx][1]})\n")
    text_file.write("----------------------------------\n")
    text_file.write(f"Winner: {election_data[0][0]}\n")
    text_file.write("----------------------------------")
