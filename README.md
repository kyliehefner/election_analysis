# Election Analysis
## Overview of Election Audit
A board of elections employee has reached out for an election audit of the results for a US congressional precinct in Colorado. I was tasked with creating an automatic vote count report that included the following:
1. The total number of votes
2. The number of votes from each county
3. The percentage of votes from each county
4. The county with the largest percentage of the voter turnout
5. List of all the candidates who recieved votes
6. The total number of votes for each candidate
7. The percentage of votes for each candidate
8. The winner of the election based on the popular vote

## Resources
Data Source: election_results.csv

Software: Python 3.7.6, Visual Studio Code 1.66.2

## Results
The analysis of the tabulated results from the election shows the following:
- There were 369,711 total votes cast in the election.
- The county statistics were:
  - Jefferson County constituted 10.5% of the total votes at 38,855 votes.
  - Denver County constituted 82.8% of the total votes at 306,055 votes.
  - Arapahoe County constituted 6.7% of the total votes at 24,801 votes
- The county with the largest turnout was:
  - Denver County which constituted 82.8% of the total votes at 306,055 votes.
- The candidates who recieved votes were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the total votes at 85,213 votes.
  - Diana DeGette received 73.8% of the total votes at 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the total votes at 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the total votes at 272,892 votes.

## Summary
The script created in this project is highly adaptable in that it can be adjusted and used for a wide variety of election audits. For example, the Python code can be repurposed for other congressional elections, senatorial elections, or local elections since the candidate vote count and county vote count in the code are dictionaries that will expand and shrink depending on the number in the election. For example, in a senatorial election, there will be many more counties, which the script for this project can handle without any modifications. Yet there are also simple code modifications that we can make to adapt the code to other types of elections.
```python
candidate_options = []    # Initializing empty candidate options list
candidate_votes = {}    # Initializing empty candidate votes dictionary
candidate_options.append(candidate_name)    # Appending a new candidate name to the list
candidate_votes[candidate_name] = 0    # Creating a new key-value pair in the dictionary
```  
In a rank-choice instant-runoff election if there is no majority winner from the first-choices, then the candidate with the fewest votes is eliminated and the ballots with the eliminated candidate as their first choice now have their second choice count for their vote. We can adjust our Python script to account for this type of election by a conditional if-else statement to check if there is a majority. If there is, we output the results, but if not, we would loop through the ballots again. For each row where the first choice was the eliminated candidate, we would add one vote to the candidate of their second choice. This structure would be repeated until we arrived at a majority winner.
```python
if winning_percentage > 50:
  # output results
else:
  for row in reader:
    candidate_name = row[2]
    if candidate_name == eliminated_candidate:
      candidate_name = row[3]
      candidate_votes[candidate_name] += 1
  # repeat calculations and checking if winning percentage is majority
```  
Our code could also be modified for a policy vote election. Our dictionary of candidates would become a dictionary of policies. Once all the votes were counted we would loop through the policies and use a conditional to check if the number of yes votes is more than 50% of the total votes. We would output if that that policy passed or failed, and then move onto the next policy until all are analyzed.
