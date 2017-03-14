# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

# data file and directory path
PATH = './'
FILE = 'football.csv'

# define a dictionary for scoring the scores of the teams
score_dict = {}

# open the csv file
with open(PATH+FILE) as f:
	# read each of the csv file
	# each row is a list object
    csv_file = csv.reader(f)

    # header
    headers = next(csv_file)
    
    # data: results
    for row in csv_file:
    	# team names are dictionary keys
    	key = row[0]
    	
    	results = row[1:]

    	# compute difference in ‘for’ and ‘against’ goals
    	goal_diff = abs(int(results[4])-int(results[5]))

    	# differences in goals are dictionary values
    	score_dict[key] = goal_diff
f.close()

# dictionary key with the smallest difference in ‘for’ and ‘against’ goals
min_team = min(score_dict, key=score_dict.get)

print(min_team + ' is the team with the smallest difference in ‘for’ and ‘against’ goals.')
print('The difference in ‘for’ and ‘against’ goals for ' + min_team + ' is ' + str(score_dict[min_team]) +'.' )
