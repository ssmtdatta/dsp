import csv
import re


filename = "faculty.csv"

degree_list = []
title_list = []
email_list = []

with open(filename) as f:
    csv_file = csv.reader(f)
    headers = next(csv_file)
    
    for line in csv_file:
    	_, degree, title, email = line
    	degree_list.append(degree)
    	title_list.append(title)
    	email_list.append(email) #Q4

f.close()




##Q1 
# Find how many different degrees there are, and their frequencies: 
# Ex: PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

degree_count = {}

if '0' in degree_list: 
	degree_list.remove('0')
degree_types = map(lambda x: x.split(" "), degree_list)
deg = list(degree_types)
degree_types = [d[i] for d in deg for i in range(0, len(d)) if d[i]!='']
deg = map(lambda x: x.replace(".",'').lower(), degree_types)

degree_types = list(deg)
unq = list(set(degree_types))

print("There are", len(unq), "different degrees.")
print("They are:", unq)

for d in degree_types:
	if d in degree_count:
		degree_count[d] = degree_count[d] + 1
	else:
		degree_count[d] = 1
print(degree_count)



##Q2
# Find how many different titles there are, and their frequencies: 
# Ex: Assistant Professor, Professor

title_types = ['associate', 'assistant', 'professor']
title_count = {}

for string in title_list:
	match_0 = re.search(r'^associate+', string.lower())
	match_1 = re.search(r'^assistant+', string.lower())

	if match_0:
		if title_types[0] in title_count:
			title_count[title_types[0]] = title_count[title_types[0]] + 1
		else:
			title_count[title_types[0]] = 1
	if match_1:
		if title_types[1] in title_count:
			title_count[title_types[1]] = title_count[title_types[1]] + 1
		else:
			title_count[title_types[1]] = 1
	if (not match_0) and (not match_1):
		if title_types[2] in title_count:
			title_count[title_types[2]] = title_count[title_types[2]] + 1
		else:
			title_count[title_types[2]] = 1

print(title_count)

##Q4. 
# Find how many different email domains there are 
# (Ex: mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.). Print the list of unique email domains.


email_domain_list = map(lambda x: x.split("@")[1], email_list)
#print unique email domains as a list
print(list(set(email_domain_list)))
#-----------------------------------












