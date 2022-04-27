# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import dependencies
import csv
import os

# Variable to load election results csv file from path
file_to_load = os.path.join("Resources", "election_results.csv")
# Variable to save text file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open election results and read the file
with open(file_to_load) as election_data:

    # Read the file with reader function
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)


# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")